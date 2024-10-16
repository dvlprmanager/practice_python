import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def descargar_archivo(nombre_archivo, tiempo_descarga):
    """
    Simula la descarga de un archivo.

    Args:
        nombre_archivo (str): Nombre del archivo a descargar.
        tiempo_descarga (int): Tiempo en segundos que tarda la descarga.

    Returns:
        str: Mensaje indicando la finalización de la descarga.
    """
    print(f"Iniciando descarga de {nombre_archivo}...")
    time.sleep(tiempo_descarga)  # Simula el tiempo de descarga
    print(f"Descarga de {nombre_archivo} completada.")
    return f"{nombre_archivo} descargado en {tiempo_descarga} segundos."

def descarga_sincrona(archivos):
    """
    Descarga archivos de manera síncrona.

    Args:
        archivos (list): Lista de tuplas con (nombre_archivo, tiempo_descarga).

    Returns:
        list: Lista de mensajes de descarga completada.
    """
    resultados = []
    inicio = time.time()

    for archivo, tiempo in archivos:
        resultado = descargar_archivo(archivo, tiempo)
        resultados.append(resultado)

    fin = time.time()
    print(f"\nDescarga síncrona completada en {fin - inicio:.2f} segundos.\n")
    return resultados

def descarga_asincrona(archivos, max_workers=3):
    """
    Descarga archivos de manera asíncrona utilizando ThreadPoolExecutor.

    Args:
        archivos (list): Lista de tuplas con (nombre_archivo, tiempo_descarga).
        max_workers (int): Número máximo de hilos a utilizar.

    Returns:
        list: Lista de mensajes de descarga completada.
    """
    resultados = []
    inicio = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
       
        futuros = {executor.submit(descargar_archivo, archivo, tiempo): archivo for archivo, tiempo in archivos}

        for futuro in as_completed(futuros):
            archivo = futuros[futuro]
            try:
                resultado = futuro.result()
                resultados.append(resultado)
            except Exception as e:
                print(f"Error al descargar {archivo}: {e}")

    fin = time.time()
    print(f"\nDescarga asíncrona completada en {fin - inicio:.2f} segundos.\n")
    return resultados
