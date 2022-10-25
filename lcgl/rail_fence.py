def _check_arguments(nb_rails: int):
    if nb_rails < 2:
        raise ValueError("'nb_rails' must be at least 2.")

def encrypt(plaintext: str, nb_rails: int = 2):
    _check_arguments(nb_rails)

    ciphertext = [""] * nb_rails
    current_rail = 0

    for char in plaintext:
        ciphertext[abs(current_rail)] += char

        if current_rail == nb_rails - 1:
            current_rail = -1 * nb_rails + 2
        else:
            current_rail += 1

    return "".join(ciphertext)

def decrypt(ciphertext: str, nb_rails: int = 2):
    _check_arguments(nb_rails)

    return None
