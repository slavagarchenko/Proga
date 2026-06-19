from functools import reduce


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        total = reduce(lambda x, y: x + y, self.grades, 0)
        return total/len(self.grades) if self.grades else 0

    def max_grade(self):
        def rec_max(grades, index=0, current_max=0):
            if index >= len(grades):
                return current_max
            if grades[index] > current_max:
                current_max = grades[index]
            return rec_max(grades, index + 1, current_max)
        return rec_max(self.grades) if self.grades else None

    def __str__(self):
        return "Студент: {self.name}, {self.grades}"

    def __repr__(self):
        return f"Student({self.name}, {self.grades})"
