from dataclasses import dataclass
import file_handler

from strategies import StrategyData
from renko import RenkoData
from zscore import ZscoreData
from klines import KlinesData
from partial_exits import PartialExitsData


# TODO: Add a strategy that uses the zscore and renko system to trade
@dataclass
class ZscoreRenkoStrategyData(StrategyData, ZscoreData, RenkoData, KlinesData, PartialExitsData):
    pass


def load_zscore_renko_strategies() -> list[StrategyData]:
    strategies_dict = file_handler.load_zscore_renko_strategies()
    strategies = [ZscoreRenkoStrategyData(**strategy) for strategy in strategies_dict]
    return strategies