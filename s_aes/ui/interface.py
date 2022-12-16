from s_aes.logic.encrypt import encrypt_saes
from s_aes.logic.decrypt import decrypt_saes
from s_aes.logic.key_logic import generate_keys
from s_aes.attacks.brute_force import force_brute_attack


def ui_keys():
    print("Digite su llave de encriptación:", end=" ")
    key = input()  # "-U" #
    keys = generate_keys(key)
    # print("Guarde sus llaves", keys)
    return keys


def ui_encryp():
    keys = ui_keys()
    print("Digite su frase a encriptar:", end=" ")
    value_to_encrypt = input()  # "§I" #
    value_encrypt = encrypt_saes(value_to_encrypt, keys)
    print()
    print("Texto encriptado:", value_encrypt)


def ui_decrypt():
    keys = ui_keys()
    print("Digite su frase a desencriptar:", end=" ")
    value_to_decrypt = input()  # "ÃI" #
    value_decrypt = decrypt_saes(value_to_decrypt, keys)
    print()
    print("Texto desencriptado:", value_decrypt)


def ui_attack_brute():
    print("Digite su frase a desencriptar:", end=" ")
    value_to_decrypt = input()  # "ÃI" #
    result = force_brute_attack(value_to_decrypt)
    print("==== Resultados del ataque =====")
    for i in result:
        print("LLave:", "".join(i[0]))
        print("Valor desencriptado:", i[1])
        print()


def menu():
    print("#### Bienvenido a S-AES ####")
    print()
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Ataque por fuerza bruta")
    value = input()
    print()
    if value == "1":
        ui_encryp()
    elif value == "2":
        ui_decrypt()
    elif value == "3":
        ui_attack_brute()
    else:
        print("Opción invalida")
        exit()
