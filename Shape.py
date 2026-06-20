import math


class Shape:
    def area(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle (r = {self.radius})"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle (widht = {self.width}, height = {self.height})"


def total_area(shapes, index=0):
    if index >= len(shapes):
        return 0
    return shapes[index].area() + total_area(shapes, index+1)


def filter_by_type(shapes, shape_type):
    return list(filter(lambda x: isinstance(x, shape_type), shapes))


shapes = [
    Circle(5),
    Rectangle(4, 6),
    Circle(3),
    Rectangle(2, 8)
]

print("Круги:")
for circle in filter_by_type(shapes, Circle):
    print(circle)

print(f"\nОбщая площадь всех фигур: {total_area(shapes):.2f}")
