from python.src.currency import Currency
from python.src.money_calculator import MoneyCalculator

class TestMonetaryOperations:
    def test_add_in_usd_returns_value(self): 
        #Arrange 
        money_calculator: MoneyCalculator = MoneyCalculator()
        #Act
        result = money_calculator.add(5, Currency.USD, 10)
        #Assert
        assert isinstance(result, float)
        assert result is not None

    def test_multiply_in_euros_returns_positive_number(self):
        #Arrange 
        money_calculator: MoneyCalculator = MoneyCalculator()
        #Act
        result = money_calculator.times(10, Currency.USD, 2)
        #Assert
        assert result > 0

    def test_divide_in_korean_won_returns_float(self):
        #Arrange 
        money_calculator: MoneyCalculator = MoneyCalculator()
        #Act 
        result = money_calculator.divide(4002, Currency.USD, 4) 
        #Assert
        assert result == 1000.5