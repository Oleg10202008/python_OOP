class Bank:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount} UAH")
        else:
            raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} UAH")
        else:
            raise ValueError("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

def run (Bank):
    var=int(input(" Выберите вариант операцыи\n 1- депозит\n 2- снять деньги\n 3- посмотреть баланс\n 4-история транзакцый "))
    if var == 1:
        Bank.deposit(int(input("введите суму депозита: ")))
    elif var == 2:
        Bank.withdraw(int(input("введите суму которую хотите снять: ")))
    elif var == 3:
        Bank.get_balance()
    elif var == 4:
        Bank.get_transaction_history()
bank1 = Bank()
bank1.run()