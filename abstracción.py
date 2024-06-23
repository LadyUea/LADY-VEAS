from abc import ABC, abstractmethod
# Definición de una clase abstracta Animal
class Animal(ABC):
    # Método abstracto que debe ser implementado por cualquier clase derivada
    @abstractmethod
    def hacer_sonido(self):
        pass

# Clase Perro que hereda de Animal
class Perro(Animal):
    # Implementación del método abstracto hacer_sonido
    def hacer_sonido(self):
        return "Guau"

# Clase Gato que hereda de Animal
class Gato(Animal):
    # Implementación del método abstracto hacer_sonido
    def hacer_sonido(self):
        return "Miau"

# Uso de las clases
animales = [Perro(), Gato()]

# Iteramos sobre la lista de animales y llamamos al método hacer_sonido de cada uno
for animal in animales:
    print(animal.hacer_sonido())