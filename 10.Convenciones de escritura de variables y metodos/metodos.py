class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""
    
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado
    
    def depositar(self, cantidad):
        """Método para depositar dinero en la cuenta."""
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depositados {cantidad}€. Nuevo saldo: {self.__saldo}€.")
        else:
            print("Cantidad a depositar debe ser positiva.")
    
    def retirar(self, cantidad):
        """Método para retirar dinero de la cuenta."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retirados {cantidad}€. Nuevo saldo: {self.__saldo}€.")
        elif cantidad > self.__saldo:
            print("Fondos insuficientes.")
        else:
            print("Cantidad a retirar debe ser positiva.")
    
    def obtener_saldo(self):
        """Método para obtener el saldo actual."""
        return self.__saldo
    
    def __str__(self):
        """Método especial para representar la cuenta como una cadena."""
        return f"CuentaBancaria(titular={self.titular}, saldo={self.__saldo}€)"
    
def ejecutar_metodos():
    cuenta = CuentaBancaria("Ana Pérez")
    print(cuenta)
    
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.retirar(400)
    
    print(f"Saldo final: {cuenta.obtener_saldo()}€")
    print(cuenta)

if __name__ == "__main__":
    ejecutar_metodos()
