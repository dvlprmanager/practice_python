def listas():
    frutas = ["manzana", "banana", "cereza"]
    print("Lista original:", frutas)
    frutas.append("naranja")
    print("Después de append:", frutas)
    frutas.remove("banana")
    print("Después de remove:", frutas)
    print("Elemento en índice 1:", frutas[1])

def diccionarios():
    estudiante = {
        "nombre": "Juan",
        "edad": 21,
        "carrera": "Biología"
    }
    print("Diccionario original:", estudiante)
    estudiante["edad"] = 22
    print("Después de actualizar edad:", estudiante)
    estudiante["universidad"] = "Universidad de Madrid"
    print("Después de agregar universidad:", estudiante)
    print("Valor de 'nombre':", estudiante.get("nombre"))

def conjuntos():
    numeros = {1, 2, 3, 4, 4, 5}
    print("Conjunto original (sin duplicados):", numeros)
    numeros.add(6)
    print("Después de add:", numeros)
    numeros.remove(3)
    print("Después de remove:", numeros)
    otros_numeros = {5, 6, 7, 8}
    union = numeros.union(otros_numeros)
    print("Unión:", union)
    interseccion = numeros.intersection(otros_numeros)
    print("Intersección:", interseccion)

def tuplas():
    coordenadas = (10.0, 20.0)
    print("Tupla original:", coordenadas)
    print("Elemento en índice 0:", coordenadas[0])
    # Las tuplas son inmutables, intentar modificar generará un error
    # coordenadas[0] = 15.0  # Esto causará TypeError

def ejecutar_data_structures():
    print("Listas:")
    listas()
    print("\nDiccionarios:")
    diccionarios()
    print("\nConjuntos:")
    conjuntos()
    print("\nTuplas:")
    tuplas()

if __name__ == "__main__":
    ejecutar_data_structures()
