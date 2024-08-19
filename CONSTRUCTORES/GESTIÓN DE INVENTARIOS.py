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
class Inventario:
    def __init__(self):
        # Inicializa una lista con los productos de la tienda
        self.productos = [
            Producto("001", "Chaleco Balístico", 10, 125.00),
            Producto("002", "Placas Kevlar Nivel III", 15, 140.00),
            Producto("003", "Camiseta Táctica", 30, 10.00),
            Producto("004", "Pantalón Táctico", 20, 40.00)
        ]

    def agregar_producto(self, producto):
        # Añade un nuevo producto al inventario, asegurando que el ID sea único
        for prod in self.productos:
            if prod.get_id_producto() == producto.get_id_producto():
                print(f"Error: Ya existe un producto con el ID {producto.get_id_producto()}.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                self.productos.remove(prod)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"No se encontró un producto con el ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for prod in self.productos:
            if prod.get_id_producto() == id_producto:
                if cantidad is not None:
                    prod.set_cantidad(cantidad)
                if precio is not None:
                    prod.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado.")
                return
        print(f"No se encontró un producto con el ID {id_producto}.")

    def buscar_producto(self, nombre):
        resultados = [prod for prod in self.productos if nombre.lower() in prod.get_nombre().lower()]
        if resultados:
            for prod in resultados:
                print(prod)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for prod in self.productos:
                print(prod)


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


