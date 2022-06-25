dicta={'pro':'艺术','school':'2123'}
a=[1,2,3,'abc']
# print(dicta.keys()) # 获取所有的键
# print(dicta.values()) #获取所有的值
# print(dicta.items()) #获取所有的键值对
# for i in dicta.items():  #获取所有的键值对
#     print(i)
# for key,value in dicta.items(): #获取所有的键值对
#     print('%s==%s'%(key,value))
cla_dict = dict((val, key) for key, val in dicta.items())
flower_list = dicta.class_to_idx
print(flower_list)