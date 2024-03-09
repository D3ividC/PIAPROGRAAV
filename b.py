from PIA.A import TDevice


class TV(TDevice):
    def __init__(self, tamaño, peso, altura, marca, pulgadas):
        super().__init__(tamaño, peso, altura, marca)
        self.pulgadas = pulgadas

    def cambiar_canal(self, canal):
        print(f"Cambiando al canal {canal}")

    def ajustar_volumen(self, nivel):
        print(f"Ajustando el volumen al nivel {nivel}")

    def reproducir_pelicula(self, pelicula):
        print(f"Reproduciendo la película: {pelicula}")


class Licuadora(TDevice):
    def __init__(self, tamaño, peso, altura, marca, capacidad):
        super().__init__(tamaño, peso, altura, marca)
        self.capacidad = capacidad

    def mezclar(self, ingredientes):
        print(f"Mezclando los ingredientes: {ingredientes}")

    def triturar_hielo(self):
        print("Triturando hielo")

    def hacer_batido(self, fruta):
        print(f"Haciendo un batido de {fruta}")


class Celular(TDevice):
    def __init__(self, tamaño, peso, altura, marca, modelo):
        super().__init__(tamaño, peso, altura, marca)
        self.modelo = modelo

    def llamar(self, numero):
        print(f"Llamando al número: {numero}")

    def enviar_mensaje(self, contacto, mensaje):
        print(f"Enviando mensaje a {contacto}: {mensaje}")

    def tomar_foto(self):
        print("Tomando una foto")

# Ejemplos de uso
mi_tv = TV(tamaño="Grande", peso="5kg", altura="50cm", marca="Samsung", pulgadas=55)
mi_tv.encender()
mi_tv.cambiar_canal(5)
mi_tv.apagar()

mi_licuadora = Licuadora(tamaño="Mediano", peso="2kg", altura="30cm", marca="Oster", capacidad="1.5 litros")
mi_licuadora.encender()
mi_licuadora.triturar_hielo()
mi_licuadora.apagar()

mi_celular = Celular(tamaño="Pequeño", peso="150g", altura="15cm", marca="Apple", modelo="iPhone 12")
mi_celular.encender()
mi_celular.llamar("123456789")
mi_celular.enviar_mensaje("Amigo", "Hola, ¿cómo estás?")
mi_celular.apagar()
