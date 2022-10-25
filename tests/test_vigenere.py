from lcgl.vigenere import encrypt, decrypt

def test_encrypt():
    assert encrypt("TEST", "KEY") == "DIQD"

def test_decrypt():
    assert decrypt("DIQD", "KEY") == "TEST"

def test_encrypt_with_unknown_char():
    assert encrypt("HELLO WORLD", "KEY") == "RIJVS�GSPVH"

def test_decrypt_with_unknown_char():
    assert decrypt("RIJVS�GSPVH", "KEY") == "HELLO�WORLD"

def test_encrypt_with_another_alphabet():
    new_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert encrypt("YESTERDAY", "MONDAY", new_alphabet) == "K2F6OPZYL"
    assert encrypt("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", "SUNDAY", new_alphabet) == "SVPGE3Y1VMK9471SQFAD7YWLGJD42RMPJA8X"

def test_decrypt_with_another_alphabet():
    new_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert decrypt("K2F6OPZYL", "MONDAY", new_alphabet) == "YESTERDAY"
    assert decrypt("SVPGE3Y1VMK9471SQFAD7YWLGJD42RMPJA8X", "SUNDAY", new_alphabet) == "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
