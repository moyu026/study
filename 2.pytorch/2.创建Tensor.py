import torch
import numpy as np

a=np.array([2,3.4])
'''[2.  3.4]'''
b=torch.from_numpy(a)
'''tensor([2.0000, 3.4000], dtype=torch.float64)'''

a1=np.ones([2,3])
'''[[1. 1. 1.]
 [1. 1. 1.]]'''
c=torch.from_numpy(a1)
'''tensor([[1., 1., 1.],
        [1., 1., 1.]], dtype=torch.float64)'''

# torch.tensor（）接收现有的数据；
# torch.Tensor() 接受现有的数据或者维度数
a2=torch.tensor([2,3.2])
'''tensor([2.0000, 3.2000])'''
a3=torch.FloatTensor([2,3.2])
'''tensor([2.0000, 3.2000])'''
a4=torch.FloatTensor(2)
'''tensor([1.1785e-42, 0.0000e+00])'''
a5=torch.FloatTensor(2,3)
'''tensor([[0., 0., 0.],
        [0., 0., 0.]])'''


####### 生成未初始化数据
b1=torch.empty(2)
'''tensor([       nan, 4.5908e-41])'''
b1=torch.empty(3)
'''tensor([-3.2985e+29,  4.5908e-41,  1.1959e+08])'''

b2=torch.Tensor(2,3)
'''tensor([[0., 0., 0.],
        [0., 0., 0.]])'''
b2=torch.FloatTensor(3,3)
'''tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])'''


###### 随机初始化
c1=torch.rand(3,2)  # rand:均匀分布[0,1]
'''tensor([[0.2460, 0.4487],
        [0.9593, 0.4172],
        [0.5495, 0.3877]])'''
c2=torch.rand_like(c1)   # 接收c1的维度数
'''tensor([[0.7039, 0.9948],
        [0.5906, 0.2905],
        [0.3309, 0.6727]])'''

c3=torch.randint(1,10,[3,4]) # 指定范围[1,10),3行4列
'''tensor([[6, 3, 4, 9],
        [3, 3, 5, 1],
        [9, 1, 4, 5]])'''

c4=torch.randn(3,4)  # randn：正态分布
'''tensor([[ 1.8980, -1.8849,  1.0240,  0.0489],
        [ 0.9590, -1.7477,  0.5193, -1.9899],
        [-0.3370, -0.7566,  0.3651, -0.7651]])'''


### 初值全部赋值同一个数值
d1=torch.full([2, 3], 3.1) #**** 3.1改成整数会报错,整数要写3.
'''tensor([[3.1000, 3.1000, 3.1000],
        [3.1000, 3.1000, 3.1000]])'''
d2=torch.full([],2.) # 维度为0的标量
'''tensor(2.)'''


####  生成等差数列
e=torch.arange(0,10) # [0,10)的等差数列
'''tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])'''
e1=torch.arange(0,10,2)  # [0,10)的等差数列，公差为2
'''tensor([0, 2, 4, 6, 8])
'''


##### 生成等分数列
f1=torch.linspace(0,10,steps=4) # [0,10]的距离4等分
'''tensor([ 0.0000,  3.3333,  6.6667, 10.0000])'''
f1=torch.linspace(0,10,steps=10)
'''tensor([ 0.0000,  1.1111,  2.2222,  3.3333,  4.4444,  5.5556,  6.6667,  7.7778,
         8.8889, 10.0000])'''
f1=torch.linspace(0,10,steps=11)
'''tensor([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])'''


### 生成特殊矩阵
e=torch.ones(3,3) # 生成全是1的矩阵
'''tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])'''
e=torch.zeros(3,3)  # 生成全是0的矩阵
'''tensor([[0., 0., 0.],
        [0., 0., 0.],
        [0., 0., 0.]])'''
e=torch.eye(3,3)   # 生成对角矩阵
'''tensor([[1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]])
'''

e1=torch.ones_like(e) # 生成矩阵e维度的单位阵
'''tensor([[1., 1., 1.],
        [1., 1., 1.],
        [1., 1., 1.]])
'''


###  random,shuffle
f1=torch.randperm(10) # 生成[0,10)的数并随机排列
'''tensor([8, 7, 0, 2, 3, 9, 4, 1, 5, 6])'''


#####  shuffle
'''
list = [20, 16, 10, 5]
random.shuffle(list)
print "随机排序列表 : ",  list

random.shuffle(list)
print "随机排序列表 : ",  list

以上实例运行后输出结果为：
随机排序列表 :  [16, 5, 10, 20]
随机排序列表 :  [16, 5, 20, 10]
'''

a = torch.rand(2,3)
b = torch.rand(2,2)
idx=torch.randperm(2)
print(a[idx])
'''tensor([[0.3221, 0.3104, 0.7335],
        [0.7737, 0.1862, 0.1792]])'''
print(b[idx])
'''tensor([[0.6458, 0.9410],
        [0.1616, 0.2893]])'''