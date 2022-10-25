import pytest

from lcgl.rail_fence import encrypt, decrypt

def test_encrypt():
    assert encrypt("TEST")  == "TSET"
    assert encrypt("HELLO") == "HLOEL"
    assert encrypt("WEAREDISCOVEREDRUNATONCE") == "WAEICVRDUAOCERDSOEERNTNE"
    assert encrypt("The rail fence cipher is a simple form of transposition cipher.") == "Teri ec ihri  ipefr ftasoiincpe.h alfnecpe sasml omo rnpsto ihr"

def test_encrypt_with_custom_nb_rails():
    with pytest.raises(ValueError):
        encrypt("TEST", 1)

    assert encrypt("TEST", 3)  == "TETS"
    assert encrypt("HELLO", 3) == "HOELL"
    assert encrypt("WEAREDISCOVEREDRUNATONCE", 3) == "WECRUOERDSOEERNTNEAIVDAC"
    assert encrypt("TEST", 6)  == "TEST"
    assert encrypt("HELLO", 6) == "HELLO"
    assert encrypt("WEAREDISCOVEREDRUNATONCE", 6) == "WVOEOETNACRACRSENEEIDUDR"
    assert encrypt("The rail fence cipher is a simple form of transposition cipher.", 6) == "Terpfiehfne mlo sthre chiie toip. lepss mrpoiri i  frasncacaon "
    assert encrypt("The rail fence cipher is a simple form of transposition cipher.", 7) == "Tc roehnesaompshree i f sip. fc s ontir iriefaicalpeml ro ihptn"
