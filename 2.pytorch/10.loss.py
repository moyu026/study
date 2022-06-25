from torch.nn import functional as F
import torch

#   autograd.grad
x=torch.ones(1)  # x初始化为1
w=torch.full([1],2.)  # w初始化为1*1维度的标量2
mes=F.mse_loss(torch.ones(1),x*w)  #F.mse_loss(loss,label)
'''tensor(1.)'''
w.requires_grad_()  # 表示w值需要梯度更新
mes=F.mse_loss(torch.ones(1),x*w)
w1=torch.autograd.grad(mes,[w])
'''(tensor([2.]),)'''


#    loss.backward
x=torch.ones(1)  # x初始化为1
w=torch.full([1],2.)  # w初始化为1*1维度的标量2
mes=F.mse_loss(torch.ones(1),x*w)  #F.mse_loss(loss,label)
'''tensor(1.)'''
w.requires_grad_()  # 表示w值需要梯度更新
mes=F.mse_loss(torch.ones(1),x*w)
mes.backward()
w2=w.grad
'''tensor([2.])'''


#   Softmax: 概率和加起来为1，大的更大，小的更小
a=torch.rand(3)
a.requires_grad_() # 表示a需要梯度更新
'''tensor([0.8453, 0.4746, 0.4804], requires_grad=True)'''
p=F.softmax(a,dim=0)  # 对a的0维度使用softmax函数
'''tensor([0.4194, 0.2895, 0.2912], grad_fn=<SoftmaxBackward>)'''
p1_a=torch.autograd.grad(p[1],[a],retain_graph=True) # p1对a求导，p1和a1下标相同为正，下标不同为负
'''(tensor([-0.1214,  0.2057, -0.0843]),)'''
p2_a=torch.autograd.grad(p[2],[a],retain_graph=True)#  p2对a求导，p2和a2下标相同为正，下标不同为负
'''(tensor([-0.1221, -0.0843,  0.2064]),)'''
