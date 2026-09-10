#EXAMEN RECUPERATORIO PYTHON
#TEMA: MATRICES
#AÑO: 3°AÑO
#MODALIDAD: INFORMATICA
#NOMBRE:OCTAVIO
#APELLIDO: CARRIZO
#FECHA: 10/09/2026
matriz = []

while True:
    menu = int(input("Ingresá el número de la opción que quieras realizar: \n1. Crear matriz \n2. Mostrar la matriz cargada \n3. Sumatoria \n4. Productoria \n5. Transpuesta \n6. Salir \n"))
    if menu == 1:
        Filas = int(input("Ingresá el número de filas: "))
        Columnas = int(input("Ingresá el número de columnas: "))
        matriz = []
        for xd in range(Filas):
            fila = []
            for gg in range(Columnas):
                valor = int(input(f"Ingresá el valor para la fila {xd + 1}, columna {gg + 1}: "))
                fila.append(valor)
            matriz.append(fila)
    elif menu == 2:
        for fila in matriz:
            print(fila)
    elif menu == 3:
        suma = 0
        for fila in matriz:
            for valor in fila:
                suma += valor
        print(f"La suma de todos los elementos de la matriz es: {suma}")
    elif menu == 4:
        producto = 1
        for fila in matriz:
            for valor in fila:
                producto *= valor
        print(f"La productoria de todos los elementos de la matriz es: {producto}")
    elif menu == 5:
        if not matriz:
            print("Primero debe crear una matriz.")
            continue
        transpuesta = []
        for j in range(len(matriz[0])):
            fila_transpuesta = []
            for i in range(len(matriz)):
                fila_transpuesta.append(matriz[i][j])
            transpuesta.append(fila_transpuesta)
        print("La matriz transpuesta es:")
        for fila in transpuesta:
            print(fila)
    elif menu == 6:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida.") 