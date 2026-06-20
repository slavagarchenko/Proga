from functools import reduce


class University:
    def __init__(self, name, students=None):
        self._name = name
        self._students = students if students is not None else []

    @property
    def name(self):
        return self._name

    @property
    def students(self):
        return self._students

    @name.setter
    def name(self, value):
        if not value.strip() or not isinstance(value, str):
            raise ValueError
        self._name = value

    @students.setter
    def students(self, value):
        if not all(self.is_valid_student(s) for s in value):
            raise ValueError
        self._students = list(value)

    @property
    def average_gpa(self):
        if not self._students:
            return 0
        all_grades = [g for s in self._students for g in s["grades"]]
        return sum(all_grades)/len(all_grades) if all_grades else 0

    @property
    def student_count(self):
        return len(self._students)

    @staticmethod
    def is_valid_student(student):
        if not isinstance(student, dict):
            return False
        if "name" not in student or "grades" not in student:
            return False
        if not isinstance(student["name"], str) or not isinstance(student["grades"], list):
            return False
        if not student["name"].strip():
            return False
        correct_grades = [1, 2, 3, 4, 5]
        return all(isinstance(g, int) and g in correct_grades for g in student["grades"])

    @classmethod
    def from_csv(cls, csv_data):
        lines = csv_data.strip().split("\n")
        name = lines[0].strip()
        students = []
        for line in lines[1:]:
            if line.strip():
                parts = line.split(",")
                student_name = parts[0].strip()
                grades = [int(g.strip()) for g in parts[1:] if g.strip()]
                students.append({"name": student_name, "grades": grades})
        return cls(name, students)

    def recursive_find_student(self, name, index=0):
        if index >= len(self._students):
            return None
        if name == self._students[index]["name"]:
            return self._students[index]
        return self.recursive_find_student(name, index+1)

    def recursive_total_grades(self, index=0):
        if index >= len(self._students):
            return 0
        return len(self._students[index]["grades"]) + self.recursive_total_grades(index+1)

    def filter_students(self, min_grade):
        return list(filter(lambda x: all(g >= min_grade for g in x["grades"]), self._students))

    def map_students(self):
        return list(map(lambda x: x["name"].upper(), self._students))

    def reduce_average(self):
        if not self._students:
            return 0
        all_grades = [g for s in self._students for g in s["grades"]]
        if not all_grades:
            return 0
        total = reduce(lambda x, y: x + y, all_grades)
        return total / len(all_grades)

    def add_student(self, name, grades):
        student = {'name': name, 'grades': grades}
        if not self.is_valid_student(student):
            raise ValueError("Некорректные данные студента")
        self._students.append(student)

    def __str__(self):
        return f"University: {self._name}, Count = {self.student_count}"


# 1. Создание университета
uni = University("МГУ")
uni.add_student("Иван", [4, 5, 3, 5])
uni.add_student("Мария", [5, 5, 4, 5])
uni.add_student("Петр", [3, 3, 4, 3])
uni.add_student("Анна", [5, 5, 5, 5])

print("\n1. Исходный университет:")
print(uni)

# 2. Геттеры
print(f"\n2. Геттеры:")
print(f"   Средний GPA всех студентов: {uni.average_gpa:.2f}")
print(f"   Количество студентов: {uni.student_count}")

# 3. Рекурсивный поиск
print("\n3. Рекурсивный поиск:")
found = uni.recursive_find_student("Мария")
print(f"   Найден студент: {found}")
print(
    f"   Общее количество оценок (рекурсивно): {uni.recursive_total_grades()}")

# 4. Функциональное программирование
print("\n4. Функциональное программирование:")
good_students = uni.filter_students(4)
print(f"   Студенты с оценками >= 4: {[s['name'] for s in good_students]}")
print(f"   Имена в верхнем регистре: {uni.map_students()}")
print(f"   Средний балл (через reduce): {uni.reduce_average():.2f}")

# 5. Создание из CSV
print("\n5. Создание из CSV:")
csv_data = """ВШЭ
Алексей,5,4,5
Ольга,4,4,5
Дмитрий,3,4,3"""
uni2 = University.from_csv(csv_data)
print(uni2)

# 6. Сеттер с валидацией
print("\n6. Проверка валидации:")
try:
    uni.name = ""
except ValueError as e:
    print(f"   Ошибка: {e}")
