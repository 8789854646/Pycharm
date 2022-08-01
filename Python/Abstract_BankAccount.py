from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        raise Exception
    @abstractmethod
    def withdraw(self, amount):
        raise Exception
    @abstractmethod
    def funds_transfer(self, to_account, amount):
        raise Exception
    @abstractmethod
    def statement(self):
        raise Exception

class WorldBank(BankAccount):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction = []
        self.transaction.append(f"Intial deposit:{balance}")
    def deposit(self, amount):
        self.balance+= amount
        self.transaction.append(f"Amount deposited:{amount}")
    def withdraw(self, amount):
        if amount>self.balance:
            raise Exception("Insuficent Funds")
        self.balance-= amount
        self.transaction.append(f"Amount withdrawn:{amount}")
    def funds_transfer(self,to_account, amount):
        if amount>self.balance:
            raise Exception("Insufficient funds")
        to_account.deposit(amount)
        self.balance-= amount
    def statement(self):
        for item in self.transaction:
            print(item)
        print(f"Total balance:{self.balance}")

sbi = WorldBank("India",2000)
boi = WorldBank("Nepal",2000)
