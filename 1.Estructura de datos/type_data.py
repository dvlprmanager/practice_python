#dato int

numero_entero = 10
numero_negativo = -5

edad = 25
años_experiencia = -3  # Puede representar, por ejemplo, años faltantes para un evento

#dato float
numero_flotante = 3.14
otro_flotante = -0.001

precio = 19.99
temperatura = -4.5

#dato Boolenaos

es_activo = True
tiene_acceso = False

es_mayor = edad > 18  # Devuelve True si edad es mayor que 18


#dato str cadena de texto

texto = "Hola, mundo"
texto_con_comillas_simples = 'Python es genial'


#Las cadenas pueden estar delimitadas por comillas simples (' ') o dobles (" ").
#Soportan caracteres de escape, como \n para nueva línea.

nombre = "Juan Pérez"
mensaje = 'Él dijo: "¡Hola!"'
multilinea = """Esta es una
cadena de múltiples
líneas"""


#dato lista simple

mi_lista = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

frutas = ["manzana", "banana", "cereza"]
frutas.append("naranja")  # Agrega "naranja" al final de la lista

#dato tuplas tuple

mi_tupla = (1, 2, 3)
tupla_mixta = (1, "dos", 3.0, False)


coordenadas = (10.0, 20.0)


#dato set

mi_set = {1, 2, 3, 4, 5}
set_mixto = {1, "dos", 3.0, True}


frutas_unicas = {"manzana", "banana", "cereza"}
frutas_unicas.add("naranja")  # Agrega "naranja" al conjunto

#dato dict Diccionarios

mi_diccionario = {"nombre": "Juan", "edad": 30}
diccionario_mixto = {"id": 1, "nombre": "Producto", "precio": 9.99}

persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}
print(persona["nombre"])  # Imprime "Ana"
persona["edad"] = 26  # Actualiza la edad a 26

#dato NoneType  (None)

variable_nula = None

resultado = None
# Más adelante en el código
if algun_evento:
    resultado = "Éxito"

#Bytes y Bytearrays

datos_bytes = b"Hola"

mensaje_bytes = b"Python es divertido"

#Bytearray 

datos_bytearray = bytearray(b"Hola")

#Enumeraciones (enum)

from enum import Enum

class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

#Clases

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Carlos", 28)

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto1 = Producto("Laptop", 999.99)




#Resumen de Declaraciones
#Tipo de Dato	Ejemplo de Declaración           	        Descripción
#int	            numero = 10	                                Números enteros
#float	        precio = 19.99	                            Números con decimales
#bool	        es_activo = True	                        Valores de verdad (True o False)
#str	            nombre = "Ana"	                            Cadenas de texto
#list	        frutas = ["manzana", "banana"]	            Listas ordenadas y mutables
#tuple	        coordenadas = (10.0, 20.0)	                Tuplas ordenadas e inmutables
#set	            frutas_unicas = {"manzana", "banana"}	    Conjuntos de elementos únicos
#dict	        persona = {"nombre": "Ana", "edad": 25}	    Diccionarios de pares clave-valor
#None	        variable_nula = None	                    Representa ausencia de valor
#bytes	        datos_bytes = b"Hola"	                    Secuencia inmutable de bytes
#bytearray	    datos_bytearray = bytearray(b"Hola")	    Secuencia mutable de bytes
#enum	        Color = Enum("Color", "ROJO VERDE AZUL")	Enumeraciones para constantes nombradas
#clase	        class Persona: ...	                        Tipos personalizados mediante clases
