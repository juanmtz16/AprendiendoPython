# Creo una variable y le solicito al usuario su nombre
nombre = input("Escribe tu nombre: ")
# Creo una variable y le solicito al usuario su apellido
apellido = input("Escribe tu apellido: ")
# Uno las dos valores y formo una sola variable llamada nombrecompleto por medio de la concatenacion
nombrecompleto = nombre + " " + apellido
# Transformo los valores de la variable nombrecompleto a mayusculas con str.upper()
nombrecompleto = nombrecompleto.upper()
# mando a imprimir la variable nombrecompleto 
print("Tu nombre completo es: " + nombrecompleto)