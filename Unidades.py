# conversion_unidades.py
# Este programa convierte unidades de medida entre diferentes sistemas.
# Desarrollado por: [Elaborado por Lady Veas Estudiante UEA - TIC]

def convertir_metros_a_pies(metros):
    """
    Convierte metros a pies.
    :param metros: Longitud en metros (float)
    :return: Longitud en pies (float)
    """
    return metros * 3.28084

def convertir_litros_a_galones(litros):
    """
    Convierte litros a galones.
    :param litros: Volumen en litros (float)
    :return: Volumen en galones (float)
    """
    return litros * 0.264172

def convertir_celsius_a_fahrenheit(grados_celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    :param grados_celsius: Temperatura en grados Celsius (float)
    :return: Temperatura en grados Fahrenheit (float)
    """
    return (grados_celsius * 9/5) + 32

# Ejemplo de uso
if __name__ == "__main__":
    longitud_metros = 10.0  # float
    volumen_litros = 5.0    # float
    temperatura_celsius = 25.0 # float

    longitud_pies = convertir_metros_a_pies(longitud_metros)
    volumen_galones = convertir_litros_a_galones(volumen_litros)
    temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

    print(f"{longitud_metros} metros son {longitud_pies} pies.")
    print(f"{volumen_litros} litros son {volumen_galones} galones.")
    print(f"{temperatura_celsius} grados Celsius son {temperatura_fahrenheit} grados Fahrenheit.")