class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        """Инициализация вектора с координатами x, y, z"""
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Сложение векторов с образованием нового объекта"""
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError(f"Нельзя сложить Vector3D с {type(other)}")

    def __sub__(self, other):
        """Вычитание векторов с образованием нового объекта"""
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError(f"Нельзя вычесть из Vector3D {type(other)}")

    def __iadd__(self, other):
        """Сложение с переопределением текущего вектора (+=)"""
        if isinstance(other, Vector3D):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        raise TypeError(f"Нельзя сложить Vector3D с {type(other)}")

    def __isub__(self, other):
        """Вычитание с переопределением текущего вектора (-=)"""
        if isinstance(other, Vector3D):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        raise TypeError(f"Нельзя вычесть из Vector3D {type(other)}")

    def __str__(self):
        """Строковое представление для пользователя"""
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        """Строковое представление для воссоздания объекта через eval()"""
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def _recursive_length(self, index=0, summa=0):
        coords = [self.x, self.y, self.z]
        if index >= len(coords):
            return summa**0.5
        summa += coords[index]**2
        return self._recursive_length(index+1, summa)


# Пример использования
if __name__ == "__main__":
    # Создаём векторы
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    print("Исходные векторы:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"repr(v1) = {repr(v1)}")

    # Проверка repr
    v3 = eval(repr(v1))
    print(f"Вектор, созданный через eval(repr(v1)): {v3}")

    # Сложение с созданием нового объекта
    v_sum = v1 + v2
    print(f"\nv1 + v2 = {v_sum}")

    # Вычитание с созданием нового объекта
    v_diff = v1 - v2
    print(f"v1 - v2 = {v_diff}")

    # Переопределение текущего вектора
    v1 += v2
    print(f"\nПосле v1 += v2: v1 = {v1}")

    v1 -= v2
    print(f"После v1 -= v2: v1 = {v1}")

    # Длина вектора
    v = Vector3D(3, 4, 0)
    print(f"\nДлина вектора {v} = {v._recursive_length()}")

    v = Vector3D(1, 2, 2)
    print(f"Длина вектора {v} = {v._recursive_length()}")
