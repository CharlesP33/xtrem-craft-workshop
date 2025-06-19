from ..src.currency import Currency
from python.src.bank import Bank

class BankBuilder:
    pivot_currency: Currency = None
    exchange_rates: dict[Currency, float] = {}

    @staticmethod
    def aBank() -> "BankBuilder":
        return BankBuilder()
    
    def with_pivot_currency(self, pivot_currency: Currency):
        self.pivot_currency = pivot_currency
        return self
    
    def with_exchange_rate(self, rate: float, currency: Currency):
        self.exchange_rates[currency] = rate
        return self

    def build(self):
        currency = list(self.exchange_rates.keys())[0]
        bank = Bank.create(self.pivot_currency, currency, self.exchange_rates[currency])
        for cur, rate in self.exchange_rates.items():
            if (cur != currency and isinstance(cur, Currency)):
                bank.add_echange_rate(cur, rate)
        return bank