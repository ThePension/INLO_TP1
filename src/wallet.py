"""Module that lets you manipulate a wallet"""


class InsufficientAmount(Exception):
    """Exception triggered when you try to spend more money than a wallet has"""

    pass


class Wallet(object):
    """Wallet class that lets your create a Wallet and add or spend money"""

    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        self.deferred_balance = 0

    def spend_cash(self, amount, deferred=False):
        """Removes the specified amount of money from the current Wallet object"""
        if self.balance - self.deferred_balance < amount:
            raise InsufficientAmount(f"Not enough available to spend {amount}")
        if deferred:
            self.deferred_balance += amount
        else:
            self.balance -= amount

    def add_cash(self, amount):
        """Adds the specified amount of money to the current Wallet object"""
        self.balance += amount

    def transfer(self, wallet, amount):
        """Transfers a certain amount from the current wallet object to another one"""
        self.spend_cash(amount)
        wallet.add_cash(amount)

    def pay_deferred_payments(self):
        """Makes deferred payments effective"""
        self.spend_cash(self.deferred_balance)
