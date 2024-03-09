class TDevice:
    def __init__(self, tamaño, peso, altura, marca):
        self.tamaño = tamaño
        self.peso = peso
        self.altura = altura
        self.marca = marca
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("El dispositivo se ha encendido.")
        else:
            print("El dispositivo ya está encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("El dispositivo se ha apagado.")
        else:
            print("El dispositivo ya está apagado.")

mi_dispositivo = TDevice(tamaño="Pequeño", peso="100g", altura="10cm", marca="MarcaX")
mi_dispositivo.encender()  # Encender el dispositivo
mi_dispositivo.apagar()   # Apagar el dispositivo
mi_dispositivo.apagar()   # Intentar apagar un dispositivo ya apagado




