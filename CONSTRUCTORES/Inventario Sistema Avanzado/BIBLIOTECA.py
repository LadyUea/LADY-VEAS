class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', categoria='{self.categoria}', isbn='{self.isbn}')"
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __repr__(self):
        return f"Usuario(nombre='{self.nombre}', id_usuario='{self.id_usuario}', libros_prestados={self.libros_prestados})"
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario in [u.id_usuario for u in self.usuarios]:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario)
            print(f"Usuario '{usuario.nombre}' registrado.")

    def dar_baja_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if libro and usuario:
            if libro.isbn in [l.isbn for l in usuario.libros_prestados]:
                print(f"El libro '{libro.titulo}' ya está prestado a este usuario.")
            else:
                usuario.libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a '{usuario.nombre}'.")
        else:
            print(f"No se pudo prestar el libro o el usuario no está registrado.")

    def devolver_libro(self, isbn, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por '{usuario.nombre}'.")
            else:
                print(f"El libro con ISBN {isbn} no está prestado a este usuario.")
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")

    def buscar_libros(self, criterio):
        resultados = [libro for libro in self.libros.values() if (criterio.lower() in libro.titulo.lower() or
                                                                   criterio.lower() in libro.autor.lower() or
                                                                   criterio.lower() in libro.categoria.lower())]
        return resultados

    def listar_libros_prestados(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            return usuario.libros_prestados
        else:
            print(f"No se encontró el usuario con ID {id_usuario}.")
            return []
# Crear una biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Alquimista", "Paulo Coelho", "Ficción", "1234567890")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "0987654321")

# Añadir libros a la biblioteca
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Lady", "u001")
usuario2 = Usuario("David", "u002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar un libro
biblioteca.prestar_libro("1234567890", "u001")

# Buscar libros
print(biblioteca.buscar_libros("Cien años"))

# Listar libros prestados
print(biblioteca.listar_libros_prestados("u001"))

# Devolver un libro
biblioteca.devolver_libro("1234567890", "u001")

# Quitar un libro
biblioteca.quitar_libro("0987654321")
