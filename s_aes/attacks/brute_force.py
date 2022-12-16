import string
import re
from itertools import permutations

from s_aes.logic.decrypt import decrypt_saes
from s_aes.logic.key_logic import generate_keys

# Las llaves se tomaran de las permutacions de 2 caracteres imprimibles
perm = list(permutations(string.printable, 2))


def validator_one(values_decrypt):
    """
    Se limpian los valores tomando aquellos donde todos sus caracteres sean imprimibles de ascii
    """
    values_pista = []
    for key, value in values_decrypt.items():
        if all([v in string.printable for v in value]):
            values_pista.append((key, value))

    return values_pista


def validator_two(values_pista: list):
    """
    Segundo validaor para quitar las cadenas que no contengan digitos ni letras

    \w - Matches any alphanumeric character (digits and alphabets). 
    Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.
    """
    values_pista2 = []

    pattern = '\w'
    for vv in values_pista:
        result = re.match(pattern, vv[1])

        if result:
            values_pista2.append(vv)

    return values_pista2


def validator_three(values_pista2):
    """
    Tercer validador para dejar solo aquellas cadenas que tengan solo digitos o letras del alfabeto

    \W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]
    """
    values_pista3 = []

    pattern = '\W'
    for vv in values_pista2:
        result = re.findall(pattern, vv[1])

        if not result:
            values_pista3.append(vv)

    return values_pista3


def force_brute_attack(text_encrypt):
    """
    Realiza un ataque de fuerza bruta tratando de desencriptar el texto crifrado
    con todas las llaves posibles de 2 caracteres imprimibles de ascii

    con los resultados del desemcriptamiento, ejecuta validaciones 
    regex para filtrar resultados y mostrar un posible pareja de clave-texto_desencriptado
    """

    # text_encrypt = "'¤õ3"

    values_decrypt = {
        item: decrypt_saes(text_encrypt, generate_keys("".join(item)))
        for item in perm
    }

    list_one = validator_one(values_decrypt)
    list_two = validator_two(list_one)
    list_three = validator_three(list_two)

    return list_three
