def suma(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos parámetros deben ser de tipo entero")
    return a + b

def concatenar(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Ambos parámetros deben ser de tipo cadena")
    return a + b

if __name__ == "__main__":
    try:
        print(suma(10, 20))         # 30
        print(suma("10", 20))       # Esto lanzará una excepción
    except TypeError as e:
        print(f"Error: {e}")

    try:
        print(concatenar("Hola, ", "mundo!"))  # Hola, mundo!
        print(concatenar(10, "mundo!"))        # Esto lanzará una excepción
    except TypeError as e:
        print(f"Error: {e}")
