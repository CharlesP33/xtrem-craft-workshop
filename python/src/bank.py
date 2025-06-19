from typing import Dict

from python.src.money import Money
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[Currency, float] = {}
    _pivot : Currency = None

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(src: Currency, target: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.add_echange_rate(target, rate)
        bank.set_pivot(src)

        return bank
    
    def add_echange_rate(self, target: Currency, rate: float) -> None:
        self._exchange_rate[target] = rate
    
    def set_pivot(self, pivot: Currency) -> None:
        self._pivot = pivot

    # def convert(self, amount: float, src: Currency, target: Currency) -> float:
    #     if self.can_convert(src, target):
    #         raise MissingExchangeRateError(src, target)
        
    #     if not self.is_same_currency(src, target):
    #         amount = amount * self._exchange_rate[f'{src.value}->{target.value}']
        
    #     return amount
    
    def new_convert(self, money: Money, target: Currency) -> Money:
        if self._pivot is None:
            raise ValueError("Pivot currency is not set in the bank")
        if not self.can_convert(money.currency, target):
            raise MissingExchangeRateError(money.currency, target)
        
        if not self.is_same_currency(money.currency, target):
            if money.currency == self._pivot: # src is pivot
                money.amount = money.amount * self._exchange_rate[target]
            elif target == self._pivot: # target is pivot
                money.amount = money.amount / self._exchange_rate[money.currency]
            else: # convert src to pivot then pivot to target
                money.amount = money.amount / self._exchange_rate[money.currency]
                money.amount = money.amount * self._exchange_rate[target]

        return Money(money.amount, target)
    
    def can_convert(self, src: Currency, target: Currency) -> bool:
        return self.is_same_currency(src, target) or (src in self._exchange_rate and target == self._pivot) or (src == self._pivot and target in self._exchange_rate)or (src in self._exchange_rate and target in self._exchange_rate)

    def is_same_currency(self, src: Currency, target: Currency) -> bool:
        return src.value == target.value