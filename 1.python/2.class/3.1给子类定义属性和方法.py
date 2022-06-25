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

    def updata_odometer(self,mileage):
        '''将里程表读书设置成指定的值'''
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        '''将里程读书增加指定的量'''
        self.odometer_reading += miles

#-----创建子类时，父类必须包含在当前文件中，且位于子类前面
class Electriccar(Car): # 定义子类时，必须在括号内指定父类名称
    def __init__(self,make,model,year):
        '''初始化父类属性'''
        super().__init__(make,model,year) # super():让子类包含父类所以特性
        '''定义子类的属性'''
        self.battery_size = 70  # 所有Electriccar类包含这个属性，但是父类Car不包括这个属性

    def describe_battery(self):
        print('thi car has a ' + str(self.battery_size) + '-kWh battery.')
'''如果父类和子类有相同的方法，在调用该方法时，只会调用子类中的方法，不会调用父类中的方法'''

my_supercar = Electriccar('banche','model s',2016)
print(my_supercar.get_descriptive_name())
my_supercar.describe_battery()