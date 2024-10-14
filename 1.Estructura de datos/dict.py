# Registro de empleados
empleados = {
    "E001": {"nombre": "Ana Pérez", "edad": 30, "departamento": "Ventas"},
    "E002": {"nombre": "Luis Gómez", "edad": 25, "departamento": "Marketing"},
    "E003": {"nombre": "María López", "edad": 28, "departamento": "Desarrollo"}
}

# Agregar un nuevo empleado
empleados["E004"] = {"nombre": "Carlos Ruiz", "edad": 35, "departamento": "Recursos Humanos"}
print("Empleados después de agregar:", empleados)

# Actualizar información de un empleado
empleados["E002"]["edad"] = 26
print(f"Edad actualizada de E002: {empleados['E002']['edad']} años")

# Iterar sobre los empleados
print("Lista de empleados:")
for codigo, info in empleados.items():
    print(f"Código: {codigo}, Nombre: {info['nombre']}, Departamento: {info['departamento']}")
# Salida:
# Lista de empleados:
# Código: E001, Nombre: Ana Pérez, Departamento: Ventas
# Código: E002, Nombre: Luis Gómez, Departamento: Marketing
# Código: E003, Nombre: María López, Departamento: Desarrollo
# Código: E004, Nombre: Carlos Ruiz, Departamento: Recursos Humanos
