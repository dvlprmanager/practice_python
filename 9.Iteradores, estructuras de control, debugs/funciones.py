def saludar(nombre):
    """Función que saluda a una persona."""
    return f"Hola, {nombre}!"

def sumar(a, b):
    """Función que suma dos números."""
    return a + b

def saludar_con_defecto(nombre="Amigo"):
    """Función con un parámetro por defecto."""
    return f"Hola, {nombre}!"

def operaciones(a, b):
    """Función que realiza múltiples operaciones y retorna varios valores."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

# Función lambda
sumar_lambda = lambda x, y: x + y

def ejecutar_funciones():
    print(saludar("Ana"))
    print(sumar(10, 5))
    print(saludar_con_defecto())
    print(saludar_con_defecto("Carlos"))
    suma, resta, multiplicacion = operaciones(15, 5)
    print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}")
    print(f"Suma usando lambda: {sumar_lambda(7, 3)}")

if __name__ == "__main__":
    ejecutar_funciones()
