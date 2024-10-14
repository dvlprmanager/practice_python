from collections import defaultdict

# Lista de ventas con categorías
ventas = [
    {"producto": "Laptop", "categoria": "Electrónica", "cantidad": 5},
    {"producto": "Ratón", "categoria": "Electrónica", "cantidad": 15},
    {"producto": "Camiseta", "categoria": "Ropa", "cantidad": 20},
    {"producto": "Jeans", "categoria": "Ropa", "cantidad": 10},
    {"producto": "Monitor", "categoria": "Electrónica", "cantidad": 7}
]

# Agrupar ventas por categoría
ventas_por_categoria = defaultdict(int)
for venta in ventas:
    ventas_por_categoria[venta["categoria"]] += venta["cantidad"]

print("Ventas por categoría:")
for categoria, total in ventas_por_categoria.items():
    print(f"{categoria}: {total} unidades")
# Salida:
# Ventas por categoría:
# Electrónica: 27 unidades
# Ropa: 30 unidades
