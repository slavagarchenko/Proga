class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def compound_interest(self, years, rate):
        if years == 0:
            return self.balance
        if years > 0:
            self.balance = self.balance * (1 + rate)
            return self.compound_interest(years - 1, rate)
        return self.balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.owner} & {other.owner}", self.balance + other.balance)
        raise TypeError

    def __str__(self):
        return f"BankAccount {self.owner}: {self.balance}"


acc = BankAccount("Анна", 1000)
acc.deposit(500)
print(acc)
print(f"Через 3 года под 10%: {acc.compound_interest(3, 0.1):.2f}")
acc2 = BankAccount("Пётр", 2000)
acc3 = acc + acc2
print(acc3)
