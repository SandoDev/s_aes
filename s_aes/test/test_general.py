from s_aes.logic.encrypt import encrypt_saes
from s_aes.logic.decrypt import decrypt_saes
from s_aes.logic.key_logic import generate_keys
from s_aes.logic.utils import print_hex_matrix, print_matrix

keys = generate_keys("-U")


def test_encryp():
    value_to_encryp = "§I"
    value_encryp = encrypt_saes(value_to_encryp, keys)
    assert value_encryp == "ÃI"


def test_decryp():
    value_to_decryp = "ÃI"
    value_decryp = decrypt_saes(value_to_decryp, keys)
    assert value_decryp == "§I"


def test_all_flow():
    value_to_encryp = "§I"
    value_decryp = decrypt_saes(encrypt_saes(value_to_encryp, keys), keys)
    assert value_decryp == "§I"


def test_print():
    """
    0100    0011
    0011    1010
    """
    m = [["0100", "0011"], ["0011", "1010"]]
    print_matrix(m)
    print_hex_matrix(m)
    assert True
