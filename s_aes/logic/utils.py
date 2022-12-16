

def hex_to_ascii(str_hex, step) -> tuple:
    """
    Returns a list with each character in ascci and a string with all ascii

    "c349" -> (['Ã', 'I'], 'ÃI')
    """
    lis_hex = [str_hex[i:i+step] for i in range(0, len(str_hex), step)]
    lis_chr = [chr(int(i, 16)) for i in lis_hex]
    return lis_chr, "".join(lis_chr)


def ascii_to_hex(str_ascii, step) -> tuple:
    """
    Returns a list with each character in hexadecimal and a string with all hexadecimal

    "§I" -> (["a7","49"], 'a749')
    """
    lis_hex = [str_ascii[i:i+step] for i in range(0, len(str_ascii), step)]
    lis_chr = [hex(ord(i))[2:] for i in lis_hex]
    return lis_chr, "".join(lis_chr)


def listhex_to_bin(list_hex):
    """
    converts a list of hexadecimal value to binary

    ["a7","49"] => ["10100111","01001001"]
    """
    return [bin(int(i, 16))[2:].zfill(8) for i in list_hex]


def listbin_split(list_in_bin, split):
    """
    ['10100111', '01001001'] -> ['1010', '0111', '0100', '1001']
    """
    l = []
    for value in list_in_bin:
        l.extend([value[i:i+split] for i in range(0, len(value), split)])
    return l


def listbin_to_matrix(list_in_bin):
    """
    ['1010', '0111', '0100', '1001'] -> [['1010','0100'],['0111', '1001']]
    """
    return [[list_in_bin[0], list_in_bin[2]], [list_in_bin[1], list_in_bin[3]]]


def print_matrix(matrix):
    """
    print a matrix
    """
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()


def matrixhex_to_bin(matrix):
    m00 = bin(int(matrix[0][0], 16))[2:].zfill(4)
    m10 = bin(int(matrix[1][0], 16))[2:].zfill(4)
    m01 = bin(int(matrix[0][1], 16))[2:].zfill(4)
    m11 = bin(int(matrix[1][1], 16))[2:].zfill(4)

    return [[m00, m01], [m10, m11]]


def matrixbin_to_hex(matrix):
    m = []
    for i in matrix:
        r = []
        for j in i:
            value = hex(int(j, 2))[2:]
            r.append(value)
        m.append(r)

    return m


def print_hex_matrix(matrix):
    print()
    print("Matrix:")  # nibble representation
    for i in matrix:
        for j in i:
            try:
                print(hex(int(j, 2))[2:], end="\t")
            except:
                print(j, end="\t")

        print()


def matrix_to_list(matrix):
    m = [
        matrix[0][0],
        matrix[1][0],
        matrix[0][1],
        matrix[1][1],
    ]

    return m, "".join(m)
