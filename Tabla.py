# Le pido un valor al usuario entre los numeros del 1 al 9
numero = input("Dame un numero del 1 al 9")
# Covierto el valor en tipo entero
numero = int(numero)
# Creo un ciclo en el cual comenzara en 1 y terminara en 11 los cuales me dara los valores que vale i cada vez que se repite el ciclo
for i in range(1,11):
    salida = "{} x {} = {}"
    # Muestro los valores de la variable numero, i y la multiplicacion de i con numero
    print(salida.format(numero,i,i * numero))
