from s_aes.logic.encrypt import encrypt_saes
from s_aes.logic.decrypt import decrypt_saes
from s_aes.logic.key_logic import generate_keys


def menu():
    print("#### Bienvenido a S-AES ####")
    print()
    print("Digite su llave de encriptación:", end=" ")
    key = input()  # "-U" #
    keys = generate_keys(key)
    # print("Guarde sus llaves", keys)
    print()
    print("1. Encriptar")
    print("2. Desencriptar")
    value = input()
    print()
    if value == "1":
        print("Digite su frase a encriptar:", end=" ")
        value_to_encrypt = input()  # "§I" #
        value_encrypt = encrypt_saes(value_to_encrypt, keys)
        print()
        print("Texto encriptado:", value_encrypt)
    elif value == "2":
        print("Digite su frase a desencriptar:", end=" ")
        value_to_decrypt = input()  # "ÃI" #
        value_decrypt = decrypt_saes(value_to_decrypt, keys)
        print()
        print("Texto desencriptado:", value_decrypt)
    else:
        print("Opción invalida")
        exit()
