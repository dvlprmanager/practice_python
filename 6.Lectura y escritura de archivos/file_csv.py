import csv

# Supongamos que tenemos un archivo 'estudiantes.csv' con el siguiente contenido:
# nombre,edad,grado
# Ana,20,3
# Luis,22,4
# María,19,2

# Leer el archivo CSV y almacenar los datos en una lista de diccionarios
estudiantes = []
with open('estudiantes.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        estudiantes.append({
            "nombre": fila["nombre"],
            "edad": int(fila["edad"]),
            "grado": int(fila["grado"])
        })

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

# Calcular la edad promedio
edad_promedio = sum(estudiante["edad"] for estudiante in estudiantes) / len(estudiantes)
print(f"\nEdad promedio de los estudiantes: {edad_promedio:.2f} años")

# Filtrar estudiantes que están en el grado 3 o superior
estudiantes_grado3 = [est for est in estudiantes if est["grado"] >= 3]
print("\nEstudiantes en el grado 3 o superior:")
for est in estudiantes_grado3:
    print(est["nombre"])
