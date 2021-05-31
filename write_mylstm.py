import torch
import torch.nn as nn
from torch.tensor import Tensor
from torch.nn.parameter import Parameter

class MyLSTM(nn.Module):

    def __init__(self, input_size, hidden_size):
        super(MyLSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # forget
        self.l_fi = nn.Linear(input_size, hidden_size)
        self.l_fh = nn.Linear(hidden_size, hidden_size)

        # input
        self.l_ii = nn.Linear(input_size, hidden_size)
        self.l_ih = nn.Linear(hidden_size, hidden_size)

        # memory
        self.l_mi = nn.Linear(input_size, hidden_size)
        self.l_mh = nn.Linear(hidden_size, hidden_size)

        # output
        self.l_oi = nn.Linear(input_size, hidden_size)
        self.l_oh = nn.Linear(hidden_size, hidden_size)

    def forward(self, input, state=None):
        # input (batch_size, seq_lengh, input_size)
        # state [(1,hidden),(1,hidden)]

        if state is None:
            ht_1 = torch.zeros(1,1,self.hidden_size)
            ct_1 = torch.zeros(1,1,self.hidden_size)
        else:
            ht_1 = state[0].squeeze(0)
            ct_1 = state[-1].squeeze(0)

        h_s,h_t,c_t = [],None,None
        for t in range(input.size()[1]):
            input_t = input[:,t,:]
            f = torch.sigmoid(self.l_fi(input_t) + self.l_fh(ht_1))
            i = torch.sigmoid(self.l_fi(input_t) + self.l_fh(ht_1))
            m = torch.tanh(self.l_fi(input_t) + self.l_fh(ht_1))
            o = torch.sigmoid(self.l_fi(input_t) + self.l_fh(ht_1))

            c_t = f*ct_1 + i*m
            h_t = o * torch.tanh(c_t)

            h_s.append(h_t.unsqueeze(0))

        hidden_seq = torch.cat(h_s,dim=0)
        return hidden_seq,(h_t,c_t)

def reset_weights(model):
    for param in model.parameters():
        nn.init.constant_(param,0.5)

if __name__ == '__main__':
    input = torch.ones(size=(1,1,10))
    h0 = torch.ones(size=(1,20))
    c0 = torch.ones(size=(1,20))
    mylstm = MyLSTM(10,20)
    reset_weights(mylstm)
    output1,(h1,c1) = mylstm(input,(h0,c0))
    print(output1.shape,c1.shape,h1.shape)
    print(output1,c1,h1)






