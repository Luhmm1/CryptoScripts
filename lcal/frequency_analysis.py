import pandas as pd
import re
import unidecode

def count_symbols(text: str, target_pattern: str = ".*", normalize: bool = False):
    target_pattern = re.compile(target_pattern)

    if normalize:
        text = unidecode.unidecode(text.upper())

    count = pd.Series(dtype=int)

    for char in text:
        if char in count:
            count[char] += 1
        elif target_pattern.fullmatch(char):
            count[char] = 1

    return count

def calculate_frequencies(text: str, target_pattern: str = ".*", normalize: bool = False):
    frequencies = count_symbols(text, target_pattern=target_pattern, normalize=normalize)

    return frequencies / frequencies.sum()
