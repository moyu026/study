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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.updata_odometer(33)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()