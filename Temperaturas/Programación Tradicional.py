# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Lista para almacenar las temperaturas diarias
    temperaturas = []
    # Solicitar la temperatura para cada día de la semana (7 días)
    for i in range(7):
        # Captura la temperatura como un número flotante
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        # Agrega la temperatura a la lista
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    # Calcula el promedio dividiendo la suma de temperaturas por el número de días
    return sum(temperaturas) / len(temperaturas)

# Función principal para gestionar el flujo del programa
def main():
    print("Programa para calcular el promedio semanal de temperaturas.")
    # Llama a la función para ingresar las temperaturas
    temperaturas = ingresar_temperaturas()
    # Llama a la función para calcular el promedio
    promedio = calcular_promedio(temperaturas)
    # Imprime el promedio calculado
    print(f"La temperatura promedio de la semana es: {promedio:.2f}°C")

# Ejecutar la función principal si este archivo se ejecuta como script
if __name__ == "__main__":
    main()