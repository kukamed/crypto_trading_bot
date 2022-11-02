from exchange import Binance
import time
from datetime import timedelta
from renko import RenkoSystem
from partial_exits import PartialExitsSystem
from zscore import get_zscore_value
from strategies import *
from zscore_renko_strategy import load_zscore_renko_strategies

# constants
GET_PRICE_PERIOD = 1

# Initializations
exchange = Binance()
strategies: list[StrategyData] = Strategies(load_zscore_renko_strategies).strategies
renko_bricks: list[RenkoSystem] = []
partial_exits: list[PartialExitsSystem] = []

for strategy in strategies:
    renko_bricks.append(RenkoSystem(strategy.brick_size))


# Loops
def strategies_loop():
    for strategy in strategies:
        price_time_series = exchange.get_prices_time_series(strategy.symbol, strategy.interval)
        zscore_value = get_zscore_value(values=price_time_series, zscore_length=strategy.zscore_length)

        if strategy.symbol in partial_exits:
            continue

        if zscore_value > strategy.zscore_threshold:
            partial_exits[strategy.symbol] = PartialExitsSystem(strategy.partial_exit_percent, strategy.partial_exit_count,
                                                                strategy.long_short, price_time_series[-1])

def exits_loop(price: float):

    for partial_exit in partial_exits():
        partial_exit.update_price(price)


# Main loop
# while True:
for _ in range(1):
    initial_time = time.time()


    strategies_loop()

    # Check if sleep is needed
    sleep_time = GET_PRICE_PERIOD - (time.time() - initial_time)
    if sleep_time > 0:
        time.sleep(sleep_time)





# close_prices = exchange.get_close_prices('BTCUSDT', '1m', 500)
# zscore = technical_analysis.zscore(values=close_prices, zscore_length=zscore_length)




# symbol_renko_bricks = {}
# # renko_params = {'symbol': 'BTCUSDT', brick_size' : 5, 'max_bricks' : 500, 'bricks_to_exit' : 3}
# for symbol in prices:
#     brick_size = prices[symbol] * 0.0005
#     print(f'Brick size for {symbol} is {brick_size}')
#     symbol_renko_bricks[symbol] = Renko(brick_size, 500)
# # renko_bricks = Renko(renko_params['brick_size'], renko_params['max_bricks'])
# #
# while True:
#     initial_time = time.time()
#
#     prices = exchange.get_last_prices()
#     for symbol in prices:
#         symbol_renko_bricks[symbol].new_price(prices[symbol])
#         print(f'{symbol} : {symbol_renko_bricks[symbol].renko_bricks}')
#
#     sleep_time = GET_PRICE_PERIOD - (time.time() - initial_time)
#     if sleep_time > 0:
#         time.sleep(sleep_time)
