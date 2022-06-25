# 元组是一种不可变的序列，用（）创建元组类型，数据项用逗号分隔，可以是任何类型
# 当元组中只有一个元素时，要加逗号，否则会被当做整型

#tuple=('abc',123,3.14,[1,2,3])
# print(len(tuple))
# for i in tuple:
#     print(i,end=' ')
# print(tuple[1:3])
# print(tuple[::-1])
# print(tuple[-2:-1:])
# tuple[3][0]=321 #不能对元组数据项修改，但可以对元组中的列表数据进行修改
# print(tuple)

# tuple=('1',) #当元组中只有一个数据项的时候，必须在数据项后面加逗号
# print(type(tuple))
tupleA=tuple(range(5)) #强制转换成元组类型
print(tupleA)
a=(1,2,1,3,1)
print(a.count(1)) #统计个数


#--------更新元组--------
tuple1=(12,34,56,78)
tuple1=tuple1[:2]+('xxx',)+tuple1[2:]
print(tuple1)