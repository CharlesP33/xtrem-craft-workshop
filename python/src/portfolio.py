from python.src.bank import Bank
from python.src.currency import Currency
from python.src.money import Money

class Portfolio:
    
    def __init__(self):
        self._amounts = {}
        self._moneys = []
            
    def add(self, money: Money) -> None:        
        self._moneys.append(money)
     

    def evaluate(self, bank: Bank, currency: Currency) -> float:
        total = Money(0, currency)
        for money in self._moneys:
            total = total + bank.new_convert(money, currency)
        return total.amount