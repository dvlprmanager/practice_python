# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

# Crear instancias de libros
libro1 = Libro("1984", "George Orwell", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "0987654321")

# Prestar un libro
libro1.prestar()
# Intentar prestar nuevamente
libro1.prestar()

# Devolver el libro
libro1.devolver()

# Verificar disponibilidad
libro1.prestar()
