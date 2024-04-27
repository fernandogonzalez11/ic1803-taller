def imprimir_matriz(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    contador = 0

    # para cada fila, imprime los valores separados por espacios
    while contador < n_filas:
        fila = matriz[contador]
        indice = 0
        while indice < n_columnas:
            print(fila[indice], end=" ")
            indice += 1
        # termina cada fila con una nueva línea
        print(end="\n")
        contador += 1