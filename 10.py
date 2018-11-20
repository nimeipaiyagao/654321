'''class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name + " is now sitting")
    def roll(self):
        print(self.name + " is rolling")
my_dog = Dog("haha",6)
print("my dog's name is " + my_dog.name.title())
my_dog.roll()
my_dog.sit()


class Restaurant():
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restautant(self):
        print("THE " + self.name + " serves wonderful food.")
    def open_restaurant(self):
        print("The " + self.name + " is open.")
restautant = Restaurant("KFC","Fried Chicken")
restautant1 = Restaurant("MDL","Fried Chicken")
restautant2 = Restaurant("HDY","KAOROU")
print(restautant.name)
print(restautant.cuisine_type)

restautant.describe_restautant()
restautant1.describe_restautant()
restautant2.describe_restautant()


class User():
    def __init__(self,first_name,last_name,full_name,age):

        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.age = str(age)
    def describe_user(self):

        print("My name is " + self.first_name.title() +" "+ self.last_name.title() + ".")
        print('I am '+ self.age + ' years old.')

    def greet_user(self):
        print("Hello," + self.full_name.title()+ ".")

name =  User('yao','yuan','yaoyuan',24)
name.describe_user()
name.greet_user()
'''



class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading= 0
        self.fel_tank_capacity = 70
    def get_message(self):
        message = str(self.year) + " " + self.make + " " + self.model
        return message
    def odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def tank_capacity(self):
        print("The fuel tank capacity of this car is " + str(self.fel_tank_capacity) + " L.")
    def update_tank_capacity(self,L):
        self.fel_tank_capacity = L
my_car = Car("Audi","A4",2016)
my_car2= Car("长城","H6",2018)
print(my_car.get_message())
my_car.odometer()
my_car.update_odometer(10)
my_car.odometer()
my_car.fel_tank_capacity = 50
my_car.tank_capacity()

print(my_car2.get_message())
my_car.odometer_reading = 25
my_car.odometer()
my_car.tank_capacity()


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_capacity = 70
    def battery(self):
        print("This electric car has a " + str(self.battery_capacity) + " kwh battery capacity."  )
    def tank_capacity(self):
        print("This electric car has no fuel tank.")
my_electric_car = ElectricCar("小牛","尊享版",2018)
print(my_electric_car.get_message())
my_electric_car.battery()
my_electric_car.tank_capacity()
my_car3 = Car("本田","雅阁",2015)
print(my_car3.get_message())
my_car3.odometer_reading = 70000
my_car3.odometer()
my_car3.update_tank_capacity(100)
my_car3.tank_capacity()