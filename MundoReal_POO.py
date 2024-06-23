# sistema_reservas.py

class Cliente:
    """
    Representa un cliente del hotel.
    """
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def _str_(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

class Habitacion:
    """
    Representa una habitación del hotel.
    """
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.esta_disponible = True

    def _str_(self):
        estado = "Disponible" si self.esta_disponible else "Ocupada"
        return f"Habitación {self.numero} ({self.tipo}): {estado}, Precio: ${self.precio}"

class Reserva:
    """
    Representa una reserva realizada por un cliente para una habitación específica.
    """
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def costo_total(self):
        """
        Calcula el costo total de la reserva en función del precio de la habitación y la cantidad de días.
        """
        return self.habitacion.precio * self.dias

    def _str_(self):
        return f"Reserva de {self.cliente.nombre} en {self.habitacion.tipo} por {self.dias} días. Costo total: ${self.costo_total()}"

class Hotel:
    """
    Representa un hotel con múltiples habitaciones y reservas.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación a la lista de habitaciones del hotel.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """
        Muestra todas las habitaciones disponibles en el hotel.
        """
        disponibles = [str(habitacion) for habitacion in self.habitaciones if habitacion.esta_disponible]
        return "\n".join(disponibles) if disponibles else "No hay habitaciones disponibles."

    def realizar_reserva(self, cliente, numero_habitacion, dias):
        """
        Realiza una reserva para un cliente dado un número de habitación y la cantidad de días.
        """
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion:
                if habitacion.esta_disponible:
                    habitacion.esta_disponible = False
                    nueva_reserva = Reserva(cliente, habitacion, dias)
                    self.reservas.append(nueva_reserva)
                    return f"Reserva realizada:\n{nueva_reserva}"
                else:
                    return "Habitación no disponible."
        return "Habitación no encontrada."

    def _str_(self):
        return f"Hotel {self.nombre}"

# Ejemplo de uso
if _name_ == "_main_":
    # Crear hotel
    hotel = Hotel("Gran Hotel")

    # Agregar habitaciones
    hotel.agregar_habitacion(Habitacion(101, "Individual", 50))
    hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
    hotel.agregar_habitacion(Habitacion(103, "Suite", 120))

    # Crear cliente
    cliente1 = Cliente("Juan Pérez", "juan.perez@example.com")

    # Mostrar habitaciones disponibles
    print("Habitaciones disponibles:")
    print(hotel.mostrar_habitaciones_disponibles())

    # Realizar reserva
    print("\nRealizando reserva...")
    print(hotel.realizar_reserva(cliente1, 102, 3))

    # Mostrar habitaciones disponibles después de la reserva
    print("\nHabitaciones disponibles después de la reserva:")
    print(hotel.mostrar_habitaciones_disponibles())