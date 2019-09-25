# Le pido al usuario 2 variables con un input
numero1 = input("Ingresa un numero: ")
numero2 = input("Ingresa otro numero: ")
# mediante el if estoy comparando los 2 valores que me dio el usuario y hara la condicion que se vaya cumpliendo
#  si no se cumple continuara hasta que alguna se cumpla.
if numero1 > numero2:
    resultado = ("Numeros proporcionados: {} y {} . El mayor es el primero")
    print(resultado.format(numero1,numero2))
else:
    # Puedo crear un if dentro de otro if
    if numero1 == numero2:
        resultado = ("Numeros proporcionados: {} y {} . Los dos numeros son iguales")
        print(resultado.format(numero1,numero2))
    else:
        resultado2 = ("Numeros proporcionados: {} y {} . El mayor es el segundo")
        print(resultado2.format(numero1,numero2))