from python.src.currency import Currency
from python.src.money_calculator import MoneyCalculator

class TestMonetaryOperations:
    def test_add_in_usd_returns_float(self): 
        #Arrange
        
        #Act
        result = MoneyCalculator.add(5, Currency.USD, 10)
        #Assert 
        assert result is not None
        assert isinstance(result, float)

    def test_multiply_currency_by_value_returns_positive_number(self):
        #Arrange
        
        #Act
        result = MoneyCalculator.times(10, Currency.EUR, 2)
        #Assert
        assert result > 0

    def test_divide_currency_by_value_returns_divided_value(self):
        #Arrange
        
        #Act
        result = MoneyCalculator.divide(4002, Currency.KRW, 4)
        #Assert
        assert result == 1000.5