class Shape:

    def __init__(self, h, w):
        self.w = w
        self.h = h


class Rectangle(Shape):
    def area(self):

        return (self.w * self.h)


class Triangle(Shape):

    def area(self):
        return (1 / 2) * (self.w * self.h)


triangle = Triangle(w=10, h=12)
rectangle = Rectangle(w=10, h=12)

print(triangle.area())  # -> 60
print(rectangle.area())  # -> 120
