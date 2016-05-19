# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self, radius):
        circumference = self.radius * pi * 2
        return circumference

    def get_area(self, radius):
        circleArea = self.radius ** 2 * pi
        return circleArea

wheel = Circle(5)

print(wheel.get_circumference(5))
print(wheel.get_area(5))
