import json

# Supongamos que recibimos la siguiente respuesta JSON de una API:
respuesta_json = '''
{
    "usuarios": [
        {"id": 1, "nombre": "Ana", "email": "ana@example.com"},
        {"id": 2, "nombre": "Luis", "email": "luis@example.com"},
        {"id": 3, "nombre": "María", "email": "maria@example.com"}
    ]
}
'''

# Convertir el JSON a un diccionario de Python
datos = json.loads(respuesta_json)

# Acceder a los datos
usuarios = datos["usuarios"]
print("Lista de usuarios:")
for usuario in usuarios:
    print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Email: {usuario['email']}")

# Agregar un nuevo usuario
nuevo_usuario = {"id": 4, "nombre": "Carlos", "email": "carlos@example.com"}
usuarios.append(nuevo_usuario)
print("\nUsuarios después de agregar uno nuevo:")
for usuario in usuarios:
    print(usuario)

# Convertir de vuelta a JSON
nueva_respuesta_json = json.dumps(datos, indent=4)
print("\nNueva respuesta JSON:")
print(nueva_respuesta_json)
