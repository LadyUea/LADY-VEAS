# calculo_areas.py
# Este programa calcula el área de un rectángulo y de un círculo.
# Desarrollado por: [Estudiante de TIC Lady Veas]

def calcular_area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.
    :param largo: Largo del rectángulo (float)
    :param ancho: Ancho del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    return largo * ancho

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    import math
    return math.pi * radio ** 2

# Ejemplo de uso
if __name__ == "__main__":
    largo = 5.0  # float
    ancho = 3.0  # float
    radio = 2.5  # float

    area_rectangulo = calcular_area_rectangulo(largo, ancho)
    area_circulo = calcular_area_circulo(radio)

    print(f"El área del rectángulo es: {area_rectangulo} unidades cuadradas.")
    print(f"El área del círculo es: {area_circulo} unidades cuadradas.")