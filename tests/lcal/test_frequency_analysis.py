import lcal.frequency_analysis as fa

def test_count_symbols():
    assert dict(fa.count_symbols("Hello World! (WOW)"))  == {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'W': 3, 'r': 1, 'd': 1, '!': 1, '(': 1, 'O': 1, ')': 1}
    assert dict(fa.count_symbols("Hello World! (WOW)", target_pattern="[a-zA-Z]*"))  == {'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 3, 'r': 1, 'd': 1, 'O': 1}
    assert dict(fa.count_symbols("Hello World! (WOW)", target_pattern="[A-Z]*", normalize=True))  == {'H': 1, 'E': 1, 'L': 3, 'O': 3, 'W': 3, 'R': 1, 'D': 1}

def test_calculate_frequencies():
    assert abs(1 - fa.calculate_frequencies("Hello World! (WOW)").sum()) < 0.01
    assert abs(1 - fa.calculate_frequencies("Hello World! (WOW)", target_pattern="[a-zA-Z]*").sum()) < 0.01
    assert abs(1 - fa.calculate_frequencies("Hello World! (WOW)", target_pattern="[A-Z]*", normalize=True).sum()) < 0.01
