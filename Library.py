from functools import reduce


class Library:
    def __init__(self, name, books=None):
        self._name = name
        self._books = books if books is not None else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name.strip() or not isinstance(new_name, str):
            raise ValueError
        self._name = new_name

    @property
    def books(self):
        return self._books.copy()

    @staticmethod
    def is_valid_book(book):
        if not isinstance(book, dict):
            return False
        if not book["title"].strip() or book["author"].strip() is None:
            return False
        if not isinstance(book["pages"], int) or book["pages"] <= 0:
            return False
        if not isinstance(book["rating"], (int, float)) or not 0 <= book["rating"] <= 10:
            return False
        return True

    @books.setter
    def books(self, new_books):
        if not isinstance(new_books, list):
            raise TypeError
        for book in new_books:
            if not self.is_valid_book(book):
                raise TypeError
        self._books = new_books

    @property
    def total_pages(self):
        return sum(b["pages"] for b in self._books)

    @property
    def popular_books(self):
        return [b for b in self._books if b["rating"] >= 7]

    @classmethod
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls(data["name"], data["books"])

    def recursive_search_by_author(self, author, index=0, result=None):
        if result is None:
            result = []
        if index >= len(self._books):
            return result
        if author == self._books[index]["author"]:
            result.append(self._books[index])
        return self.recursive_search_by_author(author, index+1, result)

    def recursive_total_pages(self, index=0):
        if index >= len(self._books):
            return 0
        return self._books[index]["pages"] + self.recursive_total_pages(index+1)

    def filter_by_rating(self, min_rating):
        return list(filter(lambda x: x["rating"] >= min_rating,  self._books))

    def map_titles(self):
        return list(map(lambda x: x["title"], self._books))

    def reduce_total_pages(self):
        if not self._books:
            return 0
        return reduce(lambda total, book: book["pages"] + total, self._books, 0)

    def add_book(self, title, author, pages, rating):
        book = {"title": title, "author": author,
                "pages": pages, "rating": rating}
        if not self.is_valid_book(book):
            raise ValueError
        self._books.append(book)

    def __str__(self):
        result = f"📚 {self._name} (книг: {len(self._books)})\n"
        for b in self._books:
            result += f"  - '{b['title']}' {b['author']}, {b['pages']} стр., рейтинг: {b['rating']:.1f}\n"
        return result


print("=" * 60)
print("ПРОВЕРКА КОМПЛЕКСНОГО ЗАДАНИЯ 32")
print("=" * 60)

# 1. Создание библиотеки
lib = Library("Городская библиотека")
lib.add_book("Война и мир", "Толстой", 1225, 9.5)
lib.add_book("Преступление и наказание", "Достоевский", 671, 8.7)
lib.add_book("Анна Каренина", "Толстой", 864, 8.9)
lib.add_book("Мастер и Маргарита", "Булгаков", 480, 9.2)
lib.add_book("Идиот", "Достоевский", 560, 7.8)

print("\n1. Исходная библиотека:")
print(lib)

# 2. Геттеры
print(f"\n2. Геттеры:")
print(f"   Общее количество страниц: {lib.total_pages}")
print(f"   Популярные книги (рейтинг >= 8):")
for b in lib.popular_books:
    print(f"     - {b['title']} ({b['rating']:.1f})")

# 3. Рекурсивный поиск
print("\n3. Рекурсивный поиск по автору:")
tolstoy_books = lib.recursive_search_by_author("Толстой")
print(f"   Книги Толстого: {[b['title'] for b in tolstoy_books]}")
print(
    f"   Общее количество страниц (рекурсивно): {lib.recursive_total_pages()}")

# 4. Функциональное программирование
print("\n4. Функциональное программирование:")
high_rated = lib.filter_by_rating(8.5)
print(f"   Книги с рейтингом >= 8.5: {[b['title'] for b in high_rated]}")
print(f"   Названия всех книг: {lib.map_titles()}")
print(
    f"   Общее количество страниц (через reduce): {lib.reduce_total_pages()}")

# 5. Создание из JSON
print("\n5. Создание из JSON:")
json_str = '{"name": "Домашняя библиотека", "books": [{"title": "1984", "author": "Оруэлл", "pages": 328, "rating": 9.0}]}'
lib2 = Library.from_json(json_str)
print(lib2)

# 6. Проверка валидации
print("\n6. Проверка валидации:")
try:
    lib.add_book("", "Автор", 100, 5)
except ValueError as e:
    print(f"   Ошибка: {e}")
