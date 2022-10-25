import numpy as np

DEFAULT_SQUARE = np.array([
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "X", "Y", "Z"]
])

def encrypt(plaintext: str, square: np.ndarray|list = DEFAULT_SQUARE):
    square = np.array(square)
    ciphertext = ""

    for char in plaintext:
        position = np.where(square == char)

        try:
            ciphertext += str(position[0][0] + 1) + str(position[1][0] + 1)
        except IndexError:
            ciphertext += "��"

    return ciphertext

def decrypt(ciphertext: str, square: np.ndarray|list = DEFAULT_SQUARE):
    square = np.array(square)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        try:
            plaintext += square[int(ciphertext[i]) - 1, int(ciphertext[i + 1]) - 1]
        except (IndexError, ValueError):
            plaintext += "�"

    return plaintext
