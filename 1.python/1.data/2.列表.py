#特点：1.支持增删改查
#     2.数据项可以变化，内存地址不会变
#     3.用[]表示列表类型，数据项之间用逗号分隔，数据项可以是任何类型的数据
#     4.支持索引和切片操作
'''
1.append 在列表后面追加元素
2.count 统计出现次数
3.extend 拓展，相当于批量添加
4.index 获取指定元素索引号
5.insert 在指定位置插入
6.pop 删除最后一个元素
7.remove 一处左边找大的第一个元素
8.reverse 反转列表
9.sort 列表排序
'''

# a=[1,2,3,'abc']
# b='abcde'
# print(len(a)) #获取列表长度
# print(len(b)) #获取字符串长度

# a=['abc',123,2.36,True]
# print(a) #输出完整列表
# print(a[0]) #输出第一个元素
# print(a[1:3]) #从第二个开始到第三个元素
# print(a[1:]) #输出到最后
# print(a[:3]) #从开始输出
# print(a[::-1]) #倒序输出
# print(a*2) #输出两遍

#----------增加------------
# a=['abc',123,2.36,True]
# print('追加之前',a)
# a.append(['dada',256])
# print('追加之后',a)
# a.insert(1,'插入的数据') #insert(位置，数据)
# print(a)

# rsdata=list(range(10)) #强制转换成list对象
# a.extend(rsdata)   #拓展，也就是批量增加
# a.extend([1,2,66])
# print(a)

#-------------修改-------
# a=['abc',123,2.36,True]
# print('修改之前',a)
# a[1]=3.14
# print('修改之后',a)

#------------删除----------
#a=['abc',123,2.36,True]
# del a[1] #删除某个元素
# del a[1:3] #批量删除
# a.remove(123) #删除指定元素
# a.pop(2)  #删除指定位置元素

# b=a.index(123) #查找元素所在位置
# print(b)

#---------拷贝----------
a=[1,2,3,4]
b=a
c=a[:]
print(b)
print(c)
a.reverse()
print(b)    # b发生改变
print(c)    # c未发生改变