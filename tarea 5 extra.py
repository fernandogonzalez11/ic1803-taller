# ej 2: versión for
def obtener_digitos_for(string):
    if not isinstance(string, str):
        return "string no es string"

    res = ""
    for char in string:
        if char.isdigit():
            res += char

    return res
        
# ej 2: versión trozos
def obtener_digitos_trozos(string):
    if not isinstance(string, str):
        return "string no es string"
    
    res = ""
    while string:
        if string[0].isdigit():
            res += string[0]

        string = string[1:]

    return res

# ej 3: versión índices
def obtener_digitos_indices(string):
    if not isinstance(string, str):
        return "string no es string"

    res = ""
    for i in range(len(string)):
        if string[i].isdigit():
            res += string[i]

    return res

# ej 3
def contar_palabras(palabras, frases):
    if not isinstance(palabras, tuple) or not isinstance(frases, tuple):
        return "que sean tuplas plox"

    apariciones = []
    for palabra in palabras:
        apariciones_palabra = 0
        for frase in frases:
            apariciones_palabra += frase.count(palabra)
        
        apariciones.append((palabra, apariciones_palabra))

    return apariciones

# ej 5
def fibonacci(n):
    if n == 1:
        return (0,)

    inicio = (0, 1)

    for i in range(2, n):
        inicio += (inicio[-1] + inicio[-2],)
    
    return inicio

# ej 6
def es_palabra_palindromo(palabra):
    if not isinstance(palabra, str) or not palabra:
        return "mande un string no vacío gracias"

    reverso = palabra[::-1]
    
    return palabra == reverso

# ej 8
def produccion_total(plantas):
    producidos = []
    
    for planta in plantas:
        for tableta in planta[2:]:
            # revisar membresía en producidos
            for i, producido in enumerate(producidos):
                if producido[0] == tableta[0]:
                    producidos[i] = (producido[0], producido[1] + tableta[1])
                    break
            else:
                producidos.append((tableta[0], tableta[1]))

    return producidos

# ej 9
def leer_matriz(filas, columnas):
    matriz = [[0 for col in range(columnas)] for fil in range(filas)]

    for fila in range(filas):
        for columna in range(columnas):
            val = input(f"fila {fila} columna {columna} ")
            matriz[fila][columna] = int(val)

    return matriz

# ej 11
def matriz_transpuesta(matriz):
    transpuesta = [[0 for col in range(len(matriz))] for fil in range(len(matriz[0]))]

    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            transpuesta[columna][fila] = matriz[fila][columna]

    return transpuesta

# ej 12
def triángulo_de_pascal(n):
    términos = [(1,), (1,1)]

    if n < 3:
        return términos[:n]

    for i in range(3, n + 1):
        tupla = (1,)

        for j in range(len(términos[-1]) - 1):
            tupla += (términos[-1][j] + términos[-1][j + 1],)

        tupla += (1,)
        
        términos.append(tupla)

    return términos

# ej 14
def crear_matriz_unitaria(tamaño):
    matriz = [[0 for i in range(tamaño)] for j in range(tamaño)]

    for k in range(tamaño):
        matriz[k][k] = 1

    return matriz

# ej 15
def multiplica_matrices(matriz_1, matriz_2):
    matriz_resultante = [[0 for col in range(len(matriz_2[0]))] for fil in range(len(matriz_1))]

    for i in range(len(matriz_1)):
        for j in range(len(matriz_2[0])):
            for k in range(len(matriz_1)):
                matriz_resultante[i][j] += matriz_1[i][k] * matriz_2[k][j]

    return matriz_resultante

# ej 18
def materias_y_estudiantes(estudiantes):
    materias = []

    for estudiante in estudiantes:
        # para cada tupla de materia contenida en el estudiante
        for tupla_materia in estudiante[2:]:
            # construir la tupla formateada para la lista de materias
            tupla_formateada = (estudiante[0], estudiante[1], tupla_materia[0])

            # encontrar el índice de la materia en cuestión, si existe
            ind = índice_en_materias(tupla_materia[1], materias)

            if ind != -1:
                # añadirlo al índice indicado si existe
                materias[ind].append(tupla_formateada)
            else:
                # crear un nuevo elemento si no
                materias.append([tupla_materia[1], tupla_formateada])

    return materias

def índice_en_materias(materia, materias):
    for i, m in enumerate(materias):
        if m[0] == materia:
            return i
    else:
        return -1