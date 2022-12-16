from s_aes.resources.resources import s_box, s_box_inverse, sbox_sum, sbox_mul


def add_key(matrix_block, matrix_key):
    """
    Ak
    """
    m = []
    for row in range(len(matrix_block)):
        r = []
        for column in range(len(matrix_block)):
            val1 = int(matrix_block[row][column], 2)
            val2 = int(matrix_key[row][column], 2)
            # print(val1, val2)
            xor = val1 ^ val2
            r.append(bin(xor)[2:].zfill(4))
        m.append(r)

    return m


def nibble_substitution(matrix, inverse: bool = False):
    """
    NS

    bin -> hex

    pass for s_box or s_box_inverse
    """
    s_box_f = s_box_inverse if inverse else s_box
    result = map(lambda x: [s_box_f[i] for i in x], matrix)
    return list(result)


def shift_row(matrix, inverse: bool = False):
    """
    SR
    """
    return [matrix[0], [matrix[1][1], matrix[1][0]]]


def mix_column(matrix):
    """
    MC
    """
    s00 = matrix[0][0].upper()
    s10 = matrix[1][0].upper()
    s01 = matrix[0][1].upper()
    s11 = matrix[1][1].upper()

    # s_00 = s00 + (4 * s10)
    col = s00
    row = int(str(sbox_mul[s10][4]), 16)
    s_00 = sbox_sum[col][row]

    # s_10 = (4 * s00) + s10
    col = s10
    row = int(str(sbox_mul[s00][4]), 16)
    s_10 = sbox_sum[col][row]

    # s_01 = s01 + (4 * s11)
    col = s01
    row = int(str(sbox_mul[s11][4]), 16)
    s_01 = sbox_sum[col][row]

    # s_11 = (4 * s01) + s11
    col = s11
    row = int(str(sbox_mul[s01][4]), 16)
    s_11 = sbox_sum[col][row]

    return [[s_00, s_01], [s_10, s_11]]


def mix_column_inverse(matrix):
    """
    MC

    [['6', '4'], ['c', '0']]
    """
    s00 = matrix[0][0].upper()
    s10 = matrix[1][0].upper()
    s01 = matrix[0][1].upper()
    s11 = matrix[1][1].upper()

    # s_00 = (9 * s00) + (2 * s10)
    col = str(sbox_mul[s00][9])
    row = int(str(sbox_mul[s10][2]).upper(), 16)
    s_00 = sbox_sum[col][row]

    # s_10 = (2 * s00) + (9 * s10)
    col = str(sbox_mul[s00][2])
    row = int(str(sbox_mul[s10][9]).upper(), 16)
    s_10 = sbox_sum[col][row]

    # s_01 = (9 * s01) + (2 * s11)
    col = str(sbox_mul[s01][9])
    row = int(str(sbox_mul[s11][2]).upper(), 16)
    s_01 = sbox_sum[col][row]

    # s_11 = (2 * s01) + (9 * s11)
    col = str(sbox_mul[s01][2])
    row = int(str(sbox_mul[s11][9]).upper(), 16)
    s_11 = sbox_sum[col][row]

    return [[s_00, s_01], [s_10, s_11]]
