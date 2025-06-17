from python.src.currency import Currency
from python.src.money_calculator import MoneyCalculator
from python.src.money import Money

class TestMonetaryOperations:
    def test_add_in_usd_returns_float(self): 
        #Arrange
        m1 = Money(5, Currency.USD)
        m2 = Money(10, Currency.USD)
        #Act
        result = m1 + m2
        #Assert 
        assert result is not None
        assert isinstance(result, Money)

    def test_multiply_currency_by_value_returns_positive_number(self):
        #Arrange
        m1 = Money(10, Currency.EUR)
        value = 2
        #Act
        result = m1 * value
        #Assert
        assert result.amount > 0

    def test_divide_currency_by_value_returns_divided_value(self):
        #Arrange
        m1 = Money(4002, Currency.KRW)
        value = 4
        #Act
        result = m1 / value
        #Assert
        assert result.amount == 1000.5