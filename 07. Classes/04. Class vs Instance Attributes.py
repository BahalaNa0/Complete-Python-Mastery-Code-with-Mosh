"""
7. Classes, 04. Class vs Instance Attributes

Whenever new point object is created, it will inherit from the Point class.
Each instance can have different attributes. 
Classes can define the attributes.
Class attributes are applied to class instances. 
All class level changes apply to all instances in the class. 
"""


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
