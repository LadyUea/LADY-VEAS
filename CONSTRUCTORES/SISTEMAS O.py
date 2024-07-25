import threading
import time

# Función que realiza una tarea simple
def tarea_simple(nombre):
    print(f"Hilo {nombre} iniciando...")
    time.sleep(2)
    print(f"Hilo {nombre} terminado...")

# Crear y lanzar hilos
hilos = []
for i in range(5):
    hilo = threading.Thread(target=tarea_simple, args=(f'Hilo-{i+1}',))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("Todos los hilos han terminado.")