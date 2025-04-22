import pytest

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError

class Portfolio:
    
    def __init__(self):
        self._amounts = {}
    
    def add(self, amount: float, currency: Currency) -> None:
        if currency in self._amounts:
            self._amounts[currency] += amount
        else:
            self._amounts[currency] = amount

    def evaluate(self, bank: Bank, currency: Currency) -> float:
        total = 0
        for c in self._amounts.keys():
            total += bank.convert(self._amounts[c], c, currency)
        return total


class TestPortfolio:
    def test_should_evaluate_portfolio_containing_one_amount_in_same_currency(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        portfolio = Portfolio()
        portfolio.add(5, Currency.USD)

        # act
        evaluation = portfolio.evaluate(bank, Currency.USD)

        # assert
        assert evaluation == 5
        
    def test_should_evaluate_portofilio_in_target_currency(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        portfolio = Portfolio()
        portfolio.add(5, Currency.EUR)

        # act
        evaluation = portfolio.evaluate(bank, Currency.USD)

        # assert
        assert evaluation == 6
        
    def test_should_raise_error_if_change_rate_does_not_exist(self):
        # arrange
        bank = Bank.create(Currency.EUR, Currency.USD, 1.2)

        portfolio = Portfolio()
        portfolio.add(5, Currency.EUR)

        # act
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(bank, Currency.KRW)
            # assert
            assert str(error.value) == "EUR->KRW"