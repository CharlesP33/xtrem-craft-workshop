from .currency import Currency


class MissingExchangeRateError(Exception):
    def __init__(self, src: Currency, target: Currency) -> None:
        super().__init__(f'{src.value}->{target.value}')