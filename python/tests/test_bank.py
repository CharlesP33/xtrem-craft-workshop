import pytest
import re

from python.src.bank import Bank
from python.tests.bank_builder import BankBuilder
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError
from python.src.money import Money


class TestConvertCurrency:
    def test_convert_currencies_when_exchange_rate_exists_returns_convert_value(self):
        #Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(10, Currency.EUR)
        #Act
        result = bank.new_convert(money, Currency.USD)
        #Assert
        assert type(result) == Money
        assert result.amount == 12
        assert result.currency == Currency.USD

    def test_convert_same_currencies_returns_same_value(self):
        #Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(10, Currency.EUR)
        #Act
        result = bank.new_convert(money, Currency.EUR)
        #Assert
        assert type(result) == Money
        assert result.amount == 10
        assert result.currency == Currency.EUR

    def test_convert_with_missing_exchange_rate_throws_exception(self):
        #Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(10, Currency.EUR)
        #Act
        with pytest.raises(MissingExchangeRateError) as error:
            bank.new_convert(money, Currency.KRW)
            #Assert
            assert str(error.value) == "EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_convert_value(self):
        #Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(10, Currency.EUR)
        #Act
        bank.add_echange_rate(Currency.EUR, Currency.USD, 1.3)
        #Assert
        assert 13 == bank.new_convert(money, Currency.USD).amount

    ####
    def test_convert_to_same_currency_without_exchange_rate(self):
        # Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).build()
        money: Money = Money(10, Currency.EUR)
        # Act
        result = bank.new_convert(money, Currency.EUR)
        # Assert
        assert result.amount == 10
        assert result.currency == Currency.EUR

    def test_convert_to_other_currency_with_exchange_rate(self):
        # Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(10, Currency.EUR)
        # Act
        result = bank.new_convert(money, Currency.USD)
        # Assert
        assert result.amount == 12
        assert result.currency == Currency.USD

    def test_convert_non_pivot_currency_to_pivot_currency(self):
        # Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1.2, Currency.USD).build()
        money: Money = Money(12, Currency.USD)
        # Act
        result = bank.new_convert(money, Currency.EUR)
        # Assert
        assert result.amount == 10
        assert result.currency == Currency.EUR

    def test_convert_non_pivot_to_other_non_pivot_currency(self):
        # Arrange
        bank: Bank = (
            BankBuilder.aBank()
            .with_pivot_currency(Currency.EUR)
            .with_exchange_rate(1.2, Currency.USD)
            .with_exchange_rate(1120, Currency.KRW)
            .build()
        )
        money: Money = Money(12, Currency.USD)
        # Act
        eur = bank.new_convert(money, Currency.EUR) 
        krw = bank.new_convert(eur, Currency.KRW)    
        # Assert
        assert krw.amount == 11200
        assert krw.currency == Currency.KRW

    def test_convert_non_pivot_to_same_currency(self):
        # Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).build()
        money: Money = Money(12, Currency.KRW)
        # Act
        result = bank.new_convert(money, Currency.KRW)
        # Assert
        assert result.amount == 12
        assert result.currency == Currency.KRW

    def test_convert_non_pivot_to_unknown_currency_raises(self):
        # Arrange
        bank: Bank = BankBuilder.aBank().with_pivot_currency(Currency.EUR).with_exchange_rate(1344, Currency.KRW).build()
        money: Money = Money(1, Currency.KRW)
        # Act / Assert
        with pytest.raises(MissingExchangeRateError) as error:
            bank.new_convert(money, Currency.USD)
        assert str(error.value) == "EUR->USD"
