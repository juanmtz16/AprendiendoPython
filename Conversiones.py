# Declaro una variable de tipo string y le asigno una cadena con valor "1234".
numeros = "1234"
# Muestro en pantalla el tipo de dato que es la variable numeros.
print(type(numeros))
# Convierto el tipo de dato str en int.
numeros = int(numeros)
# Muestro en pantalla el nuevo tipo de dato de la variable numeros.
print(type(numeros))
# declaro una variable de tipo string en la cual iran valores proporcionados usando el format.
salida = "El numero que se convirtio es {}"
# Muestro el resultado las llaves y el punto format haran que se coloque el valor de numeros.
print(salida.format(numeros))