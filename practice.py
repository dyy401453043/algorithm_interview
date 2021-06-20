import torch
import torch.nn as nn
import math

class ScaledDotProductionAttention(nn.Module):
    def __init__(self):
        super(ScaledDotProductionAttention, self).__init__()

    def forward(self,query,key,value,attn_mask):
        # query (batch_size, seq_len1, hidden1)
        # key (batch_size, seq_len2, hidden1)
        # value (batch_size, seq_len2, hiddn2)
        # attn_mask (batch_size, seq_len1, seq_len2)
        score = torch.matmul(query,key.transpose(-1,-2))/math.sqrt(query.size(-1)) # (batch_size, seq_len1, seq_len2)
        mask_score = torch.masked_fill(input=score, mask=attn_mask, value=1e-9)
        score_matrix = torch.softmax(mask_score,dim=1)
        output = torch.matmul(score_matrix,value)
        return output

class Attention(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Attention, self).__init__()
        self.wq = nn.Linear(input_size, hidden_size, bias=False)
        self.wk = nn.Linear(input_size, hidden_size, bias=False)
        self.wv = nn.Linear(input_size, hidden_size, bias=False)
        self.dot_procution = ScaledDotProductionAttention()

    def forward(self, seq1, seq2, attn_mask):
        # seq1, (batch_size, input_size)
        # seq2, (batch_size, input_size)
        query,key,value = self.wq(seq1),self.wk(seq2),self.wv(seq2)
        output = self.dot_procution(query,key,value,attn_mask)
        return output

class MultiheadAttention(nn.Module):
    def transpose_qkv(self, query, num_heads):
        # query (batch_size, seq, hidden)
        query = query.view(query.size(0),query.size(1),num_heads,-1) # (batch,seq,n,hidden/n)
        query = query.transpose(1,2).contiguous()# (batch,n,seq,hidden/n)
        query = query.view(-1,query.size(2),query.size(3))
        return query

    def transpose_output(self, output, num_heads):
        # output (batch*n,seq,hidden/n)
        output = output.view(-1,num_heads,output.size(1),output.size(2))
        output = output.transpose(1,2).contiguous()
        output = output.view(output.size(0),output.size(1),-1)
        return output

    def __init__(self, input_size, hidden_size, num_heads):
        super(MultiheadAttention,self).__init__()
        self.num_heads = num_heads
        self.wq = nn.Linear(input_size, hidden_size, bias=False)
        self.wk = nn.Linear(input_size, hidden_size, bias=False)
        self.wv = nn.Linear(input_size, hidden_size, bias=False)
        self.dot_procution = ScaledDotProductionAttention()

    def forward(self, seq1, seq2, attn_mask):
        query, key, value = self.wq(seq1), self.wk(seq2), self.wv(seq2)
        query, key, value = self.transpose_qkv(query,self.num_heads), self.transpose_qkv(key,self.num_heads), \
                            self.transpose_qkv(value,self.num_heads)
        output = self.dot_procution(query, key, value, attn_mask)
        output = self.transpose_output(output,self.num_heads)
        return output

if __name__ == '__main__':
    seq1 = torch.ones(4,10,100)
    seq2 = torch.ones(4,20,100)
    attn_mask = torch.zeros(4,10,20)
    attn = Attention(100,512)
    output = attn(seq1,seq2,attn_mask)
    print(output.shape)
    print(output)
