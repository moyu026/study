import torch
import torch.nn as nn
from torch.nn import functional as F


x = torch.rand(1,16,14,14)
a1=x.size()
'''torch.Size([1, 16, 14, 14])'''

layer = nn.MaxPool2d(2,stride = 2)  # Max pooling
out = layer(x)
a2=out.size()
'''torch.Size([1, 16, 7, 7])'''

out = F.avg_pool2d(x,2,stride = 2)  # Avg pooling
a2=out.size()
'''torch.Size([1, 16, 7, 7])'''

x = torch.rand(1,16,14,14)
a1=x.size()
'''torch.Size([1, 16, 14, 14])'''

out =  F.interpolate(x,scale_factor = 2,mode = 'nearest')  # 上采样，upsample,尺寸扩大2倍
a2=out.shape
'''torch.Size([1, 16, 28, 28])'''

out =  F.interpolate(x,scale_factor = 3,mode = 'nearest')  # 上采样，upsample,尺寸扩大3倍
a2=out.shape
'''torch.Size([1, 16, 42, 42])'''
print(a2)