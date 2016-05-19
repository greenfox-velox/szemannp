# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area
import pi from math
class = Circle:
    def get_circumference(self, radius):
        circumference = radius * pi * 2
        return circumference

    def get_area(self, radius):
        circleArea = radius ** 2 * pi
        return circleArea

wheel = Circle()

print(wheel.get_circumference(5))
