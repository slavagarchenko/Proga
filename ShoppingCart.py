class ShoppingCart:
    def __init__(self, items=None):
        self._items = {}
        if items:
            self.items = items

    @property
    def items(self):
        return self._items.copy()

    @staticmethod
    def is_valid_item(name, data):
        if not isinstance(name, str) or not name.strip():
            return False
        if not isinstance(data, dict) or not "price" in data or not "quantity" in data:
            return False
        if not isinstance(data["price"], (int, float)) or data["price"] <= 0:
            return False
        if not isinstance(data["quantity"], (int, float)) or data["quantity"] <= 0:
            return False
        return True

    @items.setter
    def items(self, new_items):
        if not isinstance(new_items, dict):
            raise TypeError
        for keys, values in new_items.items():
            if not self.is_valid_item(keys, values):
                raise TypeError
        self._items = new_items

    @property
    def total(self):
        return sum(x["price"] * x["quantity"] for x in self._items.values())

    @property
    def item_count(self):
        return sum(x["quantity"] for x in self._items.values())

    def add_item(self, name, price, quantity=1):
        if not self.is_valid_item(name, {"price": price, "quantity": quantity}):
            raise ValueError
        if name in self._items:
            self._items[name]["quantity"] += quantity
        else:
            self._items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name):
        if name in self._items:
            del self._items[name]
        else:
            raise ValueError

    def update_quantity(self, name, quantity):
        if name not in self._items:
            raise ValueError
        if quantity <= 0:
            raise ValueError
        self._items[name]["quantity"] = quantity

    def recursive_total(self, index=0, items_list=None):
        if items_list is None:
            items_list = list(self._items.items())
        if index >= len(items_list):
            return 0
        name, data = items_list[index]
        return data["quantity"] * data["price"] + self.recursive_total(index+1, items_list)

    @classmethod
    def from_list(cls, items_list):
        items = {}
        for name, price, quantity in items_list:
            items[name] = {"price": price, "quantity": quantity}
        return cls(items)

    def filter_expensive(self, min_price):
        return dict(filter(lambda item: item[1]["price"] >= min_price, self._items.items()))

    def map_items(self):
        return list(map(lambda pair: f"{pair[0]} ({pair[1]["price"]} x {pair[2]["quantity"]})", self._items.items()))


cart = ShoppingCart()
cart.add_item("Ноутбук", 50000, 1)
cart.add_item("Мышь", 1500, 2)
cart.add_item("Клавиатура", 3000, 1)

print(cart)
print(f"\nОбщая стоимость (рекурсивно): {cart.recursive_total()}")


def rec(self, coords, index=0, summa=0):
    if index >= len(coords):
        return summa**0.5
    summa += coords[index]**2
    self.rec(coords, index+1, summa)
