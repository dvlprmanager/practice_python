# Coordenadas de una tienda
coordenadas_tienda = (40.7128, -74.0060)  # (latitud, longitud)

# Función para calcular la distancia aproximada (simplificada)
def calcular_distancia(coord1, coord2):
    lat_diff = coord2[0] - coord1[0]
    lon_diff = coord2[1] - coord1[1]
    return (lat_diff**2 + lon_diff**2) ** 0.5

# Coordenadas del usuario
coordenadas_usuario = (40.730610, -73.935242)

# Calcular distancia
distancia = calcular_distancia(coordenadas_usuario, coordenadas_tienda)
print(f"Distancia aproximada: {distancia:.2f} unidades")
# Salida: Distancia aproximada: 0.07 unidades
