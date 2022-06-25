import torch

a=torch.rand(4,3,28,30)  # 4长图片，彩色通道数为3，高28，宽30
b=a[0].shape  # 第0张图片的维度，通道数为3，高28，宽30
'''torch.Size([3, 28, 30])'''

b1=a[0,0].shape # 第0张图片的第0个通道，高28，宽30
'''torch.Size([28, 30])'''

b2=a[0,0,2,4]  # 第0张图片的第0个通道的2行4列的像素值
'''tensor(0.9340)'''

#   连续采集
c=a[:2].shape # 第0张和第1张图片的维度
'''torch.Size([2, 3, 28, 30])'''
c=a[:2,:1].shape #前2张图片的前1个通道的维度,从前往后看
'''torch.Size([2, 1, 28, 30])'''
c=a[2:,1:].shape # 从后往前看
'''torch.Size([2, 2, 28, 30])'''
c=a[2:,-1:].shape # -1表示最后一个
'''torch.Size([2, 1, 28, 30])'''


#  离散采样
d=a[:,:,0:28:3,:].shape # 高从[0,28)隔3个点采样一次
'''torch.Size([4, 3, 10, 30])'''


# 具体位置采样
e=a.index_select(0,torch.tensor([0,2])).shape # 0表示a向量中的第0个位置，即图片数，然后采样[0,2]的图片
'''torch.Size([2, 3, 28, 30])'''

e=a.index_select(1,torch.tensor([1,2])).shape # 1表示向量a的第1个位置，即彩色通道，然后采样[1,2]通道即G,B通道
'''torch.Size([4, 2, 28, 30])'''

e=a.index_select(2,torch.arange(8)).shape # 2表示向量a的第2个位置，即行数，8表示[0,8)行
'''torch.Size([4, 3, 8, 30])'''


# 取任意位置
f=a[...].shape # a的所有维度都取
'''torch.Size([4, 3, 28, 30])'''

f=a[0,...,::2].shape # 第0张图片，通道数和行数都取，列隔2个采样
'''torch.Size([3, 28, 15])'''

f=a[...,:2].shape  # 前面的维度都取（张数，通道数，行数），列数取到2
'''torch.Size([4, 3, 28, 2])'''



#  masked_selected
x=torch.randn(3,4)
'''tensor([[-0.4735, -0.7832,  2.0504, -0.8353],
        [-0.0899, -1.4150, -0.1324, -0.2647],
        [ 0.4671, -1.0837,  0.6399, -1.1117]])'''
mask=x.ge(0.5) # 大于等于0.5为True,否则为False
'''tensor([[False, False,  True, False],
        [False,  True, False, False],
        [False, False, False, False]])'''
m=torch.masked_select(x,mask) # 取出x中大于等于0.5的数
'''tensor([0.6344, 2.2834, 0.7940, 1.0210])'''
print(m)
