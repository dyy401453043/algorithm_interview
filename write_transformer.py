import torch
import torch.nn as nn
import numpy as np
# masked softmax
def SequenceMask(X, X_len, value=-1e6):
    maxlen = X.size(1)
    mask = torch.arange((maxlen), dtype=torch.float, device=X.device)[None, :] >= X_len[:, None]
    X[mask] = value
    return X


def masked_softmax(X, valid_length):
    # X: 3-D tensor, valid_length: 1-D or 2-D tensor
    softmax = nn.Softmax(dim=-1)
    if valid_length is None:
        return softmax(X)
    else:
        shape = X.shape
        if valid_length.dim() == 1:
            try:
                valid_length = torch.FloatTensor(valid_length.numpy().repeat(shape[1], axis=0))  # [2,2,3,3]
            except:
                valid_length = torch.FloatTensor(valid_length.cpu().numpy().repeat(shape[1], axis=0))  # [2,2,3,3]
        else:
            valid_length = valid_length.reshape((-1,))
        #         print(valid_length.device)
        # fill masked elements with a large negative, whose exp is 0
        X = SequenceMask(X.reshape((-1, shape[-1])), valid_length.to(X.device))

        return softmax(X).reshape(shape)

# Multi heads attention
class MultiHeadAttention(nn.Module):
    def __init__(self, input_size, hidden_size, num_heads, dropout, **kwargs):
        super(MultiHeadAttention, self).__init__(**kwargs)
        self.num_heads = num_heads
        self.attention = DotProductAttention(dropout)
        self.wq = nn.Linear(input_size, hidden_size, bias=False)
        self.wk = nn.Linear(input_size, hidden_size, bias=False)
        self.wv = nn.Linear(input_size, hidden_size, bias=False)
        self.wo = nn.Linear(hidden_size, hidden_size, bias=False)

    def forward(self, query, key, value, valid_length):
        query = transpose_qkv(self.wq(query), self.num_heads)
        key = transpose_qkv(self.wk(key), self.num_heads)
        value = transpose_qkv(self.wv(value), self.num_heads)
        valid_length = handle_valid_length(valid_length, self.num_heads)
        output = self.attention(query, key, value, valid_length)
        output_concat = transpose_output(output, self.num_heads)
        return self.wo(output_concat)

# feadfoward
class PositionWiseFFN(nn.Module):
    def __init__(self, input_size, ffn_hidden_size, hidden_size_out, **kwargs):
        super(PositionWiseFFN, self).__init__(**kwargs)
        self.ffn_1 = nn.Linear(input_size, ffn_hidden_size)
        self.ffn_2 = nn.Linear(ffn_hidden_size, hidden_size_out)

    def forward(self, X):
        return self.ffn_2(F.relu(self.ffn_1(X)))

# Add and Norm
class AddNorm(nn.Module):
    def __init__(self, hidden_size, dropout, **kwargs):
        super(AddNorm, self).__init__(**kwargs)
        self.dropout = nn.Dropout(dropout)
        self.norm = nn.LayerNorm(hidden_size)

    def forward(self, X, Y):
        return self.norm(self.dropout(Y) + X)

# position encoding
class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, dropout, max_len=1000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(dropout)
        self.P = np.zeros((1, max_len, embed_size))
        X = np.arange(0, max_len).reshape(-1, 1) / np.power(10000, np.arange(0, embed_size, 2) / embed_size)
        self.P[:, :, 0::2] = np.sin(X)
        self.P[:, :, 1::2] = np.cos(X)
        self.P = torch.FloatTensor(self.P)

    def forward(self, X):
        if X.is_cuda and not self.P.is_cuda:
            self.P = self.P.cuda()
        X = X + self.P[:, :X.shape[1], :]
        return self.dropout(X)

# encoder block
class EncoderBlock(nn.Module):
    def __init__(self, embed_size, ffn_hidden_size, num_heads, dropout, **kwargs):
        super(EncoderBlock, self).__init__(**kwargs)
        self.attention = MultiHeadAttention(embed_size, embed_size, num_heads, dropout)
        self.add_norm1 = AddNorm(embed_size, dropout)
        self.ffn = PositionWiseFFN(embed_size, ffn_hidden_size, embed_size)
        self.add_norm2 = AddNorm(embed_size, dropout)

    def forward(self, X, valid_length):
        Y = self.add_norm1(X, self.attention(X, X, X, valid_length))
        return self.add_norm2(Y, self.ffn(Y))

# Transformer encoder
class TransformerEncoder(Encoder):
    def __init__(self, vocab_size, embed_size, ffn_hidden_size, num_heads, num_layers, dropout, **kwargs):
        super(TransformerEncoder, self).__init__(**kwargs)
        self.embed_size = embed_size
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.pos_encoding = PositionalEncoding(embed_size, dropout)
        self.blocks = nn.ModuleList()
        for i in range(num_layers):
            self.blocks.append(EncoderBlock(embed_size, ffn_hidden_size, num_heads, dropout))

    def forward(self, X, valid_length, *args):
        X = self.pos_encoding(self.embedding(X) * math.sqrt(self.embed_size))
        for block in self.blocks:
            X = block(X, valid_length)
        return X

# Decoder block
class DecoderBlock(nn.Module):
    def __init__(self, embed_size, ffn_hidden_size, num_heads, dropout, i, **kwargs):
        super(DecoderBlock, self).__init__(**kwargs)
        self.i = i
        self.atten1 = MultiHeadAttention(embed_size, embed_size, num_heads, dropout)
        self.add_norm1 = AddNorm(embed_size, dropout)
        self.atten2 = MultiHeadAttention(embed_size, embed_size, num_heads, dropout)
        self.add_norm2 = AddNorm(embed_size, dropout)
        self.ffn = PositionWiseFFN(embed_size, ffn_hidden_size, embed_size)
        self.add_norm3 = AddNorm(embed_size, dropout)

    def forward(self, X, state):
        enc_outputs, enc_valid_length = state[0], state[1]
        if state[2][self.i] is None:
            key_value = X
        else:
            key_value = torch.cat((state[2][self.i], X), dim=1)
        state[2][self.i] = key_value

        if self.training:
            batch_size, seq_len, _ = X.shape
            valid_length = torch.FloatTensor(np.tile(np.arange(1, seq_len+1), (batch_size, 1)))
            valid_length = valid_length.to(X.device)
        else:
            valid_length = None
        X2 = self.atten1(X, key_value, key_value, valid_length)
        Y = self.add_norm1(X, X2)
        Y2 = self.atten2(Y, enc_outputs, enc_outputs, enc_valid_length)
        Z = self.add_norm2(Y, Y2)
        return self.add_norm3(Z, self.ffn(Z)), state

# Transformer decoder
class TransformerDecoder(Decoder):
    def __init__(self, vocab_size, embed_size, ffn_hidden_size, num_heads, num_layers, dropout, **kwargs):
        super(TransformerDecoder, self).__init__(**kwargs)
        self.embed_size = embed_size
        self.num_layers = num_layers
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.pos_encoding = PositionalEncoding(embed_size, dropout)
        self.blocks = nn.ModuleList()
        for i in range(num_layers):
            self.blocks.append(DecoderBlock(embed_size, ffn_hidden_size, num_heads, dropout, i))
        self.dense = nn.Linear(embed_size, vocab_size)

    def init_state(self, enc_outputs, enc_valid_length, *args):
        return [enc_outputs, enc_valid_length, [None] * self.num_layers]

    def forward(self, X, state):
        X = self.pos_encoding(self.embedding(X) * math.sqrt(self.embed_size))
        for block in self.blocks:
            X, state = block(X, state)
        return self.dense(X), state