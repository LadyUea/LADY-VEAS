class BaseDeDatos:
    def __init__(self, nombre):
        """
        Constructor: Inicializa la conexión a la base de datos.

        :param nombre: Nombre de la base de datos.
        """
        self.nombre = nombre
        self.conexion = self.conectar()
        print(f"Conexión a la base de datos '{self.nombre}' establecida.")

    def conectar(self):
        """
        Simula la conexión a la base de datos.

        :return: Objeto de conexión simulado.
        """
        return f"Conexión a {self.nombre}"

    def ejecutar_consulta(self, consulta):
        """
        Método para ejecutar una consulta en la base de datos.

        :param consulta: La consulta SQL que se va a ejecutar.
        """
        print(f"Ejecutando consulta: {consulta}")

    def __del__(self):
        """
        Destructor: Cierra la conexión a la base de datos.
        """
        self.conexion = None
        print(f"Conexión a la base de datos '{self.nombre}' cerrada.")


# Creación de un objeto de la clase BaseDeDatos
bd = BaseDeDatos('mi_base_de_datos')

# Ejecutando una consulta en la base de datos
bd.ejecutar_consulta('SELECT * FROM usuarios')

# Eliminando el objeto (esto llamará al destructor)
del bd
