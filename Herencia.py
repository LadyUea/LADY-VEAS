# Definición de la clase base Vehiculo
class Vehiculo:
    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método que devuelve una descripción del vehículo
    def descripcion(self):
        return f"{self.marca} {self.modelo}"

# Definición de la clase derivada Coche que hereda de Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamada al constructor de la clase base
        super()._init_(marca, modelo)
        self.puertas = puertas

    # Sobrescritura del método descripcion para incluir el número de puertas
    def descripcion(self):
        return f"{super().descripcion()} con {self.puertas} puertas"

# Uso de las clases
coche = Coche("Hyundai", "Gran i10", 5)
print(coche.descripcion())# Output: Hyundai Gran i10 con 5 puertas