from PIA.D import TPersona
from PIA.E import Administrador, Bombero, Policia


class TEmpleado:
    def __init__(self, persona, rol):
        self.persona = persona
        self.rol = rol

    def presentarse(self):
        print(f"Soy {self.persona.nombre}, un {self.rol}.")

persona_juan = TPersona(nombre="Juan", edad=30, altura=170, peso=70, ocupacion="Empleado")
policia_juan = Policia(persona_juan, rango="Sargento")
admin_juan = Administrador(persona_juan, departamento="Recursos Humanos")
bombero_juan = Bombero(persona_juan, estacion="Estación Central")

empleado_policia = TEmpleado(policia_juan, "policía")
empleado_admin = TEmpleado(admin_juan, "administrador")
empleado_bombero = TEmpleado(bombero_juan, "bombero")

empleado_policia.presentarse()
empleado_admin.presentarse()
empleado_bombero.presentarse()
