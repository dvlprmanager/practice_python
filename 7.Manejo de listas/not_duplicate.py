# Lista con nombres de participantes que pueden estar duplicados
participantes = ["Ana", "Luis", "María", "Ana", "Carlos", "Luis", "María"]

# Convertir a conjunto para eliminar duplicados
participantes_unicos = set(participantes)
print("Participantes únicos:", participantes_unicos)
# Salida: Participantes únicos: {'María', 'Carlos', 'Ana', 'Luis'}

# Si se necesita mantener el orden, se puede usar una lista con comprensión
participantes_unicos_ordenados = []
seen = set()
for participante in participantes:
    if participante not in seen:
        participantes_unicos_ordenados.append(participante)
        seen.add(participante)

print("Participantes únicos y ordenados:", participantes_unicos_ordenados)
# Salida: Participantes únicos y ordenados: ['Ana', 'Luis', 'María', 'Carlos']
