# Creo un ciclo el cual se parara cuando el conteo llegue a 11
for i in range(1,11):
    encabezado = "Tabla del {}"
    # Asigno el encabezado para cada tabla de multiplicar
    print(encabezado.format(i))
    # Salto de linea
    print()
    # Creo otro ciclo dentro de un ciclo
    for j in range(1,11):
        tabla = "{} x {} = {}"
        # Mando a llamar los datos para mostrarlos en pantalla
        print(tabla.format(i,j,i * j))
    else:
        # Otro salto de linea
        print()