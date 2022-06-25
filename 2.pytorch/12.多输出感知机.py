from torch.nn import functional as F
import torch

x=torch.randn(1,10)
w=torch.randn(2,10,requires_grad=True)

o=torch.sigmoid(x@w.t())  # [1,10]*[10,2]=[1,2]

loss=F.mse_loss(torch.ones(1,2),o)  # 期望值与输出值的误差

loss.backward()  # 反向传播

w1=w.grad   # w的梯度
'''tensor([[-6.6600e-04, -7.8686e-05, -5.5310e-04,  6.1274e-04,  8.9517e-04,
          2.6186e-04, -7.3364e-05,  5.5617e-04, -2.5466e-04,  8.2058e-04],
        [-9.2853e-02, -1.0970e-02, -7.7113e-02,  8.5428e-02,  1.2480e-01,
          3.6509e-02, -1.0228e-02,  7.7541e-02, -3.5504e-02,  1.1440e-01]])'''
print(w1)