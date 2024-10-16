import requests
import json

def obtener_datos_api(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        print
        print("Datos obtenidos desde la API:")
        print(json.dumps(datos, indent=4, ensure_ascii=False))
        return datos
    
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error en la solicitud: {err}")
    except json.JSONDecodeError:
        print("Error: La respuesta no contiene un JSON válido.")