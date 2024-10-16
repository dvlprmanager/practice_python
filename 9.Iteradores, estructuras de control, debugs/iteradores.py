# Ejemplo de un iterador personalizado
class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual > self.fin:
            raise StopIteration
        numero = self.actual
        self.actual += 1
        return numero

# Uso del iterador
def usar_iterador():
    contador = Contador(1, 5)
    for num in contador:
        print(num)

# Ejemplo de generador
def generador_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def usar_generador():
    pares = generador_pares(10)
    for par in pares:
        print(par)

if __name__ == "__main__":
    print("Usando Iterador Personalizado:")
    usar_iterador()
    print("\nUsando Generador:")
    usar_generador()
