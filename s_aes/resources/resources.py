import pandas as pd


s_box = {
    # row 1
    "0000": hex(int("1001", 2))[2:],
    "0001": hex(int("0100", 2))[2:],
    "0010": hex(int("1010", 2))[2:],
    "0011": hex(int("1011", 2))[2:],
    # row 2
    "0100": hex(int("1101", 2))[2:],
    "0101": hex(int("0001", 2))[2:],
    "0110": hex(int("1000", 2))[2:],
    "0111": hex(int("0101", 2))[2:],
    # row 3
    "1000": hex(int("0110", 2))[2:],
    "1001": hex(int("0010", 2))[2:],
    "1010": hex(int("0000", 2))[2:],
    "1011": hex(int("0011", 2))[2:],
    # row 4
    "1100": hex(int("1100", 2))[2:],
    "1101": hex(int("1110", 2))[2:],
    "1110": hex(int("1111", 2))[2:],
    "1111": hex(int("0111", 2))[2:],
}

s_box_inverse = {
    # row 1
    "0000": "a",
    "0001": "5",
    "0010": "9",
    "0011": "b",
    # row 2
    "0100": "1",
    "0101": "7",
    "0110": "8",
    "0111": "f",
    # row 3
    "1000": "6",
    "1001": "0",
    "1010": "2",
    "1011": "3",
    # row 4
    "1100": "c",
    "1101": "4",
    "1110": "d",
    "1111": "e",
}

index_labels = ["0", "1", "2", "3", "4", "5", "6",
                "7", "8", "9", "A", "B", "C", "D", "E", "F"]
path1 = "s_aes/resources/adition s_box.csv"
path2 = "s_aes/resources/multiplication s_box.csv"
sbox_sum = pd.read_csv(path1, names=index_labels)
sbox_mul = pd.read_csv(path2, names=index_labels)
