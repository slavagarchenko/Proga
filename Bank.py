from functools import reduce
import datetime


class Bank:
    def __init__(self, name, clients=None):
        self._name = name
        self._clients = clients if clients is not None else {}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name.strip():
            raise ValueError
        self._name = new_name

    @staticmethod
    def is_valid_account(account):
        if not isinstance(account, str) or len(account) != 6 or not isinstance(int(account), int):
            return False
        return True

    @staticmethod
    def is_valid_client(client):
        if not isinstance(client, dict):
            return False
        if "name" not in client or "balance" not in client or "transations" not in client:
            return False
        if not isinstance(client["name"], str) or isinstance(client["balance"], (int, float)) or isinstance(client["transactions"], list):
            return False
        if not "type" in client["transactions"] or not "amout" in client["transactions"] or not "data" in client["transactions"]:
            return False
        if not isinstance(client["transactions"]["amount"], (int, float)) or not isinstance(client["transactions"]["data"], str):
            return False
        if client["balance"] <= 0 or client["transactions"]["amount"] <= 0:
            return False
        return True

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, new_clients):
        if not isinstance(new_clients, dict):
            raise TypeError
        if not self.is_valid_account(new_clients.keys()) or not self.is_valid_client(new_clients.values()):
            raise TypeError
        self._clients = new_clients

    @property
    def total_balance(self):
        return sum(b["balance"] for b in self._clients.values())

    @property
    def active_clients(self):
        return list(filter(lambda b: b["balance"] > 0, self._clients.values()))

    @classmethod
    def from_csv(cls, csv_data):
        lines = csv_data.strip().split("\n")
        name = lines[0].strip()
        clients = {}
        for line in lines[1:]:
            parts = line.split(",")
            account = parts[0].strip()
            name_client = parts[1].strip()
            balance = float(parts[2]) if len(parts) > 2 else 0
            clients[account] = {"name": name_client,
                                "balance": balance, "transactions": []}
        return cls(name, clients)

    def recursive_find_client(self, account, accounts=None, index=0):
        if accounts is None:
            accounts = list(self._clients.keys())
        if index >= len(accounts):
            return None
        if account == accounts[index]:
            return {account: self._clients[account]}
        return self.recursive_find_client(account, accounts, index+1)

    def recursive_total_balance(self, accounts=None, index=0):
        if accounts is None:
            accounts = list(self._clients.values())
        if index >= len(accounts):
            return 0
        return accounts[index]["balance"] + self.recursive_total_balance(accounts, index+1)

    def filter_rich_clients(self, min_balance):
        return dict(filter(lambda pair: pair[1]["balance"] >= min_balance, self._clients.items()))

    def map_client_names(self):
        return list(map(lambda c: c["name"], self._clients.values()))

    def reduce_total_balance(self):
        return reduce(lambda total, b: total + b["balance"], self._clients.values(), 0)

    def apply_interest(self, rate_percent):
        """Применяет проценты к балансу всех клиентов"""
        if rate_percent < 0:
            raise ValueError("Процентная ставка должна быть положительной")

        def apply_to_client(pair):
            account, client_data = pair
            new_balance = client_data['balance'] * (1 + rate_percent / 100)
            new_balance = round(new_balance, 2)
            new_transactions = client_data['transactions'].copy()
            new_transactions.append({
                'type': 'начисление процентов',
                'amount': round(new_balance - client_data['balance'], 2),
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            })
            return (account, {
                'name': client_data['name'],
                'balance': new_balance,
                'transactions': new_transactions
            })

        new_clients = dict(map(apply_to_client, self._clients.items()))
        return Bank(f"{self._name} (с процентами {rate_percent}%)", new_clients)

    # ============ ДОПОЛНИТЕЛЬНЫЕ МЕТОДЫ ============
    def _generate_account(self):
        """Генерирует уникальный номер счёта"""
        import random
        while True:
            account = ''.join(str(random.randint(0, 9)) for _ in range(6))
            if account not in self._clients:
                return account

    def add_client(self, name, initial_balance=0):
        """Добавляет нового клиента"""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя должно быть непустой строкой")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        account = self._generate_account()
        self._clients[account] = {
            'name': name,
            'balance': initial_balance,
            'transactions': []
        }
        if initial_balance > 0:
            self._clients[account]['transactions'].append({
                'type': 'пополнение',
                'amount': initial_balance,
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
            })
        return account

    def make_transaction(self, account, amount, transaction_type):
        """Выполняет транзакцию"""
        if account not in self._clients:
            raise ValueError(f"Счёт {account} не найден")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if transaction_type not in ['пополнение', 'снятие']:
            raise ValueError(
                "Тип транзакции должен быть 'пополнение' или 'снятие'")

        client = self._clients[account]
        if transaction_type == 'снятие' and client['balance'] < amount:
            raise ValueError("Недостаточно средств")

        if transaction_type == 'пополнение':
            client['balance'] += amount
        else:
            client['balance'] -= amount

        client['transactions'].append({
            'type': transaction_type,
            'amount': amount,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        })

    def get_transaction_history(self, account):
        """Возвращает историю транзакций клиента"""
        if account not in self._clients:
            raise ValueError(f"Счёт {account} не найден")
        return self._clients[account]['transactions']

    def __str__(self):
        result = f"🏦 {self._name} (клиентов: {len(self._clients)}, суммарный баланс: {self.total_balance:.2f} руб.)\n"
        for account, data in sorted(self._clients.items()):
            result += f"  - {account}: {data['name']}, баланс: {data['balance']:.2f} руб., транзакций: {len(data['transactions'])}\n"
        return result


# ============ ПРОВЕРКА ============
print("=" * 70)
print("ПРОВЕРКА КОМПЛЕКСНОГО ЗАДАНИЯ 34")
print("=" * 70)

# 1. Создание банка
bank = Bank("Центральный Банк")

# 2. Добавление клиентов
acc1 = bank.add_client("Иван Петров", 5000)
acc2 = bank.add_client("Мария Сидорова", 10000)
acc3 = bank.add_client("Алексей Смирнов", 3000)

print("\n1. Созданный банк:")
print(bank)

# 3. Выполнение транзакций
print("\n2. Выполнение транзакций:")
bank.make_transaction(acc1, 1500, 'пополнение')
bank.make_transaction(acc2, 2000, 'снятие')
bank.make_transaction(acc3, 500, 'пополнение')

print("После транзакций:")
print(bank)

# 4. История транзакций
print("\n3. История транзакций Ивана:")
for t in bank.get_transaction_history(acc1):
    print(f"   {t['date']}: {t['type']} на {t['amount']:.2f} руб.")

# 5. Геттеры
print(f"\n4. Геттеры:")
print(f"   Суммарный баланс: {bank.total_balance:.2f} руб.")
print(f"   Активные клиенты: {len(bank.active_clients)}")

# 6. Рекурсивный поиск
print("\n5. Рекурсивный поиск:")
found = bank.recursive_find_client(acc2)
print(f"   Найден клиент: {found}")
print(
    f"   Суммарный баланс (рекурсивно): {bank.recursive_total_balance():.2f} руб.")

# 7. Функциональное программирование
print("\n6. Функциональное программирование:")
rich = bank.filter_rich_clients(5000)
print(f"   Клиенты с балансом >= 5000: {list(rich.keys())}")
print(f"   Имена клиентов: {bank.map_client_names()}")
print(
    f"   Суммарный баланс (через reduce): {bank.reduce_total_balance():.2f} руб.")

# 8. Применение процентов
print("\n7. Применение процентов 5%:")
bank_with_interest = bank.apply_interest(5)
print(bank_with_interest)

# 9. Создание из CSV
print("\n8. Создание из CSV:")
csv_data = """Региональный Банк
111111,Олег Новиков,2000
222222,Елена Кузнецова,3500
333333,Дмитрий Васильев,1500"""
bank2 = Bank.from_csv(csv_data)
print(bank2)
