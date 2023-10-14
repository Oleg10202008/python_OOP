import requests
from bs4 import BeautifulSoup
class Bank:
    def __init__(self, name="Oleg", initial_balance=0):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def get_trans(self):
        url = "https://privatbank.ua/all-ways-to-receive-send-an-international-transfer"
        rq = requests.get(url)
        soup = BeautifulSoup(rq.text, "html.parser")
        trans = []
        for ul in soup.find_all("ul", class_="with-bull"):
            rate = ul.text
            trans.append(rate)
        if trans:
            print(trans)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount} UAH")
            print("вам зачисленно ",amount)

        else:
            raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount} UAH")
            print("зписано ", amount)

        else:
            raise ValueError("Invalid withdrawal amount or insufficient funds")

    def get_balance(self):

        print(self.balance)


    def get_transaction_history(self):
        print(self.transaction_history)

    def run (self):
            while True:
                var=int(input(" Выберите вариант операцыи\n 1- депозит\n 2- снять деньги\n 3- посмотреть баланс\n 4-история транзакцый\n 5-список транзакцый "))
                if var == 1:
                    self.deposit(int(input("введите суму депозита: ")))
                elif var == 2:
                    self.withdraw(int(input("введите суму которую хотите снять: ")))
                elif var == 3:
                    self.get_balance()
                elif var == 4:
                    self.get_transaction_history()
                elif var == 5:
                    self.get_trans()

bank1=Bank()
bank1.run()
