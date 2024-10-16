import json

def modificar_persona(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            persona = json.loads(file)
        
        #Modificar edad
        persona["edad"] = 26

        #Agregar un nuevo interes
        persona["intereses"].append('fotografia')

        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            json.dump(persona, file, indent=4, ensure_ascii=False)

        print(f"Datos actualizados en '{nombre_archivo}'.")
        return persona
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' tiene un formato JSON inválido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")