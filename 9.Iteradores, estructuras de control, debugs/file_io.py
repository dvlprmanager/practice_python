def escribir_archivo(nombre_archivo, contenido):
    """Escribe contenido en un archivo."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as file:
            file.write(contenido)
        print(f"Contenido escrito en '{nombre_archivo}'.")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

def leer_archivo(nombre_archivo):
    """Lee y devuelve el contenido de un archivo."""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
        print(f"Contenido leído de '{nombre_archivo}':")
        print(contenido)
        return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

def ejecutar_file_io():
    nombre = "ejemplo.txt"
    contenido = "Hola, este es un ejemplo de escritura y lectura de archivos en Python.\nSegunda línea del archivo."

    escribir_archivo(nombre, contenido)
    print()
    leer_archivo(nombre)

if __name__ == "__main__":
    ejecutar_file_io()
