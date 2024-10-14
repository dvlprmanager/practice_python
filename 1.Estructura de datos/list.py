# Lista inicial de tareas
tareas = ["Comprar alimentos", "Llamar al médico", "Enviar correos electrónicos"]

# Agregar una nueva tarea
tareas.append("Leer un libro")
print("Tareas después de agregar:", tareas)
# Salida: Tareas después de agregar: ['Comprar alimentos', 'Llamar al médico', 'Enviar correos electrónicos', 'Leer un libro']

# Marcar una tarea como completada (eliminar de la lista)
tarea_completada = tareas.pop(1)
print(f"Tarea completada: {tarea_completada}")
print("Tareas restantes:", tareas)
# Salida:
# Tarea completada: Llamar al médico
# Tareas restantes: ['Comprar alimentos', 'Enviar correos electrónicos', 'Leer un libro']

# Iterar sobre las tareas
print("Lista de tareas:")
for tarea in tareas:
    print(f"- {tarea}")
# Salida:
# Lista de tareas:
# - Comprar alimentos
# - Enviar correos electrónicos
# - Leer un libro
