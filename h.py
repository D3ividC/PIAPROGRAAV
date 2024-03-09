class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 30, "Masculino")
persona1.presentarse()

persona2 = Persona("María", 25, "Femenino")
persona2.presentarse()
