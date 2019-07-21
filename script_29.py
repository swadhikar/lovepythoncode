import re
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.circle_area(self.radius)  # call a static method

    @classmethod
    def from_csv(cls, input_csv):
        _, diameter, _ = input_csv.split(',')
        return cls(int(diameter) / 2)           # construct object

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2            # 78.53981633974483


c = Circle.from_csv('Tyre,10,50$')
print(  c.area()  )
