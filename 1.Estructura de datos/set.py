# Etiquetas para un artículo específico
etiquetas_articulo = {"Python", "Programación", "Tutorial"}

# Agregar nuevas etiquetas
etiquetas_articulo.add("Educación")
etiquetas_articulo.add("Python")  # Duplicado, no se añadirá
print("Etiquetas del artículo:", etiquetas_articulo)
# Salida: Etiquetas del artículo: {'Educación', 'Tutorial', 'Programación', 'Python'}

# Verificar si una etiqueta existe
if "Desarrollo" in etiquetas_articulo:
    print("La etiqueta 'Desarrollo' está presente.")
else:
    print("La etiqueta 'Desarrollo' no está presente.")
# Salida: La etiqueta 'Desarrollo' no está presente.

# Eliminar una etiqueta
etiquetas_articulo.remove("Tutorial")
print("Etiquetas después de eliminar 'Tutorial':", etiquetas_articulo)
# Salida: Etiquetas después de eliminar 'Tutorial': {'Educación', 'Programación', 'Python'}
