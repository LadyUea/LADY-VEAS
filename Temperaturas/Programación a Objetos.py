class ClimaDiario:
    def __init__(self):
        # Inicializa la lista de temperaturas
        self.temperaturas = []

    def ingresar_temperaturas(self):
        # Solicitar la temperatura para cada día de la semana (7 días)
        for i in range(7):
            # Captura la temperatura como un número flotante
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            # Agrega la temperatura a la lista
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        # Calcula el promedio dividiendo la suma de temperaturas por el número de días
        return sum(self.temperaturas) / len(self.temperaturas)

class GestorClima:
    def __init__(self):
        # Inicializa una instancia de ClimaDiario
        self.clima_diario = ClimaDiario()

    def ejecutar(self):
        print("Programa para calcular el promedio semanal de temperaturas.")
        # Llama al método para ingresar las temperaturas
        self.clima_diario.ingresar_temperaturas()
        # Llama al método para calcular el promedio
        promedio = self.clima_diario.calcular_promedio()
        # Imprime el promedio calculado
        print(f"La temperatura promedio de la semana es: {promedio:.2f}°C")

# Ejecutar el programa si este archivo se ejecuta como script
if __name__ == "__main__":
    gestor_clima = GestorClima()
    gestor_clima.ejecutar()