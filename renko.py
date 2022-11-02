from dataclasses import dataclass

@dataclass
class RenkoData:
    brick_size: float
    brick_count_to_enter: int
    brick_count_to_exit: int

class RenkoSystem:

    brick_size: float
    renko_bricks : list[int] = []
    last_price : float = None
    max_bricks : int

    def __init__(self, brick_size:float, max_bricks:int = 500):
        self.brick_size = brick_size
        self.max_bricks = max_bricks


    def add_bricks(self, price:float) -> None:

        if self.last_price is None:
            self.last_price = price
            return


        while price > self.last_price + self.brick_size:
            self.last_price += self.brick_size
            self.renko_bricks.append(1)

        while price < self.last_price - self.brick_size:
            self.last_price -= self.brick_size
            self.renko_bricks.append(-1)

    def update_price(self, price:float) -> None:
        self.add_bricks(price)
        self.check_renko_bricks_length()

    def check_renko_bricks_length(self) -> None:
        brick_length = len(self.renko_bricks)
        if brick_length > self.max_bricks:
            self.renko_bricks = self.renko_bricks[-self.max_bricks:]







