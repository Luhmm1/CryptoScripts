DEFAULT_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext: str, key: str, alphabet: str = DEFAULT_ALPHABET):
    ciphertext = ""

    for i in range(len(plaintext)):
        try:
            ciphertext += alphabet[(alphabet.index(plaintext[i]) + alphabet.index(key[i % len(key)])) % len(alphabet)]
        except (IndexError, ValueError):
            ciphertext += "�"

    return ciphertext

def decrypt(ciphertext: str, key: str, alphabet: str = DEFAULT_ALPHABET):
    plaintext = ""

    for i in range(len(ciphertext)):
        try:
            plaintext += alphabet[(alphabet.index(ciphertext[i]) - alphabet.index(key[i % len(key)])) % len(alphabet)]
        except (IndexError, ValueError):
            plaintext += "�"

    return plaintext
