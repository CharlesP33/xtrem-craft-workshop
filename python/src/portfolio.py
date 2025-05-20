from python.src.bank import Bank
from python.src.currency import Currency
from python.src.money import Money

class Portfolio:
    
    def __init__(self):
        self._amounts = {}
    
    def add(self, amount: float, currency: Currency) -> None:
        if currency in self._amounts:
            self._amounts[currency] += amount
        else:
            self._amounts[currency] = amount
            
    def new_add(self, money: Money) -> None:
        if money.currency in self._amounts:
            self._amounts[money.currency] += money.amount
        else:
            self._amounts[money.currency] = money.amount

    def evaluate(self, bank: Bank, currency: Currency) -> float:
        total = 0
        for c in self._amounts.keys():
            total += bank.new_convert(Money(self._amounts[c], c), currency).amount
        return total