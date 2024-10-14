# Implementación de una pila usando una lista
historial = []

# Función para visitar una nueva página
def visitar_pagina(pagina):
    historial.append(pagina)
    print(f"Visitando: {pagina}")

# Función para retroceder en el historial
def retroceder():
    if historial:
        pagina = historial.pop()
        print(f"Regresando de: {pagina}")
    else:
        print("No hay páginas en el historial.")

# Simulación de navegación
visitar_pagina("https://www.google.com")
visitar_pagina("https://www.github.com")
visitar_pagina("https://www.python.org")
retroceder()  # Regresa de "https://www.python.org"
retroceder()  # Regresa de "https://www.github.com"
retroceder()  # Regresa de "https://www.google.com"
retroceder()  # No hay páginas en el historial
