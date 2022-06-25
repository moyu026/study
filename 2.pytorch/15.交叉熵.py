import torch
from torch.nn import functional as F

#   Entropy
a=torch.full([4],1/4)
'''tensor([0.2500, 0.2500, 0.2500, 0.2500])'''
sp=a*torch.log2(a)   # y=a*log2(a)
'''tensor([-0.5000, -0.5000, -0.5000, -0.5000])'''
sp1=-(a*torch.log2(a)).sum() # y=-求和（a*log2(a))
'''tensor(2.)'''   # 值越大，惊喜度越低

a=torch.tensor([0.1,0.1,0.1,0.7])
sp2=-(a*torch.log2(a)).sum()
'''tensor(1.3568)'''  # 值越大，惊喜度越低

a=torch.tensor([0.001,0.001,0.001,0.999])
sp3=-(a*torch.log2(a)).sum()
'''tensor(0.0313)'''   # 熵值越小，惊喜度越高



#  cross entropy
'''H(P,Q)=-求和P*logQ
          =-P1*logQ1-P2*logQ2
          =-y*log(p)-(1-y)*log(1-p)'''

x=torch.randn(1,784)
w=torch.randn(10,784)

logits=x@w.t()

pred=F.softmax(logits,dim=1)

pred_log=torch.log(pred)

y=F.cross_entropy(logits,torch.tensor([3]))  # 用logist而不是pred,cross_entropy函数包含了softmax等函数
'''tensor(18.9161)'''
print(y)