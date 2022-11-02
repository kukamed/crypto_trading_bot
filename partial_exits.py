from dataclasses import dataclass


@dataclass
class PartialExitsData:
    partial_exits_count: int
    partial_exits_percent: float
    is_last_trailing_stop: bool


class PartialExitsSystem:

    prices_percent: float

    def __init__(self, partial_exits_count: int, partial_exits_percent: float, is_last_trailing_stop: bool,
                 long_or_short: str, starting_price: float):
        self.partial_exits_count = partial_exits_count
        self.partial_exits_percent = partial_exits_percent
        self.is_last_trailing_stop = is_last_trailing_stop
        self.long_or_short = long_or_short
        self.starting_price = starting_price

    def update_prices(self, price: float) -> None:
        self.prices_percent = (price - self.starting_price) / self.starting_price