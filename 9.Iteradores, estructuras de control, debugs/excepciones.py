class MiError(Exception):
    """Excepción personalizada."""
    pass

def dividir(a, b):
    """Función que divide dos números y maneja la división por cero."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"El resultado de la división es {resultado}.")
    finally:
        print("Ejecución de la operación de división finalizada.")

def manejar_mi_error(valor):
    """Función que lanza una excepción personalizada si el valor es negativo."""
    if valor < 0:
        raise MiError("El valor no puede ser negativo.")
    else:
        print(f"El valor es {valor}.")

def ejecutar_excepciones():
    dividir(10, 2)
    print()
    dividir(5, 0)
    print()

    try:
        manejar_mi_error(10)
        manejar_mi_error(-5)
    except MiError as e:
        print(f"Capturada MiError: {e}")

if __name__ == "__main__":
    ejecutar_excepciones()
