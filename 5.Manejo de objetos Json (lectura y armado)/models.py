from datetime import datetime

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __repr__(self):
        return f"Estudiante(nombre={self.nombre}, edad={self.edad}, carrera={self.carrera})"