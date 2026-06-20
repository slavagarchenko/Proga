class Stack:
    def __init__(self, items=None):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def _push_bottom(self, item):
        if self.is_empty():
            self.items.append(item)
        else:
            top = self.pop()
            self._push_bottom(item)
            self.items.append(top)

    def reverse(self):
        if self.is_empty():
            return None
        temp = self.pop()
        self.reverse()
        self._push_bottom(temp)

    def map_stack(self, func):
        return Stack(list(map(func, self.items)))

    def __add__(self, other):
        if isinstance(other, Stack):
            return Stack(self.items + other.items)
        return TypeError

    def __str__(self):
        return f"Stack: {self.items}"


s = Stack([1, 2, 3, 4])
print(f"Исходный: {s}")
s.reverse()
print(f"Развёрнутый: {s}")

squared = s.map_stack(lambda x: x ** 2)
print(f"Квадраты: {squared}")

s2 = Stack([5, 6])
print(f"Объединённый: {s + s2}")
