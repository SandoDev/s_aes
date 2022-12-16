from s_aes.logic.utils import ascii_to_hex
from s_aes.logic.utils import hex_to_ascii
from s_aes.logic.utils import listbin_split
from s_aes.logic.utils import listbin_to_matrix
from s_aes.logic.utils import listhex_to_bin
from s_aes.logic.utils import matrixhex_to_bin
from s_aes.logic.utils import matrixbin_to_hex
from s_aes.logic.utils import matrix_to_list
from s_aes.logic.utils import print_hex_matrix, print_matrix

from s_aes.logic.methods import add_key, nibble_substitution, shift_row, mix_column


def round_0(matrix_bin, key):
    list_key_bin = listbin_split([key], split=8)
    list_key_bin = listbin_split(list_key_bin, split=4)
    matrix_key_bin = listbin_to_matrix(list_key_bin)
    new_state = add_key(matrix_bin, matrix_key_bin)

    return new_state


def round_1(matrix_bin, key):
    new_state1 = nibble_substitution(matrix_bin)
    new_state2 = shift_row(new_state1)
    new_state3 = mix_column(new_state2)

    list_key_bin = listbin_split([key], split=8)
    list_key_bin = listbin_split(list_key_bin, split=4)
    matrix_key_bin = listbin_to_matrix(list_key_bin)
    new_state3 = matrixhex_to_bin(new_state3)
    new_state4 = add_key(new_state3, matrix_key_bin)

    return new_state4


def round_2(matrix_bin, key):
    new_state1 = nibble_substitution(matrix_bin)
    new_state2 = shift_row(new_state1)

    list_key_bin = listbin_split([key], split=8)
    list_key_bin = listbin_split(list_key_bin, split=4)
    matrix_key_bin = listbin_to_matrix(list_key_bin)
    new_state2 = matrixhex_to_bin(new_state2)
    new_state3 = add_key(new_state2, matrix_key_bin)

    return new_state3


def encrypt_saes(value_to_encrypt, keys):
    k0, k1, k2 = keys

    list_in_hex, _ = ascii_to_hex(value_to_encrypt, step=1)
    list_in_bin = listhex_to_bin(list_in_hex)
    list_in_bin = listbin_split(list_in_bin, split=4)
    matrix_in_bin = listbin_to_matrix(list_in_bin)

    # Round 0
    new_state = round_0(matrix_in_bin, k0)
    # print_hex_matrix(new_state)

    # Round 1
    new_state = round_1(new_state, k1)
    # print_hex_matrix(new_state)

    # Round 2
    new_state = round_2(new_state, k2)
    # print_hex_matrix(new_state)

    matrix_hex = matrixbin_to_hex(new_state)
    _, str_hex = matrix_to_list(matrix_hex)
    _, text_encrypt = hex_to_ascii(str_hex, 2)

    return text_encrypt
