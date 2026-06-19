class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pager = pages

    @staticmethod
    def recursive_search(books, title, index=0):
        if title == books[index].title:
            return books[index]
        if index >= len(books):
            return None
        return Book.recusive_search(books, title, index + 1)

    def __lt__(self, other):
        return self.pages < other.pages

    @classmethod
    def filter_books_by_author(books, author):
        return list(filter(lambda x: x.author == author, books))

    def __str__(self):
        return f"{self.title}, {self.author}, {self.pages}"
