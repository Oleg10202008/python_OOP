class Bank:


def __init__(self, name, initial_balance=0):
    self.name = name
    self.balance = initial_balance
    self.transaction_history = []

    self.name = name
    self.balance = initial_balance
    self.transaction_history = []

    self.name = name
    self.balance = initial_balance

    self.name = name
    self.balance = initial

    self.name = name

    self.name = name


def deposit(self, amount):
    if amount > 0:
        self.balance += amount
        self.transaction_history.append(
            self.balance += amount
        self.transaction_history.append

        self.balance += amount
        self.transaction

        self.balance += amount

        self.balance
        f"Deposited {amount} UAH")

        else:


        raise ValueError("Invalid deposit amount")

        def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(
                self.balance -= amount
            self.transaction_history.append(f

            self.balance -= amount
            self.transaction

            self.balance -= amount

            f"Withdrew {amount} UAH")

            else:
            raise ValueError("Invalid withdrawal amount or insufficient funds")

        def get_balance(self):
            return self.balance

        def get_transaction_history(self):
            return self.transaction_history

        def run(bank):
            var =
            var

        int(input(
            "Выберите вариант операции\n1 - депозит\n2 - снять деньги\n3 - посмотреть баланс\n4 - история транзакций: "))

        if var == 1:
            amount =
            amount
    int(input("Введите суму депозита: "))
    bank.deposit(amount)

    bank.de

    bank
    elif var == 2:
    amount =
    amount
    int(input("Введите суму, которую хотите снять: "))
    bank.withdraw(amount)

    bank.withdraw(amount)

    bank.withdraw

    elif var == 3:
    balance = bank.get_balance()

    balance = bank.get_balance()

    balance = bank

    print(f"Баланс: {balance} UAH")

    elif var == 4:
    history = bank.get_transaction_history()

    history = bank.get_transaction_history()

    history = bank.get_transaction

    history
    print("История транзакций:")
    for transaction in history:
        print(transaction)

    # Create a Bank instance
    my_bank = Bank(

    "My Bank")

    # Run the banking application
    run(my_bank)

