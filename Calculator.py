import math


class Calculator:
    def __init__(self, history=None):
        self._history = history if history is not None else []

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        if not isinstance(value, list):
            raise ValueError
        if not all(isinstance(h, str) for h in value):
            raise ValueError
        self._history = value

    @property
    def last_result(self):
        if self._history is None:
            return None
        return self._history[-1]

    @property
    def operation_count(self):
        return len(self._history)

    def _add_to_history(self, operation, result):
        self._history.append(f"{operation} = {result}")
        return result

    def add(self, a, b):
        result = a + b
        return self._add_to_history(f"{a} + {b}", result)

    def sub(self, a, b):
        result = a - b
        return self._add_to_history(f"{a} - {b}", result)

    def mul(self, a, b):
        result = a * b
        return self._add_to_history(f"{a} * {b}", result)

    def div(self, a, b):
        if b == 0:
            raise ValueError
        result = a / b
        return self._add_to_history(f"{a}/{b}", result)

    def recursive_sum(self, numbers, index=0, result=0):
        if index >= len(numbers):
            return result
        result += numbers[index]
        return self.recursive_sum(numbers, index+1, result)

    def clear_history(self):
        self._history = []

    @staticmethod
    def is_valid_number(value):
        if not isinstance(value, (int, float)):
            return False
        return True

    @classmethod
    def from_string(cls, s):
        history = [op.strip() for op in s.split(",").strip()]
        return cls(history)

    def filter_operations(self, keyword):
        return list(filter(lambda x: keyword in x, self._history))

    def map_results(self):
        return list(map(lambda x: x[-1], self._history))

    def __str__(self):
        return "\n".join(self._history)


class ScientificCalculator(Calculator):
    def __init__(self, history=None):
        super().__init__(history)

    @property
    def last_result(self):
        if not self._history:
            return None
        result = self._history[-1].split("=")[-1].strip()
        return round(float(result), 2)

    def power(self, base, exp):
        result = base ** exp
        return self._add_to_history(f"{base} ** {exp}", result)

    def sqrt(self, a):
        if not isinstance(a, (int, float)) or a < 0:
            return ValueError
        result = a ** 0.5
        return self._add_to_history(f"{a} ** 0.5", result)

    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        result = 1
        if n == 0 or n == 1:
            result = 1
        for i in range(1, n+1):
            result *= i
        return self._add_to_history(f"{n}!", result)

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def from_history(cls, history):
        return cls(history)

    def __str__(self):
        return "🔬 Научный калькулятор\n" + super().__str__()


calc = ScientificCalculator()
calc.add(10, 5)
calc.mul(3, 7)
calc.power(2, 8)
calc.sqrt(144)
calc.factorial(5)

print(calc)
print(f"\nПоследний результат (округлённый): {calc.last_result}")
print(f"Всего операций: {calc.operation_count}")
print(f"Операции со сложением: {calc.filter_operations('+')}")
print(f"Все результаты: {calc.map_results()}")
print(f"Сумма [1,2,3,4,5] (рекурсивно): {calc.recursive_sum([1, 2, 3, 4, 5])}")
print(f"Число 17 простое? {ScientificCalculator.is_prime(17)}")
