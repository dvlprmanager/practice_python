import json

def leer_json(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(f"Datos leídos desde '{nombre_archivo}':")
    print(data)
    return data