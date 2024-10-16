from data_creation import ( 
    crear_persona,
    guardar_json,
    crear_lista_personas,
    crear_evento
)
from data_reading import leer_json
from data_modification import modificar_persona
from error_handling import (
    leer_archivo_inexistente,
    leer_json_invalido
)
from custom_encoder import serializar_objeto
from api_example import obtener_datos_api

def main():

    # Paso 1: Crear y guardar un diccionario como JSON
    persona = crear_persona()
    guardar_json(persona, 'persona.json')
    
    # Paso 2: Leer el JSON desde el archivo
    persona_leida = leer_json('persona.json')
    
    # Paso 3: Modificar los datos del JSON
    persona_modificada = modificar_persona('persona.json')
    
    # Paso 4: Manejar excepciones al intentar leer un archivo inexistente
    leer_archivo_inexistente('datos_inexistentes.json')
    
    # Paso 5: Serializar un objeto complejo usando un codificador personalizado
    evento = crear_evento()
    evento_json = serializar_objeto(evento)
    print("Evento serializado con CustomEncoder:")
    print(evento_json)
    
    # Guardar el evento serializado en un archivo
    with open('evento.json', 'w', encoding='utf-8') as file:
        file.write(evento_json)
    print("Evento guardado en 'evento.json'.")
    
    # Paso 6: Obtener y procesar datos desde una API
    url_api = "https://jsonplaceholder.typicode.com/users/1"
    obtener_datos_api(url_api)
    
    # Paso 7: Crear y guardar una lista de personas
    personas = crear_lista_personas()
    guardar_json(personas, 'personas.json')
    
    # Leer la lista de personas desde el archivo
    personas_leidas = leer_json('personas.json')

if __name__ == "__main__":
    main()