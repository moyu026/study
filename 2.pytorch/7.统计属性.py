import torch

a=torch.full([8],1.)
'''tensor([1., 1., 1., 1., 1., 1., 1., 1.])'''
b=a.view(2,4)
'''tensor([[1., 1., 1., 1.],
        [1., 1., 1., 1.]])'''
c=a.view(2,2,2)
'''tensor([[[1., 1.],
         [1., 1.]],

        [[1., 1.],
         [1., 1.]]])'''

a1=a.norm(1)  # 1范数 tensor(8.)
b1=b.norm(1)  # 1范数 tensor(8.)
c1=c.norm(1)  # 1范数 tensor(8.)

a2=a.norm(2)  # 2范数 tensor(2.8284)
b2=b.norm(2)  # 2范数 tensor(2.8284)
c2=c.norm(2)  # 2范数 tensor(2.8284)

b11=b.norm(1,dim=1) #  b向量1维度的1范数
'''tensor([4., 4.])'''
b12=b.norm(2,dim=1) #  b向量1维度的2范数
'''tensor([2., 2.])'''

c11=c.norm(1,dim=1) #  c向量1维度的1范数
'''tensor([[2., 2.],
        [2., 2.]])'''
c12=c.norm(2,dim=1) #  c向量1维度的2范数
'''tensor([[1.4142, 1.4142],
        [1.4142, 1.4142]])'''


a=torch.tensor([[0.,1.,2.,3.],[4.,5.,6.,7.]])
a1=a.mean() # 均值   tensor(3.5000)
a2=a.max()  # 最大值  tensor(7.)
a3=a.min()  # 最小值  tensor(0.)
a4=a.prod() # 累乘值  tensor(0.)
a5=a.sum()  # 求和    tensor(28.)
a6=a.argmax()  # 最大值索引  tensor(7) 打平之后的索引
a7=a.argmin()  # 最小值索引  tensor(0) 打平之后的索引

a=torch.rand(4,10)
'''a[0]=tensor([0.6807, 0.1421, 0.4733, 0.5921, 0.9241, 0.7086, 0.9215, 0.0784, 0.9913,
        0.2250])'''
# print(a[0])
a0=a.argmax(dim=1)    # 指定维度最大值的索引
'''tensor([6, 1, 3, 2])'''


a=torch.rand(4,10)
'''tensor([[0.9161, 0.8370, 0.3848, 0.9213, 0.1679, 0.2144, 0.1095, 0.8617, 0.1634,
         0.9775],
        [0.8073, 0.9927, 0.6955, 0.7911, 0.2509, 0.9945, 0.2332, 0.2816, 0.5257,
         0.8899],
        [0.8537, 0.0825, 0.9181, 0.9950, 0.4268, 0.9205, 0.7377, 0.9617, 0.1353,
         0.2058],
        [0.9483, 0.7985, 0.2682, 0.0027, 0.4036, 0.1234, 0.6511, 0.4877, 0.7308,
         0.3066]])'''
a_max=a.max(dim=1)  # 1维度的最大值，返回数和索引
'''torch.return_types.max(
values=tensor([0.8941, 0.9829, 0.9845, 0.6834]),
indices=tensor([7, 1, 7, 8]))'''

a_max=a.max(dim=1,keepdim=True)  # 1维度的最大值，保持原维度不变
'''torch.return_types.max(
values=tensor([[0.9734],
        [0.7659],
        [0.9623],
        [0.7550]]),
indices=tensor([[2],
        [6],
        [0],
        [5]]))'''

a_max=a.argmax(dim=1,keepdim=True)  # 1维度最大值的索引，维度保持不变
'''tensor([[3], 
        [5],
        [3],
        [0]])'''

a_top3=a.topk(3,dim=1)   # 1维度最大的3个数及其索引
'''torch.return_types.topk(
values=tensor([[0.8553, 0.6735, 0.6342],
        [0.9237, 0.8017, 0.7291],
        [0.9263, 0.9112, 0.9061],
        [0.7413, 0.7005, 0.6153]]),
indices=tensor([[3, 5, 2],
        [3, 0, 9],
        [1, 7, 4],
        [9, 1, 0]]))'''

a_bottom3=a.topk(3,dim=1,largest=False)  # 1维度最小3个数及其索引
'''torch.return_types.topk(
values=tensor([[0.0504, 0.4418, 0.4956],
        [0.1078, 0.2179, 0.2690],
        [0.0767, 0.2043, 0.3528],
        [0.0142, 0.0314, 0.1857]]),
indices=tensor([[0, 4, 6],
        [7, 6, 8],
        [3, 0, 4],
        [6, 7, 5]]))'''

a_small8=a.kthvalue(8,dim=1)  # 1维度第8小的值
'''torch.return_types.kthvalue(
values=tensor([0.6852, 0.7760, 0.7694, 0.5975]),
indices=tensor([9, 3, 6, 1]))
'''


b=a>0 #  判断a中大于0的值
'''tensor([[True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True]])'''

b=torch.gt(a,0)  # 判断a中大于0的值
'''tensor([[True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True]])'''

b1=a!=0  # 判断a中不等于0的值
'''tensor([[True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True]])'''

a=torch.ones(2,3)
b=torch.rand(2,3)
eq=torch.eq(a,b) # 比较a,b中元素是否相等
'''tensor([[False, False, False],
        [False, False, False]])'''
eq1=torch.eq(a,a)
'''tensor([[True, True, True],
        [True, True, True]])'''
print(eq1)