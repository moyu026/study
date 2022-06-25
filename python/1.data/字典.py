# 字典时由 键值对 组成的集合，通常使用键来访问数据，效率非常高，和list一样支持添加、修改、删除
# 特点：1.无视序列类型，没有下标概念，是一个无序的键值集合，是内置的高级数据类型
#      2.用{}表示字典对象，每个键值用逗号分隔
#      3.键 必须是不可变得类型， 【元组、字符串】值可以是任意的类型
#      4.每个键必定是惟一的，如果存在重复的键，后者会覆盖前者

#----创建字典----
dicta={'pro':'艺术','school':'2123'}    #字典
dicta['name']='123' #key:value
dicta['age']=30
dicta['job']='singer'
# print(dicta)
# print(len(dicta)) #长度
# print(dicta['name']) #通过键获取对应的值
# dicta['name']='abc'  #修改键对应的值
# print(dicta)

# print(dicta.keys()) # 获取所有的键
# print(dicta.values()) #获取所有的值
# print(dicta.items()) #获取所有的键值对
# for i in dicta.items():  #获取所有的键值对
#     print(i)
# for key,value in dicta.items(): #获取所有的键值对
#     print('%s==%s'%(key,value))

#---------修改--------
# dicta['name']='abc'  #修改键对应的值
# dicta.update({'height':1.80}) #可以添加或者更新
# print(dicta)

#----------删除-----
# del dicta['name'] #通过指定键进行删除
# dicta.pop('age')    #通过指定键进行删除
# print(dicta)

#--------------排序------
