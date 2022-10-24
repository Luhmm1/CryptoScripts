DEFAULT_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext: str, key: int, alphabet: str = DEFAULT_ALPHABET):
    ciphertext = ""

    for char in plaintext:
        try:
            ciphertext += alphabet[(alphabet.index(char) + key) % len(alphabet)]
        except (IndexError, ValueError):
            ciphertext += "�"

    return ciphertext

def decrypt(ciphertext: str, key: int, alphabet: str = DEFAULT_ALPHABET):
    plaintext = ""

    for char in ciphertext:
        try:
            plaintext += alphabet[(alphabet.index(char) - key) % len(alphabet)]
        except (IndexError, ValueError):
            plaintext += "�"

    return plaintext
