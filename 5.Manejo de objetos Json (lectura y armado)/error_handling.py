import json

def leer_archivo_inexistente(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' tiene un formato JSON inválido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def leer_json_invalido(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' contiene JSON inválido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
