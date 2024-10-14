import json

# Crear un diccionario
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Barcelona",
    "intereses": ["leer", "cocinar", "arte"]
}

# Convertir el diccionario a JSON
json_data = json.dumps(persona, indent=4)

# Guardar el objeto JSON en un archivo
with open('persona.json', 'w') as file:
    file.write(json_data)

# Mostrar el objeto JSON
print(json_data)
