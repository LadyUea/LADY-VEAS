class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Inicializa un nuevo producto con los atributos dados.
        :param id_producto: ID único del producto
        :param nombre: Nombre del producto
        :param cantidad: Cantidad del producto en inventario
        :param precio: Precio del producto
        """
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id_producto(self):
        """Devuelve el ID del producto."""
        return self._id_producto

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    def get_cantidad(self):
        """Devuelve la cantidad del producto."""
        return self._cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        """Establece el nombre del producto."""
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        """Establece la cantidad del producto."""
        self._cantidad = cantidad

    def set_precio(self, precio):
        """Establece el precio del producto."""
        self._precio = precio

    def __str__(self):
        """
        Representación en cadena del producto.
        :return: Cadena que representa el producto.
        """
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        """
        Inicializa el inventario y carga los productos desde un archivo.
        :param archivo: Nombre del archivo donde se almacenan los productos
        """
        self.archivo = archivo
        self.productos = {}  # Utiliza un diccionario para almacenar productos por ID
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos del archivo especificado y los añade al inventario."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[id_producto] = Producto(id_producto, nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar cambios.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda el estado actual del inventario en un archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.productos.values():
                    file.write(f"{prod.get_id_producto()},{prod.get_nombre()},{prod.get_cantidad()},{prod.get_precio()}\n")
            print("Cambios guardados exitosamente en el inventario.")
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario y guarda los cambios en el archivo.
        :param producto: Objeto Producto a añadir
        """
        if producto.get_id_producto() in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.get_id_producto()}.")
            return
        self.productos[producto.get_id_producto()] = producto
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario según su ID y guarda los cambios en el archivo.
        :param id_producto: ID del producto a eliminar
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto y guarda los cambios en el archivo.
        :param id_producto: ID del producto a actualizar
        :param cantidad: Nueva cantidad del producto
        :param precio: Nuevo precio del producto
        """
        if id_producto in self.productos:
            prod = self.productos[id_producto]
            if cantidad is not None:
                prod.set_cantidad(cantidad)
            if precio is not None:
                prod.set_precio(precio)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print(f"No se encontró un producto con el ID {id_producto}.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre y los muestra.
        :param nombre: Nombre del producto a buscar
        """
        encontrados = [prod for prod in self.productos.values() if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            for prod in encontrados:
                print(prod)
        else:
            print(f"No se encontró ningún producto con el nombre '{nombre}'.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for prod in self.productos.values():
                print(prod)
        else:
            print("El inventario está vacío.")


def menu():
    """Interfaz de usuario en la consola para interactuar con el sistema de gestión de inventarios."""
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios - Tactical Vencer o Morir ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, cantidad=int(cantidad) if cantidad else None,
                                           precio=float(precio) if precio else None)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
