class Persona:
    """Clase base que representa una persona."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Empleado(Persona):
    """Clase derivada que representa a un empleado, hereda de Persona."""
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y trabajo como {self.puesto}."

class Estudiante(Persona):
    """Clase derivada que representa a un estudiante, hereda de Persona."""
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def saludar(self):
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."

def ejecutar_clases():
    persona = Persona("Luis", 40)
    empleado = Empleado("Marta", 30, "Ingeniera")
    estudiante = Estudiante("Sofía", 20, "Arquitectura")

    print(persona.saludar())
    print(empleado.saludar())
    print(estudiante.saludar())

if __name__ == "__main__":
    ejecutar_clases()
