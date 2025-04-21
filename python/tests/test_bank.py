import pytest
import re

from python.src.bank import Bank
from python.src.currency import Currency
from python.src.missing_exchange_rate_error import MissingExchangeRateError


class TestConvertCurrency:
    def test_convert_euro_to_usd_returns_float(self):
        #Arrange
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #Act
        result = bank.convert(10, Currency.EUR, Currency.USD)
        #Assert
        assert result == 12

    def test_convert_euro_to_usd_returns_same_value(self):
        #Arrange
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #Act
        result = bank.convert(10, Currency.EUR, Currency.EUR)
        #Assert
        assert result == 10

    def test_convert_with_missing_exchange_rate_throws_exception(self):
        #Arrange
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #Act
        with pytest.raises(MissingExchangeRateError) as error:
            bank.convert(10, Currency.EUR, Currency.KRW)
        #Assert
        assert str(error.value) == "EUR->KRW"

    def test_convert_with_different_exchange_rate_returns_different_floats(self):
        #Arrange
        bank: Bank = Bank.create(Currency.EUR, Currency.USD, 1.2)
        #Act
        result1 = bank.convert(10, Currency.EUR, Currency.USD)
        bank.add_echange_rate(Currency.EUR, Currency.USD, 1.3)
        result2 = bank.convert(10, Currency.EUR, Currency.USD)
        #Assert
        assert result1 == 12
        assert result2 == 13