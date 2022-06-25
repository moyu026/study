import torch

#  cat

a=torch.rand(4,32,8) # 4个班级，32个学生，8门课
b=torch.rand(5,32,8) # 5个班级，32个学生，8门课
# 除了相加的维度不同，其余维度数要相同
c=torch.cat([a,b],dim=0).shape # 班级相加，9个班级，32学生，8门课
'''torch.Size([9, 32, 8])'''

a1=torch.rand(4,3,16,32)
b1=torch.rand(4,3,16,32)
c=torch.cat([a1,b1],dim=2).shape
''''torch.Size([4, 3, 32, 32])'''


#  stack

a=torch.rand(32,8) # 第1个班级32个学生，8门课
b=torch.rand(32,8) # 第2个班级32个学生，8门课
c=torch.stack([a,b],dim=0).shape  # 合并的两个向量维度数要相同
'''torch.Size([2, 32, 8])''' # 合并成两个班级，32个学生，8门课


# split :根据长度拆分

'''c:torch.Size([2, 32, 8])'''
c=torch.stack([a,b],dim=0)
aa,bb=c.split([1,1],dim=0) # 把两个班级拆分成a一个班级，b一个班级
# print(aa.shape,bb.shape)
'''torch.Size([1, 32, 8]) torch.Size([1, 32, 8])'''

c=torch.rand(3,32,8)
a1,b1=c.split([1,2],dim=0) # 把3个班级拆分成a1一个班级，b1两个班级
# print(a1.shape,b1.shape)
'''torch.Size([1, 32, 8]) torch.Size([2, 32, 8])'''

c=torch.rand(6,32,8)
a2,b2=c.split(3,dim=0) # 把6个班级拆分成a2三个班级，b2三个班级
# print(a2.shape,b2.shape)
'''torch.Size([3, 32, 8]) torch.Size([3, 32, 8])'''

a3,b3=c.chunk(2,dim=0) # 把6个班级平均拆分成2分
print(a3.shape,b3.shape)
'''torch.Size([3, 32, 8]) torch.Size([3, 32, 8])'''