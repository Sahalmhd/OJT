#Shape Class with Rectangle and Circle Subclasses

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage:
rectangle = Rectangle(5, 10)
circle = Circle(7)

print(f"Rectangle Area: {rectangle.area()}")
print(f"Circle Area: {circle.area()}")