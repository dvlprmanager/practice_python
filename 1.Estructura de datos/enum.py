from enum import Enum

# Definir los posibles estados de una orden
class EstadoOrden(Enum):
    PENDIENTE = 1
    PROCESANDO = 2
    ENVIADO = 3
    ENTREGADO = 4
    CANCELADO = 5

# Clase Orden
class Orden:
    def __init__(self, id_orden, producto, estado=EstadoOrden.PENDIENTE):
        self.id_orden = id_orden
        self.producto = producto
        self.estado = estado

    def actualizar_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, EstadoOrden):
            self.estado = nuevo_estado
            print(f"Orden {self.id_orden} actualizada a {self.estado.name}.")
        else:
            print("Estado inválido.")

# Crear una orden
orden1 = Orden("ORD1001", "Laptop")

# Actualizar el estado de la orden
orden1.actualizar_estado(EstadoOrden.PROCESANDO)
orden1.actualizar_estado(EstadoOrden.ENVIADO)
orden1.actualizar_estado(EstadoOrden.ENTREGADO)
# Salida:
# Orden ORD1001 actualizada a PROCESANDO.
# Orden ORD1001 actualizada a ENVIADO.
# Orden ORD1001 actualizada a ENTREGADO.
