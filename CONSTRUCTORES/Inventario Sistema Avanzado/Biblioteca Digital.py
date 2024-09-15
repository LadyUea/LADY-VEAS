class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla inmutable para el título y autor
        self.titulo_autor = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Método para mostrar una representación amigable del libro
        return f"'{self.titulo_autor[0]}' por {self.titulo_autor[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # Lista para almacenar los libros que el usuario ha prestado
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Añade el libro a la lista de libros prestados
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        # Busca y elimina el libro prestado de la lista por su ISBN
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None  # Retorna None si no encuentra el libro

    def listar_libros_prestados(self):
        # Devuelve una lista con los títulos de los libros prestados
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        # Representación amigable del usuario
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


class Biblioteca:
    def __init__(self):
        # Diccionario para los libros disponibles, con ISBN como clave
        self.libros = {}
        # Diccionario para los usuarios registrados, con ID como clave
        self.usuarios = {}

    def agregar_libro(self, libro):
        # Añade un libro a la biblioteca si el ISBN no existe
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro {libro.titulo_autor[0]} agregado a la biblioteca.")

    def eliminar_libro(self, isbn):
        # Elimina un libro de la biblioteca por su ISBN
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn} en la biblioteca.")

    def registrar_usuario(self, usuario):
        # Registra un usuario nuevo si su ID no está registrado
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario {usuario.nombre} registrado correctamente.")

    def dar_baja_usuario(self, id_usuario):
        # Elimina a un usuario registrado por su ID
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        # Permite prestar un libro a un usuario si ambos existen
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.prestar_libro(libro)  # El usuario toma el libro prestado
            del self.libros[isbn]  # El libro se quita del catálogo
            print(f"Libro '{libro.titulo_autor[0]}' prestado a {usuario.nombre}.")
        else:
            print("Libro o usuario no encontrados.")

    def devolver_libro(self, isbn, id_usuario):
        # Devuelve un libro y lo añade de nuevo al catálogo de la biblioteca
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            libro = usuario.devolver_libro(isbn)  # El usuario devuelve el libro
            if libro:
                self.libros[isbn] = libro  # El libro se regresa al catálogo
                print(f"Libro '{libro.titulo_autor[0]}' devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario {usuario.nombre} no tiene prestado el libro con ISBN {isbn}.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        # Permite buscar libros por título, autor o categoría
        resultados = []
        for libro in self.libros.values():
            # Busca por coincidencia de título, autor o categoría
            if (titulo and titulo in libro.titulo_autor[0]) or \
               (autor and autor in libro.titulo_autor[1]) or \
               (categoria and categoria == libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        # Lista los libros prestados de un usuario si está registrado
        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].listar_libros_prestados()
        else:
            print("Usuario no encontrado.")


