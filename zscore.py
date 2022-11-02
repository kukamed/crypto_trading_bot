from dataclasses import dataclass

@dataclass
class ZscoreData:
    zscore_length: int
    zscore_threshold: float
    is_long: bool

def get_zscore_value(values: float, zscore_length: int) -> float:

    zscore_length = zscore_length
    sum = 0
    for value in values[-zscore_length::]:
        sum += value
    mean = sum / zscore_length

    sum = 0
    for value in values[-zscore_length::]:
        sum += (mean - value) ** 2
    std = (sum / zscore_length) ** 0.5

    zscore = (values[-1] - mean) / std
    return zscore