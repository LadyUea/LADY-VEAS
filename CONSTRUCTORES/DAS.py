# Lista global para almacenar tareas
tareas = []


def agregar_tarea(tarea):
    """
    Esta función agrega una tarea a la lista de tareas.
    :param tarea: str, descripción de la tarea a agregar
    """
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")


def listar_tareas():
    """
    Esta función lista todas las tareas almacenadas en la lista de tareas.
    """
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Lista de tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


# Llamar a las funciones para agregar y listar tareas al inicio del programa
if __name__ == "__main__":
    # Se agregó una llamada de prueba para agregar y listar tareas
    agregar_tarea("Estudiar para el examen de POO")
    agregar_tarea("Terminar el proyecto de POO")
    listar_tareas()
