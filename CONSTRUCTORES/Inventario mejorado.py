

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Inicializa el inventario y carga los productos desde un archivo.
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos del archivo especificado y los añade al inventario."""
        try:
            with open(self.archivo, 'r') as file:
                # Lee cada línea del archivo y crea objetos Producto.
                for linea in file:
                    id_producto, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            # Maneja el caso en que el archivo no existe.
            print(f"Archivo {self.archivo} no encontrado. Se creará uno nuevo al guardar cambios.")
        except Exception as e:
            # Maneja otros posibles errores durante la lectura del archivo.
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda el estado actual del inventario en un archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                # Escribe cada producto en una nueva línea del archivo.
                for prod in self.productos:
                    file.write(f"{prod.get_id_producto()},{prod.get_nombre()},{prod.get_cantidad()},{prod.get_precio()}\n")
            print("Cambios guardados exitosamente en el inventario.")
        except PermissionError:
            # Maneja el caso en que no se tienen permisos para escribir en el archivo.
            print(f"Error: No se tienen permisos para escribir en el archivo {self.archivo}.")
        except Exception as e:
            # Maneja otros posibles errores durante la escritura en el archivo.
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario y guarda los cambios en el archivo."""
        # Verifica si el ID del producto es único.
        for prod in self.productos:
            if prod.get_id_producto() == producto.get_id_producto():
                print(f"Error: Ya existe un producto con el ID {producto.get_id_producto()}.")
                return
        # Añade el nuevo producto al inventario y guarda los cambios.
        self.productos.append(producto)
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario según su ID y guarda los cambios en el archivo."""
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                # Elimina el producto si se encuentra en el inventario.
                self.productos.remove(prod)
                self.guardar_inventario()
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"No se encontró un producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto y guarda los cambios en el archivo."""
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                # Actualiza la cantidad y/o precio del producto.
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                # Guarda los cambios en el archivo.
                self.guardar_inventario()
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"No se encontró un producto con el ID {id_producto}.")

# La clase Producto permanece igual, utilizada para crear objetos de productos.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa un nuevo producto con los atributos dados
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id_producto(self):
        return self._id_producto

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        # Representación en cadena del producto
        return f"ID: {self._id_producto}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

def menu():
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

