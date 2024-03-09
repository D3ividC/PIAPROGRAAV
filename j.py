class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

rectangulo1 = Rectangulo(5, 3)
print("El área del rectángulo es:", rectangulo1.area())

rectangulo2 = Rectangulo(7, 4)
print("El área del rectángulo es:", rectangulo2.area())
