from car import Car  # 打开文件car.py并导入文件中的Car类

my_new_car = Car('longma','sss',2035)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 33
my_new_car.read_odometer()