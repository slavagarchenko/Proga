class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError
        self._width = value

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2*self._width + 2*self._height

    @classmethod
    def from_string(cls, s):
        w, h = map(int, s.split("x"))
        return cls(w, h)

    @staticmethod
    def is_square(width, height):
        return width == height

    def __str__(self):
        return f"{self._width} x {self._height}"


r = Rectangle(5, 10)
print(r)
print(f"Площадь: {r.area}, Периметр: {r.perimeter}")

r.width = 7
print(f"После изменения ширины: {r}")

# Проверка валидации
try:
    r.width = -3
except ValueError as e:
    print(f"Ошибка: {e}")

r2 = Rectangle.from_string("4x6")
print(f"Создан из строки: {r2}")

print(f"Является ли 5x10 квадратом? {Rectangle.is_square(5, 10)}")
print(f"Является ли 5x5 квадратом? {Rectangle.is_square(5, 5)}")
