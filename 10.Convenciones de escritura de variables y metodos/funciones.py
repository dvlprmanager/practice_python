def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    from constantes import PI
    area = PI * (radio ** 2)
    return area

def saludar_usuario(nombre):
    """Saluda al usuario por su nombre."""
    mensaje = f"Hola, {nombre}! Bienvenido."
    return mensaje

def obtener_nombre_completo(nombre, apellido):
    """Concatena el nombre y apellido para obtener el nombre completo."""
    nombre_completo = f"{nombre} {apellido}"
    return nombre_completo

def imprimir_resultados():
    area = calcular_area_circulo(5)
    saludo = saludar_usuario("Ana")
    nombre_completo = obtener_nombre_completo("Ana", "Pérez")
    
    print(f"Área del círculo: {area}")
    print(saludo)
    print(f"Nombre completo: {nombre_completo}")

if __name__ == "__main__":
    imprimir_resultados()
