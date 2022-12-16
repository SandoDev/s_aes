from s_aes.resources.resources import s_box
from s_aes.logic.utils import ascii_to_hex
from s_aes.logic.utils import listhex_to_bin


def g(w, n):
    """
    fuction g for key expansion
    """

    def SubNib(n0, n1):
        n0 = bin(int(s_box[n0], 16))[2:].zfill(4)
        n1 = bin(int(s_box[n1], 16))[2:].zfill(4)
        return n0, n1

    def RCON(n):
        if n == 1:
            return "10000000"
        elif n == 2:
            return "00110000"

    # RotNib
    n1, n0 = w[:4], w[4:]

    n0, n1 = SubNib(n0, n1)
    w = n0+n1
    w = int(RCON(n), 2) ^ int(w, 2)
    return bin(w)[2:].zfill(8)


def key_expansion(w):
    """
    Generates the expansion of keys

    return three keys
    k0, k1, k2
    """
    # w = hex_to_bin(key, 8)
    w0 = w[0]
    w1 = w[1]

    w2 = bin(int(w0, 2) ^ int(g(w1, 1), 2))[2:].zfill(8)
    w3 = bin(int(w2, 2) ^ int(w1, 2))[2:].zfill(8)
    w4 = bin(int(w2, 2) ^ int(g(w3, 2), 2))[2:].zfill(8)
    w5 = bin(int(w4, 2) ^ int(w3, 2))[2:].zfill(8)

    # k0[w0,w1], k1[w2,w3], k2[w4,w5]
    k0 = w0+w1
    k1 = w2+w3
    k2 = w4+w5

    return k0, k1, k2


def generate_keys(key):
    """
    Takes the user's key and generates the 3 keys for the encryption and decryption process
    """
    list_in_hex, _ = ascii_to_hex(key, step=1)
    list_in_bin = listhex_to_bin(list_in_hex)

    keys = key_expansion(list_in_bin)
    return keys
