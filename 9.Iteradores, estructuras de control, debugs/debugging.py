import pdb
import logging

# Configuración básica de logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')

def funcion_sin_debug(a, b):
    resultado = a + b
    print(f"Resultado: {resultado}")
    return resultado

def funcion_con_logging(a, b):
    logging.debug(f"Entrando en funcion_con_logging con a={a}, b={b}")
    resultado = a + b
    logging.info(f"Resultado: {resultado}")
    return resultado

def funcion_con_pdb(a, b):
    pdb.set_trace()  # Punto de interrupción para depurar
    resultado = a + b
    return resultado

def ejecutar_debugging():
    print("Ejecutando función sin debugging:")
    funcion_sin_debug(3, 4)

    print("\nEjecutando función con logging:")
    funcion_con_logging(5, 7)

    print("\nEjecutando función con pdb (se detendrá aquí):")
    # Descomenta la siguiente línea para depurar con pdb
    # funcion_con_pdb(10, 20)

if __name__ == "__main__":
    ejecutar_debugging()
