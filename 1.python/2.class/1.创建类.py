class Dog():
    def __init__(self,name,age):  # 属性
        '''初始化属性name和age'''
        self.name = name # 以self为前缀的变量可供类中的所有方法使用
        self.age = age

    def sit(self):  # 创建方法
        print(self.name.title()+ " is now sitting")

    def roll_over(self):
        print(self.name.title() + " rolled over")

#-----创建实例
'''
my_dog = Dog('while',16)  # 实例
print("My dog's name is " + my_dog.name.title()+".") # title()将首字母改成大写
print("My dog is " + str(my_dog.age)+" years old")  #  str(my_dog.age) 将年龄转化成字符串
'''

#----调用方法
'''
my_dog = Dog('whille',16)
my_dog.sit()
my_dog.roll_over()
'''

#---创建多个实例
my_dog = Dog('whille',16)
your_dog = Dog('tony',26)

print("My dog's name is " + my_dog.name.title()+".")
print("My dog is " + str(my_dog.age)+" years old")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title()+".")
print("Your dog is " + str(your_dog.age)+" years old")
your_dog.roll_over()
