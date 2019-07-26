from functools import reduce

class Polygon:
    def __init__(self, num_sides, *sides):
        self.sides = sides
        self.num_sides = num_sides

    def area(self):
        mul = lambda x, y: x * y              # multiply 2 numbers
        return reduce(mul, self.sides)        # multiply items in tuple

    def perimeter(self):
        return sum( self.num_sides * self.sides )

class Rectangle(Polygon):
    def __init__(self, *sides, num_side=2):   # enable subclassing
        super().__init__(num_side, *sides)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side, num_side=4)


s = Square(5)
r = Rectangle(2, 10)

print("Square area:", s.area())               # Square area: 25
print('Square perimeter:', s.perimeter())     # Square perimeter: 40
print("Rectangle area:", r.area())            # Rectangle area: 20
print("Rectangle perimeter:", r.perimeter())  # Rectangle perimeter: 24
