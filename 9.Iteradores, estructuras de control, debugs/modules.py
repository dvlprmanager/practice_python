# Este archivo actúa como un módulo con funciones reutilizables

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta el segundo número del primero."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b
