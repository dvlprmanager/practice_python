# Constantes definidas en mayúsculas
PI = 3.141592653589793
VELOCIDAD_LUZ = 299792458  # en metros por segundo
GRAVEDAD_TERRESTRE = 9.80665  # en m/s²

# Constantes con nombres descriptivos
MAX_INTENTOS = 5
TIEMPO_ESPERA = 30  # en segundos

def imprimir_constantes():
    print(f"PI: {PI}")
    print(f"Velocidad de la luz: {VELOCIDAD_LUZ} m/s")
    print(f"Gravedad terrestre: {GRAVEDAD_TERRESTRE} m/s²")
    print(f"Máximo de intentos: {MAX_INTENTOS}")
    print(f"Tiempo de espera: {TIEMPO_ESPERA} segundos")

if __name__ == "__main__":
    imprimir_constantes()
