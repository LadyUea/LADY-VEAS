import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

# Función para agregar evento
def agregar_evento():
    fecha = date_entry.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    # Comprobar si los campos están llenos
    if not (fecha and hora and descripcion):
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    # Agregar evento a TreeView
    tree.insert("", "end", values=(fecha, hora, descripcion))
    limpiar_campos()

# Función para eliminar evento seleccionado
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

# Función para limpiar campos
def limpiar_campos():
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("600x400")

# Frame principal
frame_principal = tk.Frame(root)
frame_principal.pack(pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_principal, text="Fecha").grid(row=0, column=0, padx=10, pady=5)
tk.Label(frame_principal, text="Hora").grid(row=1, column=0, padx=10, pady=5)
tk.Label(frame_principal, text="Descripción").grid(row=2, column=0, padx=10, pady=5)

# DateEntry (Selector de fecha)
date_entry = DateEntry(frame_principal, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=10, pady=5)

# Entry para hora y descripción
entry_hora = tk.Entry(frame_principal)
entry_hora.grid(row=1, column=1, padx=10, pady=5)

entry_descripcion = tk.Entry(frame_principal)
entry_descripcion.grid(row=2, column=1, padx=10, pady=5)

# Botones para agregar, eliminar y salir
btn_agregar = tk.Button(frame_principal, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=3, column=0, pady=10)

btn_eliminar = tk.Button(frame_principal, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=3, column=1, pady=10)

btn_salir = tk.Button(frame_principal, text="Salir", command=root.quit)
btn_salir.grid(row=3, column=2, pady=10)

# TreeView para mostrar los eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(pady=20)

# Configuración de columnas
tree.column("Fecha", width=100, anchor=tk.CENTER)
tree.column("Hora", width=100, anchor=tk.CENTER)
tree.column("Descripción", width=300, anchor=tk.W)

root.mainloop()
