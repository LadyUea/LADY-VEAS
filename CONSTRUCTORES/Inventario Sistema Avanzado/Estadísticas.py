import random

# Lista con las alturas de la población de la tabla 1
alturas = [12.31, 13.72, 15.84, 15.91, 14.68, 14.86, 13.66, 12.32, 18.21, 16.27,
           18.78, 17.74, 18.61, 18.77, 19.22, 19.96, 15.36, 13.10, 16.00, 16.51,
           15.83, 15.85, 17.57, 18.00, 12.23, 12.65, 11.61, 9.36, 10.21, 12.4,
           11.41, 9.74, 19.10, 17.15, 17.00, 16.25, 16.18, 17.4, 15.91, 16.17,
           13.81, 13.20, 13.53, 14.62, 15.37, 16.91, 15.45, 13.47, 12.51, 11.37,
           13.60, 13.92, 13.53, 13.54, 13.70, 14.00, 11.81, 12.57, 14.59, 13.25,
           13.41, 13.52, 14.37, 13.41, 14.60, 15.26, 15.91, 15.40, 13.45, 12.13,
           11.31, 13.88]

# Selecciona una muestra aleatoria simple de entre 10 y 20 observaciones
muestra = random.sample(alturas, k=15)  # Puedes cambiar el valor de k entre 10 y 20
print("Muestra seleccionada:", muestra)
