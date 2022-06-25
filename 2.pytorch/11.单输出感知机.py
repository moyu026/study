import torch
from torch.nn import functional as F

x=torch.randn(1,10)
w=torch.randn(1,10,requires_grad=True)

o=torch.sigmoid(x@w.t())  # [1,10]*[10,1]=[1,1]

loss=F.mse_loss(torch.ones(1,1),o)  #期望值和输出值的误差

loss.backward()  #  反向传播 loss对w偏导

w1=w.grad  # w的梯度
'''tensor([[-0.0143,  0.0738,  0.0400,  0.0044, -0.0538, -0.0130, -0.0108, -0.0174,
         -0.1354,  0.0039]])'''
print(w1)