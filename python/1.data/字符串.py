# 三种序列类型：字符串、列表、元组
# 特征：第一个正索引为0.指向的是左端；第一个索引为负数时，指向的是右端
# 切片使用语法： [起始下标：结束下标：步长]，左闭右开；下标会越界，切片不会
'''
1.capitalize() 首字母变大写
2.endswith/startswith() 是否*结束/开始
3.find() 检测*是否在字符串中
4.isalnum() 判断是否是字母或数字
5.isalpha() 判断是否是字母
6.isdigit（） 判断是否是数字
7.islower（） 判断是否是小写
8.join（） 循环取出所有值用*去连接
9.lower/upper() 大小写转换
10.swapcase() 大小写互换
11.lstrip/rstrip/strip() 移除左右两侧空白
12.split() 切割字符串
13.title() 每个单词的首字母变大写
14.replace(old,new,count=None) old被替换字符串，new替换字符串，count换多少个，无count表示全部替换
15.count() 统计出现的次数
'''

# test='python'
# print('第一个字符%c'%test[0])
# for i in test:
#     print(i,end=' ')

# test='peter'
# print('首字母大写%s'%test.capitalize()) #首字母大写
# a='   hello   '
# b=a.strip() #去除字符串中空格
# print(b)
# print(a.lstrip()) #去除左边空格
# print(a.rstrip()) #去除右边空格


# str='A B CDE FGhalpAB'
# print(str.find('A')) #查找字符在字符串中第一次出现的序号
# print(str.find('8')) #未找到返回-1
# print(str.index('B')) #index也查找字符在字符串中第一次出现的序号，未找到则报错
# print(str.startswith('A')) #是否以A开头，True
# print(str.endswith('A'))  #是否以A结尾，False
# print(str.lower()) #变成小写
# print(str.upper()) #变成大写

# 切片操作 [start:end:step]
# str='helloworld'
# print(str) #输出完整数据
# print(str[0]) #输出第一个数据
# print(str[2:5]) #2-5，左闭右开
# print(str[2:])  #输出到最后
# print(str[:3]) #从开始输出
# print(str[::-1]) #倒序输出，-1表示方向，从右往左


# ----------格式化字符串—---------
'{0} b {1} {2}'.format('a', 'c', 'd')
tuple1=(1,2,3)
a=sum(tuple1,4)
print(a)
print(max(tuple1))
print(min(tuple1))