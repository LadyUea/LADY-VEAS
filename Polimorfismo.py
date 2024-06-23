# Definición de la clase base Figura
class Figura:
    def area(self):
        pass

# Definición de la clase Rectangulo que hereda de Figura
class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Implementación del método area para un rectángulo
    def area(self):
        return self.ancho * self.alto

# Definición de la clase Circulo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    # Implementación del método area para un círculo
    def area(self):
        return 3.14 * self.radio ** 2

# Uso de las clases
figuras = [Rectangulo(2, 3), Circulo(5)]

# Iteramos sobre la lista de figuras y llamamos al método area de cada una
for figura in figuras:
    print(figura.area())