from functools import reduce


class MyString:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        text = "".join(self.text.lower().split())

        def check(s, left=0, right=None):
            if right is None:
                right = len(s) - 1
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return check(s, left + 1, right - 1)
        return check(text)

    def reverse_words(self):
        words = self.text.split()
        reversed_words = list(map(lambda x: x[::-1], words))
        return MyString(" ".join(reversed_words))

    def count_vowels(self):
        vowels = ["a", "e", "u", "i", "o", "y"]
        return reduce(lambda count, x: count + int(x in vowels), self.text.lower(), 0)

    def __add__(self, other):
        if isinstance(other, MyString):
            return MyString(self.text + other.text)
        raise TypeError

    def __str__(self):
        return f"{self.text}"


s1 = MyString("А роза упала на лапу Азора")
print(f"'{s1}' - палиндром? {s1.is_palindrome()}")

s2 = MyString("Hello World Python")
print(f"Исходная: {s2}")
print(f"С развёрнутыми словами: {s2.reverse_words()}")
print(f"Количество гласных: {s2.count_vowels()}")

s3 = MyString("Hello ") + MyString("World")
print(f"Конкатенация: {s3}")
