# Lista de estudiantes con calificaciones
estudiantes = [
    {"nombre": "Ana", "calificacion": 85},
    {"nombre": "Luis", "calificacion": 58},
    {"nombre": "María", "calificacion": 72},
    {"nombre": "Carlos", "calificacion": 49},
    {"nombre": "Elena", "calificacion": 90}
]

# Obtener nombres de estudiantes aprobados usando lista por comprensión
aprobados = [est["nombre"] for est in estudiantes if est["calificacion"] >= 60]
print("Estudiantes aprobados:", aprobados)
# Salida: Estudiantes aprobados: ['Ana', 'María', 'Elena']
