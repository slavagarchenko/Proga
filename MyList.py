class MyList:
    def __init__(self, data):
        self.data = data

    def flatten(self, lst=None):
        if lst is None:
            lst = self.data
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(self.flatten(item))
            result.append(item)
        return result

    def map_list(self, func):
        new_data = list(map(func, self.data))
        return MyList(new_data)

    def filter_list(self, predicate):
        return MyList(list(filter(predicate, self.data)))

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self.data + other.data)
        raise TypeError

    def __str__(self):
        return f"{self.data}"


ml = MyList([1, [2, 3], [4, [5, 6]], 7])
print(f"Исходный: {ml}")
print(f"Выровненный: {ml.flatten()}")

ml2 = MyList([1, 2, 3, 4, 5, 6])
print(f"Квадраты: {ml2.map_list(lambda x: x**2)}")
print(f"Чётные: {ml2.filter_list(lambda x: x % 2 == 0)}")

ml3 = MyList([10, 20]) + MyList([30, 40])
print(f"Объединённый: {ml3}")
