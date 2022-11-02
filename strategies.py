from renko import *
import file_handler

class StrategyData():
    pass

class Strategies():

    strategies: list[StrategyData] = []

    def __init__(self, load_strategies_function):
        self.strategies = load_strategies_function()












