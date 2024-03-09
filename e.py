from PIA.D import TPersona


class Policia(TPersona):
    def __init__(self, nombre, edad, altura, peso, rango):
        super().__init__(nombre, edad, altura, peso, ocupacion="Policía")
        self.rango = rango

    def mostrar_rango(self):
        print(f"Soy {self.nombre}, un policía de rango {self.rango}.")


class Administrador(TPersona):
    def __init__(self, nombre, edad, altura, peso, departamento):
        super().__init__(nombre, edad, altura, peso, ocupacion="Administrador")
        self.departamento = departamento

    def mostrar_departamento(self):
        print(f"Soy {self.nombre}, un administrador del departamento {self.departamento}.")


class Bombero(TPersona):
    def __init__(self, nombre, edad, altura, peso, estacion):
        super().__init__(nombre, edad, altura, peso, ocupacion="Bombero")
        self.estacion = estacion

    def mostrar_estacion(self):
        print(f"Soy {self.nombre}, un bombero de la estación {self.estacion}.")


policia1 = Policia(nombre="Carlos", edad=35, altura=180, peso=80, rango="Sargento")
policia1.presentarse()
policia1.mostrar_rango()

admin1 = Administrador(nombre="Ana", edad=40, altura=165, peso=70, departamento="Recursos Humanos")
admin1.presentarse()
admin1.mostrar_departamento()

bombero1 = Bombero(nombre="David", edad=28, altura=175, peso=75, estacion="Estación Central")
bombero1.presentarse()
bombero1.mostrar_estacion()
