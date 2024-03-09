# Instanciación de la clase Policia
from PIA.D import TPersona
from PIA.E import Administrador, Bombero, Policia
from PIA.F import TEmpleado


persona1 = TPersona(nombre="Carlos", edad=35, altura=180, peso=80, ocupacion="Empleado")
policia1 = Policia(persona1, rango="Sargento")
empleado_policia1 = TEmpleado(policia1, "policía")

persona2 = TPersona(nombre="Laura", edad=40, altura=170, peso=75, ocupacion="Empleado")
policia2 = Policia(persona2, rango="Oficial")
empleado_policia2 = TEmpleado(policia2, "policía")

# Instanciación de la clase Administrador
admin1 = Administrador(persona1, departamento="Recursos Humanos")
empleado_admin1 = TEmpleado(admin1, "administrador")

admin2 = Administrador(persona2, departamento="Finanzas")
empleado_admin2 = TEmpleado(admin2, "administrador")

# Instanciación de la clase Bombero
bombero1 = Bombero(persona1, estacion="Estación Central")
empleado_bombero1 = TEmpleado(bombero1, "bombero")

bombero2 = Bombero(persona2, estacion="Estación Norte")
empleado_bombero2 = TEmpleado(bombero2, "bombero")

# Mostrar información
empleado_policia1.presentarse()
empleado_policia2.presentarse()

empleado_admin1.presentarse()
empleado_admin2.presentarse()

empleado_bombero1.presentarse()
empleado_bombero2.presentarse()
