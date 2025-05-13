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
    
    calificacion = 0
    
    def calificar(self, nota):
        self.calificacion = nota
        print(f"Calificación del alumno: {self.calificacion}")
        
    def mostrar(self):
        print("============= DATOS DEL ALUMNO =============")
        super().mostrar()
        print("NOTA DEL ALUMNO: ", self.calificacion)
        print("=============================================")

class Profesor(Persona):
    
    curso = ""
    
    def asignar_curso(self, curso):
        self.curso = curso
        print(f"Curso asignado para el profesor : {self.curso}")
        
    def mostrar(self):
        print("============= DATOS DEL PROFESOR =============")
        super().mostrar()
        print("CURSO A DICTAR : ", self.curso)
        print("=============================================")

alumno1 = Alumno("Juan Perez","78787878","juan@gmail.com")
alumno1.calificar(20)
alumno1.mostrar()

profesor1 = Profesor("Maria Lopez","12345678","maria@gmail.com")
profesor1.asignar_curso("Matemáticas")
profesor1.mostrar()