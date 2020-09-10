'''class Restaurant():
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



class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		"""初始化属性restaurant_name和cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)
	def open_restaurant(self):
		print('Restaurant is open')
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.favorite = ['orange','apple']
	def show_ice(self):
		for i in self.favorite:
			print(i)

IceCreamStand1 = IceCreamStand('beijingfandian','beijingcai')
IceCreamStand1.show_ice()        '''

class User():
	def __init__(self, first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
	def describe_user(self):
		print('用户名称为：' + self.first_name + self.last_name)
	def greet_user(self):
		print('你好！ ' + self.first_name + self.last_name)

class Admin(User):
	def __init__(self,first_name,last_name):
		super().__init__(first_name,last_name)
		self.b = Privileges()
		# self.privileges = ['can add post','can del post','can ban user']
	# def show_privileges(self):
	# 	# print(self.privileges)
	# 	for i in self.privileges:
	# 		print("管理员权限有：" + i)

class Privileges():
	def __init__(self):
		self.privileges = ['can add post','can del post','can ban user']
	def show_privileges(self):
		for i in self.privileges:
			print("管理员权限有：" + i)

Admin1 = Admin('Ma','Yun')
Admin1.describe_user()

Admin1.b.show_privileges()