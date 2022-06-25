import torch

#  where
cond=torch.rand(2,2)
'''tensor([[0.8585, 0.9838],
        [0.5668, 0.0524]])'''
a=torch.tensor([[0,0],
                [0,0]])
b=torch.tensor([[1,1],
                [1,1]])
cmp=torch.where(cond>0.5,a,b) # 大于0.5就更接近a，就是0;小于0.5就更接近b，就是1
'''tensor([[0, 0],
        [0, 1]])'''


#  gather

prob=torch.randn(4,10)
idx=prob.topk(dim=1,k=3)
'''values=tensor([[1.8941, 1.3225, 1.0519],
        [1.3793, 1.1874, 0.9102],
        [1.2787, 0.7500, 0.2828],
        [1.7199, 1.0766, 1.0284]]),
indices=tensor([[1, 4, 2],
        [7, 9, 0],
        [5, 7, 8],
        [2, 8, 9]]))
'''
label=torch.arange(10)+100
gat=torch.gather(label.expand(4,10),dim=1,index=idx.long())
print(idx)
print(label)
print(gat)