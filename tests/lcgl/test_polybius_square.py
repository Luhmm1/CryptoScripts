import numpy as np

from lcgl.polybius_square import encrypt, decrypt

def test_encrypt():
    assert encrypt("POLYBIUSSQUARE") == "4135325412245144444251114315"

def test_decrypt():
    assert decrypt("4135325412245144444251114315") == "POLYBIUSSQUARE"

def test_encrypt_with_unknown_char():
    assert encrypt("POLYBIUS SQUARE") == "4135325412245144��444251114315"

def test_decrypt_with_unknown_char():
    assert decrypt("4135325412245144��444251114315") == "POLYBIUS�SQUARE"

def test_encrypt_with_another_square():
    new_square = np.array([
        list("456789"),
        list("GHIJKL"),
        list("STUVWX"),
        list("ABCDEF"),
        list("YZ0123"),
        list("MNOPQR")
    ])

    assert encrypt("POLYBIUSSQUARE", new_square) == "6463265142233331316533416645"

def test_decrypt_with_another_square():
    new_square = np.array([
        list("456789"),
        list("GHIJKL"),
        list("STUVWX"),
        list("ABCDEF"),
        list("YZ0123"),
        list("MNOPQR")
    ])

    assert decrypt("6463265142233331316533416645", new_square) == "POLYBIUSSQUARE"
