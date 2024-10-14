import requests
import json

# URL base de la API JSONPlaceholder
BASE_URL = "https://jsonplaceholder.typicode.com"

def obtener_publicaciones():
    """
    Obtiene una lista de publicaciones.
    """
    url = f"{BASE_URL}/posts"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción para códigos de error HTTP
        publicaciones = respuesta.json()
        print(f"Se obtuvieron {len(publicaciones)} publicaciones.")
        return publicaciones
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")

def obtener_publicacion(id_publicacion):
    """
    Obtiene una publicación específica por ID.
    """
    url = f"{BASE_URL}/posts/{id_publicacion}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        publicacion = respuesta.json()
        print(f"\nPublicación {id_publicacion}:")
        print(json.dumps(publicacion, indent=4))
        return publicacion
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")

def crear_publicacion(titulo, cuerpo, user_id):
    """
    Crea una nueva publicación.
    """
    url = f"{BASE_URL}/posts"
    payload = {
        "title": titulo,
        "body": cuerpo,
        "userId": user_id
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    try:
        respuesta = requests.post(url, data=json.dumps(payload), headers=headers)
        respuesta.raise_for_status()
        publicacion_creada = respuesta.json()
        print("\nPublicación creada:")
        print(json.dumps(publicacion_creada, indent=4))
        return publicacion_creada
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")

def actualizar_publicacion(id_publicacion, titulo=None, cuerpo=None, user_id=None):
    """
    Actualiza una publicación existente.
    """
    url = f"{BASE_URL}/posts/{id_publicacion}"
    payload = {}
    if titulo:
        payload["title"] = titulo
    if cuerpo:
        payload["body"] = cuerpo
    if user_id:
        payload["userId"] = user_id
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    try:
        respuesta = requests.put(url, data=json.dumps(payload), headers=headers)
        respuesta.raise_for_status()
        publicacion_actualizada = respuesta.json()
        print("\nPublicación actualizada:")
        print(json.dumps(publicacion_actualizada, indent=4))
        return publicacion_actualizada
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")

def eliminar_publicacion(id_publicacion):
    """
    Elimina una publicación por ID.
    """
    url = f"{BASE_URL}/posts/{id_publicacion}"
    try:
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print(f"\nPublicación {id_publicacion} eliminada correctamente.")
        else:
            print(f"\nNo se pudo eliminar la publicación {id_publicacion}. Estado: {respuesta.status_code}")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except Exception as err:
        print(f"Ocurrió un error: {err}")

def main():
    # Obtener todas las publicaciones
    publicaciones = obtener_publicaciones()
    
    # Obtener una publicación específica
    obtener_publicacion(1)
    
    # Crear una nueva publicación
    nueva_publicacion = crear_publicacion(
        titulo="Título de Prueba",
        cuerpo="Este es el cuerpo de la publicación de prueba.",
        user_id=1
    )
    
    # Actualizar la publicación creada
    if nueva_publicacion:
        actualizar_publicacion(
            id_publicacion=nueva_publicacion.get("id"),
            titulo="Título Actualizado",
            cuerpo="Este es el cuerpo actualizado de la publicación."
        )
    
    # Eliminar la publicación creada
    if nueva_publicacion:
        eliminar_publicacion(nueva_publicacion.get("id"))

if __name__ == "__main__":
    main()
