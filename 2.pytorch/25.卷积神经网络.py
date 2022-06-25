import torch
import torch.nn as nn
from torch.nn import functional as F

# input_channels,kernel_channels,kernel_size,stride,padding

layer = nn.Conv2d(1,3,kernel_size = 3,stride = 1,padding = 0) # 2d图像，(通道数为1，卷积核数为3，卷积核大小3*3，步长为1，填充为0)
x = torch.rand(1,1,28,28)

out = layer.forward(x)
a1=out.size()
'''torch.Size([1, 3, 26, 26])'''

layer = nn.Conv2d(1,3,kernel_size = 3,stride = 1,padding = 1)
out = layer.forward(x)
a1=out.size()
'''torch.Size([1, 3, 28, 28])'''

layer = nn.Conv2d(1,3,kernel_size = 3,stride = 2,padding = 1)
out = layer.forward(x)
a1=out.size()
'''torch.Size([1, 3, 14, 14])'''

out = layer(x) # 自带的卷积计算参数
a1=out.size()
'''torch.Size([1, 3, 14, 14])'''

a2=layer.weight
'''Parameter containing:
tensor([[[[ 0.0976,  0.1545,  0.1531],
          [ 0.2062, -0.1283, -0.3236],
          [-0.0444, -0.2197,  0.3263]]],


        [[[-0.2230,  0.2094,  0.0123],
          [ 0.0168,  0.1726, -0.2751],
          [ 0.1499, -0.0235,  0.0867]]],


        [[[-0.1319, -0.2068,  0.1821],
          [ 0.0588,  0.2992, -0.0257],
          [-0.3282, -0.1992,  0.0282]]]], requires_grad=True)'''


w = torch.rand(16,3,5,5)
b = torch.rand(16)
x = torch.randn(1,3,28,28)

out = F.conv2d(x,w,b,stride = 1,padding = 1)
a2=out.size()
'''torch.Size([1, 16, 26, 26])'''

out = F.conv2d(x,w,b,stride = 2,padding = 2)
a2=out.size()
'''torch.Size([1, 16, 14, 14])'''
