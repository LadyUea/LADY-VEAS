import tkinter as tk
from tkinter import messagebox, Listbox, END, SINGLE


class TaskManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestión de Tareas")

        # Crear un campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.pack(pady=10)

        # Crear botones para añadir, completar y eliminar tareas
        self.add_button = tk.Button(master, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(master, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Crear un Listbox para mostrar las tareas
        self.task_list = Listbox(master, selectmode=SINGLE, width=50, height=10)
        self.task_list.pack(pady=10)

        # Configurar atajos de teclado
        master.bind("<Return>", self.add_task)  # Tecla Enter para añadir tarea
        master.bind("<c>", self.complete_task)  # Tecla 'C' para completar tarea
        master.bind("<Delete>", self.delete_task)  # Tecla 'Delete' para eliminar tarea
        master.bind("<Escape>", self.close_app)  # Tecla Escape para cerrar la aplicación

    def add_task(self, event=None):
        """Añadir una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task:
            self.task_list.insert(END, task)  # Añadir la tarea al Listbox
            self.task_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self, event=None):
        """Marcar la tarea seleccionada como completada."""
        try:
            selected_task_index = self.task_list.curselection()[0]  # Obtener índice de la tarea seleccionada
            task = self.task_list.get(selected_task_index)  # Obtener la tarea seleccionada
            self.task_list.delete(selected_task_index)  # Eliminar la tarea de la lista
            self.task_list.insert(END, f"{task} (Completada)")  # Añadir tarea completada
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para completar.")

    def delete_task(self, event=None):
        """Eliminar la tarea seleccionada de la lista."""
        try:
            selected_task_index = self.task_list.curselection()[0]  # Obtener índice de la tarea seleccionada
            self.task_list.delete(selected_task_index)  # Eliminar la tarea de la lista
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def close_app(self, event=None):
        """Cerrar la aplicación."""
        self.master.quit()


# Crear la ventana principal y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
