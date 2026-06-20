class Sequence:
    def __init__(self, numbers):
        self.numbers = numbers

    def factorial(self, num):
        if num <= 1:
            return 1
        return num * self.factorial(num-1)

    def factorial_sum(self, index=0):
        if index >= len(self.numbers):
            return 0
        return self.factorial(self.numbers[index]) + self.factorial_sum(index+1)

    def map_square(self):
        return Sequence(list(map(lambda x: x**2, self.numbers)))

    def filter_even(self):
        return Sequence(list(filter(lambda x: x % 2 == 0, self.numbers)))

    def __add__(self, other):
        if isinstance(other, Sequence):
            return Sequence(self.numbers + other.numbers)
        raise TypeError

    def __str__(self):
        return f"Sequence: {self.numbers}"


seq = Sequence([1, 2, 3, 4, 5])
print(f"Исходная: {seq}")
print(f"Сумма факториалов: {seq.factorial_sum()}")
print(f"Квадраты: {seq.map_square()}")
print(f"Чётные: {seq.filter_even()}")

seq2 = Sequence([6, 7, 8])
print(f"Объединённая: {seq + seq2}")
