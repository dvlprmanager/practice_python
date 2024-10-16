import pandas as pd

# Escribir en un archivo
# Abre (o crea si no existe) un archivo llamado 'ejemplo.txt' en modo escritura ('w')
with open('ejemplo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('¡Hola, mundo!\n')
    archivo.write('Esta es una línea de texto.\n')
    archivo.write('Python facilita la manipulación de archivos.\n')

print("Escritura completada.")

# Leer de un archivo
# Abre el archivo 'ejemplo.txt' en modo lectura ('r')
with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()

print("\nContenido del archivo:")
print(contenido)

# Especifica la ruta al archivo de Excel
archivo_excel = 'datos.xlsx'

# Lee el archivo de Excel
df = pd.read_excel(archivo_excel)

# Muestra las primeras filas de DataFrame

print(df.head())

