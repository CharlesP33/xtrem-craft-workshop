import pytest

from python.src.bank import Bank
from python.tests.bank_builder import BankBuilder
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError
from python.src.money import Money
from python.src.portfolio import Portfolio


class TestPortfolio:
    def test_should_evaluate_portfolio_containing_one_amount_in_same_currency(self):
        # arrange
        bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money = Money(5, Currency.USD)

        portfolio = Portfolio()
        portfolio.add(money)

        # act
        evaluation = portfolio.evaluate(bank, Currency.USD)

        # assert
        assert evaluation == 5
        
    def test_should_evaluate_portofilio_in_target_currency(self):
        # arrange
        bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money = Money(5, Currency.EUR)

        portfolio = Portfolio()
        portfolio.add(money)

        # act
        evaluation = portfolio.evaluate(bank, Currency.USD)

        # assert
        assert evaluation == 6
        
    def test_should_raise_error_if_change_rate_does_not_exist(self):
        # arrange
        bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money = Money(5, Currency.EUR)

        portfolio = Portfolio()
        portfolio.add(money)

        # act
        with pytest.raises(MissingExchangeRateError) as error:
            portfolio.evaluate(bank, Currency.KRW)
            # assert
            assert str(error.value) == "EUR->KRW"