class Car():
    def __init__(self,make,model,year): # 初始化属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 给属性指定默认值

    def get_descriptive_name(self): # 返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
'''直接访问属性并修改值'''
my_new_car.odometer_reading = 23
my_new_car.read_odometer()