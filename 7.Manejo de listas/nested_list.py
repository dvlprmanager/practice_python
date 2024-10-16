# Crear un tablero de 3x3 vacío (por ejemplo, para Tic-Tac-Toe)
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

# Realizar algunos movimientos
tablero[0][0] = "X"
tablero[1][1] = "O"
tablero[2][2] = "X"

print("Estado actual del tablero:")
imprimir_tablero(tablero)
# Salida:
# X| | 
# -----
#  |O| 
# -----
#  | |X
