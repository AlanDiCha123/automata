import re

# Definimos funcion caracter


def checkCharacter(char: str, state: int = 0) -> int:
    global simbolo
    global Fin
    simbolo = ""
    Fin = ""
    digit = "[0-9]"
    letra_min = "[a-z]"
    letra_may = "[A-Z]"
    letrai_min1 = "[a-h]"
    letrai_min2 = "[j-z]"
    letraf_min1 = "[a-e]"
    letraf_min2 = "[g-z]"
    letra_i = "i"
    letra_f = "f"
    guion = "_"

    if state == 0:
        if re.match(letra_i, char):
            simbolo = " letra "
            return 1, False
        elif re.match(letra_may, char):
            simbolo = " letra "
        elif re.match(guion, char):
            return 3, False
        elif re.match(letrai_min1, char):
            simbolo = " letra "
            return 3, False
        elif re.match(letrai_min2, char):
            simbolo = " letra "
            return 3, False
        elif re.match(digit, char):
            simbolo = " digit "
            return 4, False
        elif char == Fin:
            return state, True
        else:
            simbolo = " symbol "
            return 5, False
    elif state == 1:
        if re.match(letra_i, char):
            simbolo = " letra "
            return 1, False
        elif re.match(letra_f, char):
            return 2, False
        elif re.match(guion, char):
            return 1, False
        elif re.match(letra_may, char):
            simbolo = " letra "
        elif re.match(letraf_min1, char):
            simbolo = " letra "
            return 1, False
        elif re.match(letraf_min2, char):
            simbolo = " letra "
            return 1, False
        elif re.match(digit, char):
            simbolo = " digit "
            return 1, False
        elif char == Fin:
            return state, True
        else:
            simbolo = " symbol "
            return 5, False
    elif state == 2:
        if re.match(letra_i, char):
            simbolo = " i "
            return 3, False
        elif re.match(letra_may, char):
            simbolo = " letra "
            return 3, False
        elif re.match(guion, char):
            return 3, False
        elif re.match(letrai_min1, char):
            simbolo = " letra "
            return 3, False
        elif re.match(letrai_min2, char):
            simbolo = " letra "
            return 3, False
        elif re.match(digit, char):
            simbolo = " digit "
            return 3, False
        elif char == Fin:
            simbolo = " symbol "
            return state, True
        else:
            return 5, False
    elif state == 3:
        if re.match(letra_i, char):
            simbolo = " i "
            return 3, False
        elif re.match(letra_may, char):
            simbolo = " letra "
            return 3, False
        elif re.match(letrai_min1, char):
            simbolo = " letra "
            return 3, False
        elif re.match(guion, char):
            return 3, False
        elif re.match(letrai_min2, char):
            simbolo = " letra "
            return 3, False
        elif re.match(digit, char):
            simbolo = " digit "
            return 3, False
        elif char == Fin:
            return state, True
        else:
            simbolo = " symbol "
            return 5, False
    elif state == 4:
        if re.match(letra_i, char):
            simbolo = " i "
            return 5, False
        elif re.match(letra_may, char):
            simbolo = " letra "
            return 5, False
        elif re.match(letrai_min1, char):
            simbolo = " letra "
            return 5, False
        elif re.match(letrai_min2, char):
            simbolo = " letra "
            return 5, False
        elif re.match(digit, char):
            simbolo = " digit "
            return 4, False
        elif char == Fin:
            return state, True
        else:
            simbolo = " symbol "
            return 5, False
    elif state == 5:
        if re.match(digit, char):
            simbolo = " digit "
            return 5, False
        elif re.match(letra_min, char):
            simbolo = " letra "
            return 5, False
        elif re.match(letra_may, char):
            simbolo = " letra "
            return 5, False
        elif char == Fin:
            return state, True
        else:
            simbolo = " symbol "
            return 5, False
    exit()


# Definimos funcion encabezado
def encabezado():
    print('| Edo. Actual | Caracter | Simbolo | Edo. Siguiente |')
    body()


# imprime linea
def body():
    print("+--------------+-------+-----------+----------------+")


# MAIN
# Tabla de transiciones
# table: int | str = [
#     [1, 3, 3, 3, 4, 5, "E"],
#     [1, 2, 1, 1, 1, 5, "A"],
#     [3, 3, 3, 3, 3, 5, "A"],
#     [3, 3, 3, 3, 3, 5, "A"],
#     [5, 5, 5, 5, 4, 5, "A"],
#     [5, 5, 5, 5, 5, 5, "A"],
# ]

string: str = input("Ingrese una cadena a evaluar: ")
body()
encabezado()
state = 0
# Loop to iterate in string
if len(string) == 0:
    print("no hay nada para evaluar")
else:
    for char in string:

        next_state = state
        # Call character method to verify if a character is correct
        state, fin = checkCharacter(char, state)
        print(
            f"|      {next_state}      |    {char}     | {simbolo} |        {state}       |")
        body()

msg = "Cadena valida" if state != 5 else "Cadena no valida"
if state != 5:
    if state == 1:
        print("Es un identificador")
    elif state == 2:
        print("Es una palabra reservada")
    elif state == 3:
        print("Es un identificador")
    elif state == 4:
        print("Es un numero")

print(msg)
