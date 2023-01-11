# wallet.py

"""
velice jednoduchá třída reprezentující bankovní účet

důležité jsou spíše testy v souboru test_05_bankaccount - ukázka fixtures

"""

class InsufficientAmount(Exception):
    pass


class BankAccount(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount