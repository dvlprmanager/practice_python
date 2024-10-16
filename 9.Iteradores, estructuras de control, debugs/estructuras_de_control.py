def condicionales():
    edad = 20
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

def bucle_for():
    frutas = ["manzana", "banana", "cereza"]
    for fruta in frutas:
        print(f"Me gusta la {fruta}.")

def bucle_while():
    contador = 0
    while contador < 5:
        print(f"Contador: {contador}")
        contador += 1

def bucle_break_continue():
    for num in range(10):
        if num == 3:
            continue  # Salta el resto del código en este ciclo
        if num == 7:
            break     # Sale del bucle
        print(num)

if __name__ == "__main__":
    print("Condicionales:")
    condicionales()
    print("\nBucle For:")
    bucle_for()
    print("\nBucle While:")
    bucle_while()
    print("\nBucle For con Break y Continue:")
    bucle_break_continue()
