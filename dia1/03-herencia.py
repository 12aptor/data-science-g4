class Persona:
    def __init__(self, nombre,dni,email):
        self.nombre = nombre
        self.dni = dni 
        self.email = email
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"DNI: {self.dni}")
        print(f"Email: {self.email}")
        
class Alumno(Persona):
    
    def calificar(self, nota):
        self.calificacion = nota
        print(f"Calificación del alumno: {self.calificacion}")

class Profesor(Persona):
    
    def asignar_curso(self, curso):
        self.curso = curso
        print(f"Curso asignado para el profesor : {self.curso}")

alumno1 = Alumno("Juan Perez","78787878","juan@gmail.com")
alumno1.mostrar()
alumno1.calificar(10)

profesor1 = Profesor("Maria Lopez","12345678","maria@gmail.com")
profesor1.mostrar()
profesor1.asignar_curso("Matemáticas")