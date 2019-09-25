# Utilizo el input para poder interactuar con el usuario y me pueda dar algun valor
entrada = input()
# Mando a pantalla el tipo de dato de la variable entrada
print(type(entrada))
# Declaro una variable la cual va a verificar si lo capturado es digito, y si no se encuentra un punto en lo que capturo el usuario
# Y si Find retorna -1 quiere decir que lo buscado, osea un punto decimal no se encontró.
esEntero = (entrada.isdigit() and entrada.find(".")==-1)
# Creo una condicion mediante un if
if (esEntero):
    # Esta parte se ejecutara si la condicion es verdadera
    print("Dato entero. ¡Muy bien!")
else:
    # Esta parte se ejecutara si la condicion es falsa.
    print("Dato no es entero. Intentar nuevamente")