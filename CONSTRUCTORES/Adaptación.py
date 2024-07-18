import datetime


# Función para mostrar la fecha y hora actuales
def mostrar_fecha_hora():
    """
    Esta función obtiene la fecha y hora actuales y las imprime en el formato 'YYYY-MM-DD HH:MM:SS'.
    """
    ahora = datetime.datetime.now()
    print("Fecha y hora actuales:", ahora.strftime("%Y-%m-%d %H:%M:%S"))


# Llamar a la función para mostrar la fecha y hora al inicio del programa
if __name__ == "__main__":
    # Se agregó la llamada a la función mostrar_fecha_hora para mostrar la fecha y hora actuales
    # al inicio del programa.
    mostrar_fecha_hora()

    # Aquí puedes incluir el resto del código existente en Dashboard.py
    # ...
