from functools import reduce


class Warehouse:
    def __init__(self, name, items=None):
        self._name = name
        self._items = items if items is not None else {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError
        self._name = new_name

    @staticmethod
    def is_valid_item(name, item_data):
        if not isinstance(name, str) or not name.strip():
            return False
        if not isinstance(item_data, dict):
            return False
        if "price" not in item_data or "quantity" not in item_data:
            return False
        if not isinstance(item_data["price"], (int, float)) or item_data["price"] <= 0:
            return False
        if not isinstance(item_data["quantity"], int) or item_data["quantity"] <= 0:
            return False
        return True

    @property
    def items(self):
        return self._items.copy()

    @items.setter
    def items(self, new_items):
        if not isinstance(new_items, dict):
            raise TypeError
        for name, item_data in new_items.items():
            if not self.is_valid_item(name, item_data):
                raise ValueError
        self._items = dict(new_items)

    @property
    def total_value(self):
        return sum([i["price"] * i["quantity"] for i in self._items.values()])

    @property
    def item_count(self):
        return sum([i["quantity"] for i in self._items.values()])

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data.get("items", {}))

    def recursive_find_item(self, name, keys=None, index=0):
        if keys is None:
            keys = list(self._items.keys())
        if index >= len(keys):
            return None

        if name == keys[index]:
            return {keys[index]: self._items[keys[index]]}
        return self.recursive_find_item(name, keys, index+1)

    def recursive_total_value(self, keys=None, index=0):
        if keys is None:
            keys = list(self._items.keys())
        if index >= len(keys):
            return 0
        item = self._items[keys[index]]
        return (item["price"] * item["quantity"]) + self.recursive_total_value(keys, index+1)

    def filter_items(self, min_price):
        return dict(filter(lambda item: item[1]["price"] >= min_price, self._items.items()))

    def map_items(self):
        return list(map(lambda i: i.upper(), self._items.keys()))

    def reduce_total_value(self):
        if not self._items:
            return 0
        return reduce(lambda total, i: total + (i["price"] * i["quantity"]), self._items.values(), 0)

    def apply_discount(self, discount):
        return dict(map(lambda item: (item[0], item[1]["price"] * (1 - discount/100)),
                    self._items.items()))

    def add_item(self, name, price, quantity):
        """Добавляет новый товар"""
        item_data = {'price': price, 'quantity': quantity}
        if not self.is_valid_item(name, item_data):
            raise ValueError("Некорректные данные товара")
        self._items[name] = item_data

    def __str__(self):
        result = f"🏭 {self._name} (всего товаров: {self.item_count}, стоимость: {self.total_value:.2f} руб.)\n"
        for name, data in sorted(self._items.items()):
            result += f"  - {name}: {data['quantity']} шт. x {data['price']:.2f} руб. = {data['price'] * data['quantity']:.2f} руб.\n"
        return result


print("=" * 60)
print("ПРОВЕРКА КОМПЛЕКСНОГО ЗАДАНИЯ 33")
print("=" * 60)

# 1. Создание склада
warehouse = Warehouse("Склад №1")
warehouse.add_item("Ноутбук", 50000, 10)
warehouse.add_item("Мышь", 1500, 50)
warehouse.add_item("Клавиатура", 3000, 30)
warehouse.add_item("Монитор", 15000, 15)

print("\n1. Исходный склад:")
print(warehouse)

# 2. Геттеры
print(f"\n2. Геттеры:")
print(f"   Общая стоимость всех товаров: {warehouse.total_value:.2f} руб.")
print(f"   Общее количество товаров: {warehouse.item_count}")

# 3. Рекурсивный поиск
print("\n3. Рекурсивный поиск:")
found = warehouse.recursive_find_item("Мышь")
print(f"   Найден товар: {found}")
print(
    f"   Общая стоимость (рекурсивно): {warehouse.recursive_total_value():.2f} руб.")

# 4. Функциональное программирование
print("\n4. Функциональное программирование:")
expensive = warehouse.filter_items(10000)
print(f"   Товары дороже 10000 руб.: {list(expensive.keys())}")
print(f"   Названия в верхнем регистре: {warehouse.map_items()}")
print(
    f"   Общая стоимость (через reduce): {warehouse.reduce_total_value():.2f} руб.")

# 5. Применение скидки
print("\n5. Применение скидки 10%:")
discounted = warehouse.apply_discount(10)
print(discounted)

# 6. Создание из словаря
print("\n6. Создание из словаря:")
data = {
    'name': 'Мини-склад',
    'items': {
        'USB-флешка': {'price': 800, 'quantity': 20},
        'Внешний диск': {'price': 5000, 'quantity': 5}
    }
}
warehouse2 = Warehouse.from_dict(data)
print(warehouse2)

# 7. Проверка валидации
print("\n7. Проверка валидации:")
try:
    warehouse.add_item("", 100, 5)
except ValueError as e:
    print(f"   Ошибка: {e}")

try:
    warehouse.add_item("Телефон", -1000, 5)
except ValueError as e:
    print(f"   Ошибка: {e}")
