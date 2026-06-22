from functools import reduce


class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        if denominator == 0:
            raise ValueError
        self._denominator = denominator
        self.simplier()

    @staticmethod
    def gcd_recursive(a, b):
        if b == 0:
            return abs(a)
        return Fraction.gcd_recursive(b, a % b)

    def simplier(self):
        g = self.gcd_recursive(self._numerator, self._denominator)
        self._numerator = self._numerator / g
        self._denominator = self._denominator / g
        return self

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int) or value == 0:
            raise ValueError
        self._denominator = value

    @property
    def value(self):
        return self._numerator / self._denominator

    @property
    def is_proper(self):
        return abs(self._numerator) < abs(self._denominator)

    @property
    def is_improper(self):
        return abs(self._numerator) > abs(self._denominator)

    @property
    def is_integer(self):
        return int(self._numerator/self._denominator) == (self._numerator/self._denominator)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        new_n = self._numerator * other._denominator + \
            other._numerator * self._denominator
        new_d = self._denominator * other._denominator
        g = self.gcd_recursive(new_n, new_d)
        new_n = new_n / g
        new_d = new_d / g
        return Fraction(new_n, new_d)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        new_n = self._numerator * other._denominator - \
            self._denominator * other._numerator
        new_d = self._denominator * other._denominator
        g = self.gcd_recursive(new_n, new_d)
        new_n = new_n / g
        new_d = new_d / g
        return Fraction(new_n, new_d)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        new_n = self._numerator * other._numerator
        new_d = self._denominator * other._denominator
        g = self.gcd_recursive(new_n, new_d)
        new_n = new_n / g
        new_d = new_d / g
        return Fraction(new_n, new_d)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        new_n = self._numerator * other._denominator
        new_d = self._denominator * other._numerator
        if new_d == 0:
            raise TypeError
        g = self.gcd_recursive(new_n, new_d)
        new_n = new_n / g
        new_d = new_d / g
        return Fraction(new_n, new_d)

    def __iadd__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        self._numerator = self._numerator * other._denominator + \
            other._numerator * self._denominator
        self._denominator = self._denominator * other._denominator
        g = self.gcd_recursive(self._numerator, self._denominator)
        self._numerator = self._numerator / g
        self._denominator = self._denominator / g
        return self

    def __isub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        self._numerator = self._numerator * other._denominator - \
            other._numerator * self._denominator
        self._denominator = self._denominator * other._denominator
        g = self.gcd_recursive(self._numerator, self._denominator)
        self._numerator = self._numerator / g
        self._denominator = self._denominator / g
        return self

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return (self._numerator * other._denominator) == (other._numerator * self._denominator)

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return (self._numerator * other._denominator) < (other._numerator * self._denominator)

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return (self._numerator * other._denominator) > (other._numerator * self._denominator)

    @staticmethod
    def filter_by_value(fractions, min_val, max_val):
        return list(filter(lambda x: x.value < max_val and x.value > min_val, fractions))

    @staticmethod
    def map_to_decimal(fractions):
        return list(map(lambda x: x.value, fractions))

    @staticmethod
    def reduce_sum(fractions):
        return reduce(lambda y, x: y + x, fractions)

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def mixed(self):
        """Возвращает смешанное число в виде строки"""
        if self._numerator == 0:
            return "0"
        if self.is_proper:
            return str(self)

        whole = self._numerator // self._denominator
        remainder = abs(self._numerator % self._denominator)

        if remainder == 0:
            return str(whole)

        sign = "-" if self._numerator < 0 else ""
        return f"{sign}{abs(whole)} {remainder}/{self._denominator}"

    def reciprocal(self):
        """Возвращает обратную дробь"""
        if self._numerator == 0:
            raise ValueError("Нельзя найти обратную дробь для нуля")
        return Fraction(self._denominator, self._numerator)


print("=" * 60)
print("ПРОВЕРКА ЗАДАНИЯ 44")
print("=" * 60)

# 1. Создание дробей
f1 = Fraction(3, 4)
f2 = Fraction(2, 3)

print("1. Созданные дроби:")
print(f"   f1 = {f1}")
print(f"   f2 = {f2}")
print(f"   repr(f1) = {repr(f1)}")

# 2. Арифметические операции
print("\n2. Арифметические операции:")
print(f"   f1 + f2 = {f1 + f2}")
print(f"   f1 - f2 = {f1 - f2}")
print(f"   f1 * f2 = {f1 * f2}")
print(f"   f1 / f2 = {f1 / f2}")

# 3. Операторы += и -=
print("\n3. Операторы += и -=:")
f3 = Fraction(1, 2)
f3 += Fraction(1, 3)
print(f"   f3 += 1/3 -> {f3}")
f3 -= Fraction(1, 6)
print(f"   f3 -= 1/6 -> {f3}")

# 4. Геттеры
print("\n4. Геттеры:")
print(f"   Значение f1: {f1.value:.4f}")
print(f"   f1 правильная? {f1.is_proper}")
print(f"   f1 неправильная? {f1.is_improper}")
print(f"   f1 целое число? {f1.is_integer}")

f4 = Fraction(7, 3)
print(f"\n   f4 = {f4}")
print(f"   f4 правильная? {f4.is_proper}")
print(f"   f4 неправильная? {f4.is_improper}")
print(f"   f4 целое число? {f4.is_integer}")

# 5. Дополнительные методы
print("\n5. Дополнительные методы:")
print(f"   Смешанное число f4: {f4.mixed()}")
print(f"   Обратная дробь f4: {f4.reciprocal()}")

f5 = Fraction(8, 4)
print(f"   f5 = {f5}")
print(f"   Смешанное число f5: {f5.mixed()}")

# 6. Рекурсия
print("\n6. Рекурсия:")
print(f"   НОД(48, 18) = {Fraction.gcd_recursive(48, 18)}")
print(f"   НОД(100, 35) = {Fraction.gcd_recursive(100, 35)}")

# 7. Функциональное программирование
print("\n7. Функциональное программирование:")
fractions = [
    Fraction(1, 2),   # 0.5
    Fraction(3, 4),   # 0.75
    Fraction(5, 3),   # 1.67
    Fraction(2, 5),   # 0.4
    Fraction(7, 4)    # 1.75
]

print("   Список дробей:")
for i, f in enumerate(fractions):
    print(f"     f{i+1} = {f} = {f.value:.2f}")

filtered = Fraction.filter_by_value(fractions, 0.5, 1.5)
print(f"\n   Дроби в диапазоне [0.5, 1.5]: {[str(f) for f in filtered]}")

decimals = Fraction.map_to_decimal(fractions)
print(f"   Десятичные значения: {[round(d, 3) for d in decimals]}")

sum_result = Fraction.reduce_sum(fractions)
print(f"   Сумма всех дробей: {sum_result} = {sum_result.value:.3f}")

# 8. Сравнения
print("\n8. Сравнения:")
print(f"   f1 < f2? {f1 < f2}")
print(f"   f1 > f2? {f1 > f2}")
print(f"   f1 == f2? {f1 == f2}")

f6 = Fraction(6, 8)  # сократится до 3/4
print(f"\n   f6 = {f6} (создана как 6/8, автоматически сократилась)")
print(f"   f1 == f6? {f1 == f6}")
