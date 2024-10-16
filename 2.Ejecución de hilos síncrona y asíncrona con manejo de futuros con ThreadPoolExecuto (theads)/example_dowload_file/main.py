from downloader import descarga_sincrona, descarga_asincrona

def main():
    # Lista de archivos a descargar: (nombre_archivo, tiempo_descarga en segundos)
    archivos = [
        ("archivo1.zip", 3),
        ("archivo2.zip", 2),
        ("archivo3.zip", 5),
        ("archivo4.zip", 1),
    ]

    print("=== Descarga Síncrona ===")
    resultados_sync = descarga_sincrona(archivos)
    for res in resultados_sync:
        print(res)

    print("\n=== Descarga Asíncrona ===")
    resultados_async = descarga_asincrona(archivos, max_workers=3)
    for res in resultados_async:
        print(res)

if __name__ == "__main__":
    main()
