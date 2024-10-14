import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print("Librería 'requests' instalada correctamente.")
    print("Respuesta de la API:", response.json())
else:
    print("Error al realizar la solicitud.")
