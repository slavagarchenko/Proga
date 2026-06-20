class Employee:
    def __init__(self, name, salary, subordinates=None):
        self.name = name
        self.salary = salary
        if not subordinates:
            self.subordinates = []
        self.subordinates = subordinates

    def total_salary(self):
        total = self.salary
        for emp in self.subordinates:
            total += emp.total_salary()
        return total

    def filter_by_salary(self, threshold):
        result = []
        if self.salary > threshold:
            result.append(self)
        for emp in self.subordinates:
            result.extend(emp.filter_by_salary(threshold))
        return result

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self.salary < other.salary
        raise TypeError

    def __str__(self):
        return f"Employee {self.name}: {self.salary}"


ceo = Employee("Директор", 100000, [
    Employee("Менеджер1", 60000, [
        Employee("Разработчик1", 50000),
        Employee("Разработчик2", 45000)
    ]),
    Employee("Менеджер2", 55000, [
        Employee("Тестировщик", 40000)
    ])
])

print(f"Общая зарплата всех сотрудников: {ceo.total_salary()} руб.")
print("\nСотрудники с зарплатой >= 50000:")
for emp in ceo.filter_by_salary(50000):
    print(emp)
