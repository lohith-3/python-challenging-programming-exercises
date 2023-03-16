# Question 47

# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# Hints
# Use def methodName(self) to define a method.


class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.pi * (self.radius * self.radius))


radius = int(input("Please enter radius value?\n"))
circle = Circle(radius)
print(circle.area())
