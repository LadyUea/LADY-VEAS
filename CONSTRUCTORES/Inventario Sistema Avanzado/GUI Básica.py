import tkinter as tk  # Importamos la librería Tkinter para crear la GUI
from tkinter import messagebox  # Importamos messagebox para mostrar advertencias

# Función para agregar un ítem a la lista
def agregar_item():
    item = entry_texto.get()  # Obtener el texto del campo de entrada
    if item:  # Verificamos si el campo de texto no está vacío
        lista_items.insert(tk.END, item)  # Agregamos el ítem al final de la lista
        entry_texto.delete(0, tk.END)  # Limpiamos el campo de texto después de agregar el ítem
    else:
        # Si el campo de texto está vacío, mostramos una advertencia
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista de ítems
def limpiar_lista():
    lista_items.delete(0, tk.END)  # Eliminamos todos los ítems de la lista

# Crear la ventana principal
ventana = tk.Tk()  # Inicializamos la ventana principal de la aplicación
ventana.title("Aplicación GUI Básica")  # Establecemos el título de la ventana

# Crear una etiqueta (label) para guiar al usuario
label = tk.Label(ventana, text="Ingresa información:")  # Creamos una etiqueta descriptiva
label.pack(pady=10)  # Colocamos la etiqueta en la ventana con un pequeño margen vertical

# Crear el campo de texto donde el usuario ingresará datos
entry_texto = tk.Entry(ventana, width=30)  # Creamos un campo de entrada con un ancho de 30 caracteres
entry_texto.pack(pady=5)  # Colocamos el campo de texto en la ventana con un pequeño margen vertical

# Crear botón para agregar ítem a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_item)  # Creamos un botón que ejecuta la función agregar_item
boton_agregar.pack(pady=5)  # Colocamos el botón en la ventana con un pequeño margen vertical

# Crear lista (Listbox) para mostrar los ítems agregados
lista_items = tk.Listbox(ventana, width=50, height=10)  # Creamos una lista con un ancho de 50 y una altura de 10 elementos visibles
lista_items.pack(pady=10)  # Colocamos la lista en la ventana con un pequeño margen vertical

# Crear botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)  # Creamos un botón que ejecuta la función limpiar_lista
boton_limpiar.pack(pady=5)  # Colocamos el botón en la ventana con un pequeño margen vertical

# Iniciar el bucle principal de la aplicación para que la ventana esté en funcionamiento
ventana.mainloop()  # Inicia el bucle principal de la ventana
