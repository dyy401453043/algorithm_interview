import torch
import torch.nn as nn
import math
from torch.nn.parameter import Parameter
from torch.tensor import Tensor
from torchsummary import summary

class NaiveLSTM(nn.Module):
    """Naive LSTM like nn.LSTM"""

    def __init__(self, input_size: int, hidden_size: int):
        super(NaiveLSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # 输入门的权重矩阵和bias矩阵
        self.w_ii = Parameter(Tensor(hidden_size, input_size))
        self.w_hi = Parameter(Tensor(hidden_size, hidden_size))
        self.b_ii = Parameter(Tensor(hidden_size, 1))
        self.b_hi = Parameter(Tensor(hidden_size, 1))

        # 遗忘门的权重矩阵和bias矩阵
        self.w_if = Parameter(Tensor(hidden_size, input_size))
        self.w_hf = Parameter(Tensor(hidden_size, hidden_size))
        self.b_if = Parameter(Tensor(hidden_size, 1))
        self.b_hf = Parameter(Tensor(hidden_size, 1))

        # 输出门的权重矩阵和bias矩阵
        self.w_io = Parameter(Tensor(hidden_size, input_size))
        self.w_ho = Parameter(Tensor(hidden_size, hidden_size))
        self.b_io = Parameter(Tensor(hidden_size, 1))
        self.b_ho = Parameter(Tensor(hidden_size, 1))

        # cell的的权重矩阵和bias矩阵
        self.w_ig = Parameter(Tensor(hidden_size, input_size))
        self.w_hg = Parameter(Tensor(hidden_size, hidden_size))
        self.b_ig = Parameter(Tensor(hidden_size, 1))
        self.b_hg = Parameter(Tensor(hidden_size, 1))

        self.reset_weigths()

    def reset_weigths(self):
        """reset weights
        """
        stdv = 1.0 / math.sqrt(self.hidden_size)
        for weight in self.parameters():
            nn.init.uniform_(weight, -stdv, stdv)

    def forward(self, inputs, state):
        """Forward
        Args:
            inputs: [1, 1, input_size]
            state: ([1, 1, hidden_size], [1, 1, hidden_size])
        """

        batch_size, seq_size , _ = inputs.size()

        if state is None:
            h_t = torch.zeros(1, self.hidden_size).t()
            c_t = torch.zeros(1, self.hidden_size).t()
        else:
            (h, c) = state
            h_t = h.squeeze(0).t()
            c_t = c.squeeze(0).t()

        hidden_seq = []

        # seq_size = 1
        for t in range(seq_size):
            x = inputs[:, t, :].t()
            # input gate
            i = torch.sigmoid(self.w_ii @ x + self.b_ii + self.w_hi @ h_t +
                              self.b_hi)
            # forget gate
            f = torch.sigmoid(self.w_if @ x + self.b_if + self.w_hf @ h_t +
                              self.b_hf)
            # cell
            g = torch.tanh(self.w_ig @ x + self.b_ig + self.w_hg @ h_t
                           + self.b_hg)
            # output gate
            o = torch.sigmoid(self.w_io @ x + self.b_io + self.w_ho @ h_t +
                              self.b_ho)

            c_next = f * c_t + i * g
            h_next = o * torch.tanh(c_next)
            c_next_t = c_next.t().unsqueeze(0)
            h_next_t = h_next.t().unsqueeze(0)
            hidden_seq.append(h_next_t)

        hidden_seq = torch.cat(hidden_seq, dim=0)
        return hidden_seq, (h_next_t, c_next_t)

def reset_weigths(model):
    """reset weights
    """
    for weight in model.parameters():
        nn.init.constant_(weight, 0.5)

if __name__ == '__main__':
    inputs = torch.ones(1, 2, 10)
    h0 = torch.ones(1, 1, 20)
    c0 = torch.ones(1, 1, 20)
    print(h0.shape, h0)
    print(c0.shape, c0)
    print(inputs.shape, inputs)
    # test naive_lstm with input_size=10, hidden_size=20
    naive_lstm = NaiveLSTM(10, 20)
    # summary(naive_lstm,input_size=(10,20))
    # reset_weigths(naive_lstm)
    output1, (hn1, cn1) = naive_lstm(inputs, (h0, c0))
    # print(hn1.shape, cn1.shape, output1.shape)
    # print(hn1)
    # print(cn1)
    # print(output1)
    lstm = nn.LSTM(10, 20, batch_first=True)
    # summary(lstm,input_size=((1,1,10),(1,1,20),(1,1,20)))
    # reset_weigths(lstm)
    # output2, (hn2, cn2) = lstm(inputs, (h0, c0))
    # print(hn2.shape, cn2.shape, output2.shape)
    # print(hn2)
    # print(cn2)
    # print(output2)
