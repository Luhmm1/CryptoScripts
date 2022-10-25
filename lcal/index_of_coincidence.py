import pandas as pd

from . import frequency_analysis as fa

def from_text(text: str, target_pattern: str = "[^ ]*", normalize: bool = False):
    ioc = 0
    symbols = fa.count_symbols(text, target_pattern=target_pattern, normalize=normalize)

    for c in symbols.values:
        ioc += c * (c - 1)

    return ioc / (symbols.sum() * (symbols.sum() - 1))

def from_frequencies(frequencies: pd.Series|dict):
    frequencies = pd.Series(frequencies)
    ioc = 0

    for f in frequencies.values:
        ioc += f ** 2

    return ioc
