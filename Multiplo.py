# Pido un valor entero al usuario y lo almaceno tipo int
numero = input("Dame un numero entero: ")
numero = int(numero)
# Realizo la operacion de almacenar los residuales de los valores booleanos.
# Si el residual es cero, quiere desir que el numero es multiplo.
esMultiplo3 = ((numero%3)==0)
esMultiplo5 = ((numero%5)==0)
esMultiplo7 = ((numero%7)==0)
# Creo una condicion con operador logico el cual dos variables juntas se deben de cumplir y si se cumple la tercera o no, no importa.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto")
else:
    print("Incorrecto")