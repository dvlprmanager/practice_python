# clases.py

class Persona:
    """Clase que representa a una persona."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        """Método para saludar."""
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Empleado(Persona):
    """Clase que representa a un empleado, heredando de Persona."""
    
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto
    
    def saludar(self):
        """Método para saludar como empleado."""
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y trabajo como {self.puesto}."

def ejecutar_clases():
    persona = Persona("Luis", 28)
    empleado = Empleado("Marta", 35, "Ingeniera de Software")
    
    print(persona.saludar())
    print(empleado.saludar())

if __name__ == "__main__":
    ejecutar_clases()
