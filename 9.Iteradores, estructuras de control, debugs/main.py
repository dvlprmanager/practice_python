from iteradores import usar_iterador, usar_generador
from estructuras_de_control import (
    condicionales,
    bucle_for,
    bucle_while,
    bucle_break_continue
)
from debugging import (
    funcion_sin_debug,
    funcion_con_logging,
    funcion_con_pdb,
    ejecutar_debugging
)
from funciones import ejecutar_funciones
from clases import ejecutar_clases
from excepciones import ejecutar_excepciones
from file_io import ejecutar_file_io
from data_structures import ejecutar_data_structures
import modules  # Importando el módulo creado

def ejecutar_modules():
    print("Usando el módulo 'modules.py':")
    a, b = 10, 5
    print(f"{a} + {b} = {modules.sumar(a, b)}")
    print(f"{a} - {b} = {modules.restar(a, b)}")
    print(f"{a} * {b} = {modules.multiplicar(a, b)}")
    try:
        print(f"{a} / {b} = {modules.dividir(a, b)}")
        print(f"{a} / 0 = {modules.dividir(a, 0)}")  # Esto lanzará una excepción
    except ValueError as e:
        print(f"Error: {e}")

def main():
    print("=== Ejemplos de Iteradores ===")
    usar_iterador()
    print()
    usar_generador()
    print("\n=== Estructuras de Control ===")
    condicionales()
    bucle_for()
    bucle_while()
    bucle_break_continue()
    print("\n=== Debugging ===")
    ejecutar_debugging()
    print("\n=== Funciones ===")
    ejecutar_funciones()
    print("\n=== Clases ===")
    ejecutar_clases()
    print("\n=== Excepciones ===")
    ejecutar_excepciones()
    print("\n=== File I/O ===")
    ejecutar_file_io()
    print("\n=== Estructuras de Datos ===")
    ejecutar_data_structures()
    print("\n=== Módulos ===")
    ejecutar_modules()

if __name__ == "__main__":
    main()
