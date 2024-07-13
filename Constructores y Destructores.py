class Archivo:
    def __init__(self, nombre):
        """
        Constructor: Inicializa el objeto y abre el archivo en modo escritura.

        :param nombre: Nombre del archivo que se va a manejar.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo {self.nombre} ha sido abierto.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.

        :param texto: Texto que se va a escribir en el archivo.
        """
        self.archivo.write(texto)

    def __del__(self):
        """
        Destructor: Cierra el archivo cuando el objeto es destruido.
        """
        self.archivo.close()
        print(f"Archivo {self.nombre} ha sido cerrado.")


# Creación de un objeto de la clase Archivo
archivo = Archivo('mi_archivo.txt')

# Escribiendo en el archivo
archivo.escribir('Hola, este es un ejemplo de uso de constructores y destructores en Python.')

# Eliminando el objeto (esto llamará al destructor)
del archivo
