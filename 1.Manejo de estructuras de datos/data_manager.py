import pandas as pd
import matplotlib.pyplot as plt

# Datos de ventas
datos = {
    "Producto": ["Laptop", "Ratón", "Teclado", "Monitor"],
    "Ventas_Q1": [150, 300, 200, 100],
    "Ventas_Q2": [200, 350, 250, 150],
    "Ventas_Q3": [180, 330, 220, 130],
    "Ventas_Q4": [210, 400, 260, 170]
}

try:
    # Crear un DataFrame
    df = pd.DataFrame(datos)
    print("DataFrame de ventas:")
    print(df)

    # Calcular ventas totales por producto
    df["Ventas_Totales"] = df[["Ventas_Q1", "Ventas_Q2", "Ventas_Q3", "Ventas_Q4"]].sum(axis=1)
    print("\nVentas totales por producto:")
    print(df[["Producto", "Ventas_Totales"]])

    # Filtrar productos con ventas totales superiores a 800
    productos_exitosos = df[df["Ventas_Totales"] > 800]
    print("\nProductos con ventas totales superiores a 800:")
    print(productos_exitosos)

    # Visualizar las ventas trimestrales
    df.set_index("Producto")[["Ventas_Q1", "Ventas_Q2", "Ventas_Q3", "Ventas_Q4"]].plot(kind="bar")
    plt.title("Ventas Trimestrales por Producto")
    plt.xlabel("Producto")
    plt.ylabel("Ventas")
    plt.tight_layout()  # Ajusta el layout para evitar recortes
    plt.show()

except ImportError as ie:
    print("Error de importación:", ie)
except KeyError as ke:
    print("Error de clave:", ke)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
