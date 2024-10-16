# Inventario inicial
inventario = [
    {"id": "P001", "nombre": "Laptop", "precio": 999.99, "stock": 10},
    {"id": "P002", "nombre": "Ratón", "precio": 25.50, "stock": 150},
    {"id": "P003", "nombre": "Teclado", "precio": 45.00, "stock": 80}
]

# Agregar un nuevo producto
nuevo_producto = {"id": "P004", "nombre": "Monitor", "precio": 150.00, "stock": 50}
inventario.append(nuevo_producto)
print("Inventario después de agregar:", inventario)

# Actualizar stock de un producto
for producto in inventario:
    if producto["id"] == "P002":
        producto["stock"] += 20  # Se reciben más ratones
        print(f"Nuevo stock de {producto['nombre']}: {producto['stock']} unidades")

# Eliminar un producto agotado
inventario = [producto for producto in inventario if producto["stock"] > 0]
print("Inventario después de eliminar productos sin stock:", inventario)

# Calcular el valor total del inventario
valor_total = sum(producto["precio"] * producto["stock"] for producto in inventario)
print(f"Valor total del inventario: ${valor_total:.2f}")
# Salida:
# Valor total del inventario: $9999.90
