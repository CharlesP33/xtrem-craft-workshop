from typing import Dict

from python.src.money import Money
from .currency import Currency
from .missing_exchange_rate_error import MissingExchangeRateError


class Bank:
    _exchange_rate: Dict[str, float] = {}

    def __init__(self, exchange_rate = {}) -> None:
        self._exchange_rate = exchange_rate

    @staticmethod
    def create(src: Currency, target: Currency, rate: float) -> "Bank":
        bank = Bank({})
        bank.add_echange_rate(src, target, rate)

        return bank
    
    def add_echange_rate(self, src: Currency, target: Currency, rate: float) -> None:
        self._exchange_rate[f'{src.value}->{target.value}'] = rate

    def convert(self, amount: float, src: Currency, target: Currency) -> float:
        if self.can_convert(src, target):
            raise MissingExchangeRateError(src, target)
        
        if not self.is_same_currency(src, target):
            amount = amount * self._exchange_rate[f'{src.value}->{target.value}']
        
        return amount
    
    def new_convert(self, money: Money, target: Currency) -> Money:
        if self.can_convert(money.currency, target):
            raise MissingExchangeRateError(money.currency, target)
        
        if not self.is_same_currency(money.currency, target):
            money.amount = money.amount * self._exchange_rate[f'{money.currency.value}->{target.value}']
        
        return Money(money.amount, target)
    
    def can_convert(self, src: Currency, target: Currency) -> bool:
        return not (self.is_same_currency(src, target) or f'{src.value}->{target.value}' in self._exchange_rate)

    def is_same_currency(self, src: Currency, target: Currency) -> bool:
        return src.value == target.value