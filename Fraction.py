class Fraction:
    def __init__(self, numerator, denomenator):
        self.numerator = numerator
        if denomenator == 0:
            raise ValueError
        self.denomenator = denomenator

    def gcd(self, a, b):
        if b == 0:
            return abs(a)
        return self.gcd(b, a % b)

    def simplify(self):
        g = self.gcd(self.numerator, self.denomenator)
        self.numerator = self.numerator // g
        self.denomenator = self.denomenator // g
        return self

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denomenator + other.numerator * self.denomenator
            new_den = self.denomenator * other.denomenator
            return Fraction(new_num, new_den)
        raise TypeError

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.numerator * other.denomenator - other.numerator * self.denomenator
            new_den = self.denomenator * other.denomenator
            return Fraction(new_num, new_den)
        raise TypeError

    def __repr__(self):
        return f"Fraction({self.numerator},{self.denomenator})"

    def __str__(self):
        return f"{self.numerator}/{self.denomenator}"


f1 = Fraction(2, 4)  # автоматически сократится до 1/2
f2 = Fraction(1, 3)
print(f"f1 = {f1}")
print(f"f2 = {f2}")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"repr(f1) = {repr(f1)}")
