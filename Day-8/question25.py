# Question 25

# Define a class, which have a class parameter and have a same instance parameter.

# Hints:
# Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

class Car:
    name = "Car"
    brand = "Toyato"

    def __init__(self, name):
        self.name = name


car = Car("fortuner")
print(car.name)
print(car.brand)
print(Car.brand)
print(Car.name)
car.name="range rover"
print(car.name)
print(Car.name)
