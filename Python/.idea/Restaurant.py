'''
#9-1餐馆
class Restaurant():
    def __init__(self,restaurabt_name,cuisine_type):
        self.name=restaurabt_name
        self.type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("The restaurant's name is "+self.name.title()+" and it's cuisine type is "+self.type+".")

    def open_restaurant(self):
        print("The restaurant is opening!")
    def number_print(self):
        print("Today,the restaurant has "+str(self.number_served)+" customers.")
    def set_number_served(self,number):
        self.number_served=number
    def increasement_number_served(self,increasement):
        self.number_served+=increasement
restaurant=Restaurant('Chongqing huoguo','Chuan cai')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_print()
#设定人数
restaurant.set_number_served(23)
restaurant.number_print()
#增加的人数
restaurant.increasement_number_served(11)
restaurant.number_print()



'''


'''
#9-3用户
class User():
    def __init__(self,name,age,sex,country):
        self.name=name
        self.age=age
        self.sex=sex
        self.country=country
        self.login_attempts=0
    def describe_user(self):
        print("The user's name is "+self.name.title()+".")
        if self.sex=='male':
            print("He is "+str(self.age)+".")
            print("He comes from "+self.country.title())
        else:
            print("She is " + str(self.age) + ".")
            print("She comes from " + self.country.title())
    def greet_user(self):
        if self.sex=='male':
            print("Hello Mr "+self.name.title()+".")
        else:
            print("Hello Mrs " + self.name.title() + ".")

    def increment_login_attempt(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

number1=User('shen cheng',20,'male','china')
number1.increment_login_attempt()
print(str(number1.login_attempts))
number1.increment_login_attempt()
print(str(number1.login_attempts))
number1.increment_login_attempt()
print(str(number1.login_attempts))
number1.increment_login_attempt()
print(str(number1.login_attempts))
number1.increment_login_attempt()
print(str(number1.login_attempts))
number1.reset_login_attempts()
print(str(number1.login_attempts))
'''


'''  
number1=User('shen cheng',20,'male','china')
number1.describe_user()
number1.greet_user()

print("\n")

number2=User('lucy',18,"female",'japan')
number2.describe_user()
number2.greet_user()

'''




class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("The car has drived "+str(self.odometer_reading)+" miles.")

    def updata_odometer(self,mileage):
        if mileage >self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer!")

    def increasement_odometer(self,miles):
        self.odometer_reading+=miles
    def fill_gas_tank(self):
        print("This car does need a gas tank.")
'''
#测试原函数
my_new_car=Car('audi','a8',2018)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading=2
my_new_car.read_odometer()

my_new_car.updata_odometer(13)
my_new_car.read_odometer()
print("\n")

my_new_car.updata_odometer(12)
my_new_car.read_odometer()
print("\n")

my_new_car.increasement_odometer(100)
my_new_car.read_odometer()
'''

'''
class battery():
    def __init__(self,battery_size=70):
        self.battery=battery_size
    def describe_battery(self):
        print("The car has a battery of " + str(self.battery) + "-kwh.")
    def get_range(self):
        if self.battery==70:
            print("240")
        elif self.battery==85:
            print("270")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=battery()
    def fill_gas_tank(self):
        print("This car does not need a gas tank.")
my_tesla=ElectricCar('tesla','Models s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()'''