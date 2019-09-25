# Declaro las variables que voy a utilizar en el while
acumulado = int(0)
numero = str("")
# Creo un ciclo infinito al colocar True como condicion de while, hasta que utilize la palabra break
while True:
    numero = input("Dame un numero entero: ")
    if numero=="":
        # Si el numero es vacio, mandara est mensaje y saldra de la aplicacion porque use el break
        print("Vacio. Salida del programa")
        # Con esto sale del programa
        break
    else:
        # Si se proporciono un valor, se realiza el calculo indicado
        acumulado+=int(numero)
        # No parara hasta que el usuario digite un valor vacio
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))