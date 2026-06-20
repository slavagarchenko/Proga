class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def power(self, n):
        if n == 0:
            return Complex(1, 0)
        if n == 1:
            return Complex(self.real, self.imag)
        if n < 0:
            return Complex(1, 0) / self.power(-n)
        if n % 2:
            half = self.power(n//2)
            return half * half
        return self * self.power(n - 1)

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real, self.imag * other.imag)
        raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real / other.real, self.imag / other.imag)
        raise TypeError

    def conjugate(self):
        return Complex(self.real, -self.imag)

    @staticmethod
    def conjugate_all(numbers):
        return list(map(lambda x: x.conjugate(), numbers))

    def __repr__(self):
        return f"Complex({self.real}, {self.imag})"

    def __str__(self):
        return f"{self.real} {self.imag}"


c1 = Complex(3, 4)
print(f"c1 = {c1}")
print(f"c1^2 = {c1.power(2)}")
print(f"c1^3 = {c1.power(3)}")
print(f"c1^0 = {c1.power(0)}")
print(f"Сопряжённое: {c1.conjugate()}")

numbers = [Complex(1, 2), Complex(3, 4), Complex(5, 6)]
conjugated = Complex.conjugate_all(numbers)
print("Сопряжённые:")
for c in conjugated:
    print(c)
