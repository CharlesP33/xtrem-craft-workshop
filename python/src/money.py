class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add amounts with different currencies")
        return Money(self.amount + other.amount, self.currency)
    
    def multiply(self, value: float):
        return Money(self.amount * value, self.currency)
    
    def __mul__(self, value: float):
        return self.multiply(value)
    
    def __rmul__(self, value: float):
        return self.multiply(value)
    
    def __truediv__(self, value: float):
        if value == 0:
            raise ValueError("Cannot divide by zero")
        return Money(self.amount / value, self.currency)
    
    def __floordiv__(self, value: float):
        if value == 0:
            raise ValueError("Cannot divide by zero")
        return Money(self.amount // value, self.currency)