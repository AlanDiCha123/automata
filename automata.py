import re


def checkCharacter(char: str) -> int:
    '''
    Toma un caracter, verifica el tipo y retorna el numero de acuerdo con el arreglo de simbolos
    '''
    digit = "[0-9]"
    letra_min = "[a-z]"
    letra_may = "[A-Z]"
    letra_i = "i"
    letra_f = "f"
    underscore = "_"
    if re.match(letra_min, char) or re.match(letra_may, char):
        if re.match(letra_i, char):
            return 0
        elif re.match(letra_f, char):
            return 1
        else:
            return 3
    elif re.match(digit, char):
        return 4
    elif re.match(underscore, char):
        return 2
    else:
        return 5


def autom(cadena: str):
    '''
    Funcion principal encargada de imprimir la tabla de transiciones entre los estados
    '''
    # * Tabla de transiciones
    table = [
        [1, 3, 3, 3, 4, 5],
        [1, 2, 1, 1, 1, 5],
        [3, 3, 3, 3, 3, 5],
        [3, 3, 3, 3, 3, 5],
        [5, 5, 5, 5, 4, 5],
        [5, 5, 5, 5, 5, 5],
    ]
    '''
    Se encarga de catalogar los caracteres en los simbolos correspondientes. 
    Si la letra es "i" o "f" se cataloga como letra, por ello se repite letra varias veces
    Teniendo en cuenta el sig. orden
    i: letra, f: letra, _: simbolo, [a-z],[A-Z]: letra, [0-9]: digito, [$|%|...]: simbolo
    '''
    simbolos = ["letra", "letra", "simbolo", "letra", "digito", "simbolo"]
    # * Guarda el estado siguiente. Por default inicia en el estado 0
    sig_estado: int = 0

    # Ciclo toma cada caracter de la cadena y la evalua llamando a la funcion
    # checkCharacter, la cual retorna la clase a la que pertenece dicho caracter
    for char in cadena:
        # Guarda el estado actual para no borrarse
        estado_actual = sig_estado
        # Call character method to verify if a character is correct
        clase = checkCharacter(char)
        # Almacena el siguiente estado segun la tabla (array) y los parametros dados
        sig_estado = table[estado_actual][clase]
    # * El estado 5 es aquel estado que determina cuando la cadena no es valida
    msg = "Cadena valida" if sig_estado != 5 else "Cadena no valida"
    # * Si el estado no es 5 verifica el ultimo estado almacenado y asigna que tipo fue
    # * la cadena
    if sig_estado != 5:
        if sig_estado == 1:
            print("Es un identificador")
        elif sig_estado == 2:
            print("Es una palabra reservada")
        elif sig_estado == 3:
            print("Es un identificador")
        elif sig_estado == 4:
            print("Es un numero")
    print(msg)


def checkTable(estado_actual: int, clase: int) -> int:
    table = [
        [1, 3, 3, 3, 4, 5],
        [1, 2, 1, 1, 1, 5],
        [3, 3, 3, 3, 3, 5],
        [3, 3, 3, 3, 3, 5],
        [5, 5, 5, 5, 4, 5],
        [5, 5, 5, 5, 5, 5],
    ]
    return table[estado_actual][clase]


if __name__ == "__main__":
    autom()
