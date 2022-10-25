from lcgl.caesar import encrypt, decrypt

def test_encrypt():
    assert encrypt("TEST", 0)  == "TEST"
    assert encrypt("TEST", 26) == "TEST"
    assert encrypt("TEST", 3)  == "WHVW"
    assert encrypt("TEST", 13) == "GRFG"
    assert encrypt("GRFG", 13) == "TEST"
    assert encrypt("TEST", 40) == "HSGH"

def test_decrypt():
    assert decrypt("TEST", 0)  == "TEST"
    assert decrypt("TEST", 26) == "TEST"
    assert decrypt("WHVW", 3)  == "TEST"
    assert decrypt("GRFG", 13) == "TEST"
    assert decrypt("TEST", 13) == "GRFG"
    assert decrypt("HSGH", 40) == "TEST"

def test_encrypt_with_unknown_char():
    assert encrypt("SALUT À TOUS", 3) == "VDOXW���WRXV"

def test_decrypt_with_unknown_char():
    assert decrypt("VDOXW���WRXV", 3) == "SALUT���TOUS"

def test_encrypt_with_another_alphabet():
    new_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert encrypt("YESTERDAY", 3, new_alphabet) == "1HVWHUGD1"

def test_decrypt_with_another_alphabet():
    new_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert decrypt("1HVWHUGD1", 3, new_alphabet) == "YESTERDAY"
