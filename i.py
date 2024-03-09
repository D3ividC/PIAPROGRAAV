from pia.h import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, curso):
        super().__init__(nombre, edad, genero)
        self.curso = curso

    def estudiar(self):
        print(f"Soy {self.nombre} y estoy estudiando el curso de {self.curso}.")

# Ejemplo de uso
estudiante1 = Estudiante("Carlos", 20, "Masculino", "Matemáticas")
estudiante1.presentarse()
estudiante1.estudiar()

estudiante2 = Estudiante("Ana", 22, "Femenino", "Historia")
estudiante2.presentarse()
estudiante2.estudiar()
