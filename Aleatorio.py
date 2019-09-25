# Importamos el modulo random mediante la instruccion import
import random
# Creo una variable de tipo float y le asigno un valor
numero1 = float(10.5)
# Creo una funcion en la cual declaro una variable de tipo float
# que adquirira un valor aleatorio entre 1 y 10 y al final se sumaran y me mostrara el resultado aleatorio.
def miprimerafuncion():
    # Creo una nueva variable que adquirira un valor aleatorio entre 1 y 10
    numero2 = float(random.randrange(1,10))
    # Utilizo meta sustituciones para mostrar resultados.
    mensaje = "La suma de {} y {} es {}"
    # Mando a pantalla los resultados y en 1 de ellos sumo las 2 variables
    print(mensaje.format(numero1,numero2,numero1+numero2))
# Ejecuto la funcion
miprimerafuncion()