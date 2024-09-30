import tkinter as tk
from tkinter import messagebox


# Función para añadir una nueva tarea a la lista
def add_task(event=None):
    task = entry_task.get()  # Obtener el texto del campo de entrada
    if task:  # Si la tarea no está vacía
        listbox_tasks.insert(tk.END, task)  # Añadir la tarea al final de la lista
        entry_task.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")


# Función para marcar una tarea como completada
def mark_completed():
    try:
        # Obtener el índice de la tarea seleccionada
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)

        # Actualizar la tarea para reflejar que está completada (visualmente)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")


# Función para eliminar una tarea seleccionada
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]  # Obtener el índice de la tarea seleccionada
        listbox_tasks.delete(selected_task_index)  # Eliminar la tarea de la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")


# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear los widgets (entrada de texto, lista y botones)
frame = tk.Frame(root)
frame.pack(pady=10)

# Campo de entrada para escribir una nueva tarea
entry_task = tk.Entry(frame, width=40)
entry_task.pack(side=tk.LEFT, padx=5)
entry_task.bind("<Return>", add_task)  # Permitir añadir tarea con tecla Enter

# Botón para añadir tarea
btn_add_task = tk.Button(frame, text="Añadir Tarea", command=add_task)
btn_add_task.pack(side=tk.LEFT, padx=5)

# Listbox para mostrar las tareas actuales
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Botones para marcar como completada y eliminar tarea
btn_mark_completed = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_mark_completed.pack(side=tk.LEFT, padx=5)

btn_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete_task.pack(side=tk.LEFT, padx=5)

# Iniciar el loop principal de la aplicación
root.mainloop()
