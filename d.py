class TPersona:
    def __init__(self, nombre, edad, altura, peso, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.ocupacion = ocupacion

    def presentarse(self):
        print(f"¡Hola! Mi nombre es {self.nombre}. Tengo {self.edad} años.")

    def crecer(self, aumento_altura):
        self.altura += aumento_altura
        print(f"Después de crecer {aumento_altura} centímetros, mi altura es ahora de {self.altura} cm.")

    def engordar(self, aumento_peso):
        self.peso += aumento_peso
        print(f"He aumentado {aumento_peso} kilogramos. Mi peso actual es de {self.peso} kg.")

    def adelgazar(self, disminucion_peso):
        self.peso -= disminucion_peso
        print(f"He perdido {disminucion_peso} kilogramos. Mi peso actual es de {self.peso} kg.")

    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"Mi nueva ocupación es {self.ocupacion}.")


persona1 = TPersona(nombre="Juan", edad=30, altura=170, peso=70, ocupacion="Ingeniero")
persona1.presentarse()
persona1.crecer(5)
persona1.engordar(3)
persona1.adelgazar(2)
persona1.cambiar_ocupacion("Doctor")

persona2 = TPersona(nombre="María", edad=25, altura=165, peso=60, ocupacion="Abogada")
persona2.presentarse()
persona2.crecer(3)
persona2.engordar(2)
persona2.adelgazar(1)
persona2.cambiar_ocupacion("Profesora")
