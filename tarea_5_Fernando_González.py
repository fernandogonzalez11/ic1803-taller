"""
Tarea 5
Fernando González, Sebastián Padilla, Juan Pablo Romero
Introducción a la Programación
Prof. William Mata
Grupo 4
"""

"""
ejercicio 1: recibe un elemento y una lista y retorna una lista con todos
los índices en donde se encuentre ese elemento en la lista

versión 1: usando un for

entradas: elemento, lista
salidas: lista de índices

autor: Fernando González
"""
def indices_for(elem, lista):
  if not isinstance(lista, list):
    return "ERROR: el segundo parámetro debe ser una lista"

  inds = []

  for i, e in enumerate(lista):
    if e == elem:
      inds.append(i)

  return inds

"""
versión 2: usando trozos
"""
def indices_trozos(elem, lista):
  if not isinstance(lista, list):
    return "ERROR: el segundo parámetro debe ser una lista"

  inds = []

  i = 0
  while lista:
    if lista[0] == elem:
      inds.append(i)

    i += 1
    lista = lista[1:]

  return inds

"""
versión 3: usando índices
"""
def indices_indices(elem, lista):
  if not isinstance(lista, list):
    return "ERROR: el segundo parámetro debe ser una lista"

  inds = []

  i = 0
  while i < len(lista):
    if lista[i] == elem:
      inds.append(i)

    i += 1

  return inds

"""
Ejercicio 2: obtiene un string con solo sus dígitos, del string de entrada

Versión 1: usando for

Entrada: string con caracteres mixtos.
Salida: dígitos que fueron encontrados en el string original.

Autor: Sebastián de Jesús Padilla Escalante
"""
def obtener_digitos_for(string_original):

    if not isinstance(string_original, str):
        return "Error: dato de entrada invalido"

    string_final = ""  #String donde van a ir todos los numeros.

    for digito in string_original:
        if digito.isdigit():  #Se comprueba si es un numero.
            string_final += digito

    return string_final

"""
Versión 2: usando trozos
"""
def obtener_digitos_trozos(string_original):
    if not isinstance(string_original, str):
        return "Error: dato de entrada invalido"

    inicio_trozo = 0
    final_trozo = 1
    aux_1 = 0
    aux_2 = 0
    string_final = ""


    while final_trozo < len(string_original) + 1:
        aux_1 = string_original[inicio_trozo:final_trozo]
        inicio_trozo += 1
        final_trozo += 1
        try:
            aux_2 = int(aux_1) #Si no da error, es porque si es un numero.
            string_final += aux_1 #La variable aux_2 solo existe para verificar si es numero o no.
        except:
            continue

    return string_final

"""
Versión 3: usando índices
"""
def obtener_digitos_indices(string_original):
    if not isinstance(string_original, str):
        return "Error: dato de entrada invalido"

    indice = -1
    string_final = ""

    while indice <= len(string_original) - 1:
        indice += 1
        try:
            aux_1 = int(string_original[indice])
            string_final += string_original[indice]
        except:
            continue

    return string_final

"""
3: CONTAR PALABRAS
ENTRADAS: Recibe dos tuplas: una con palabras como elementos, y otra con frases
SALIDAS: Retorna una lista de tuplas, donde cada tupla contiene la palabra de la tupla de palabras, y la cantidad de veces que esta aparece en la tupla de frases
AUTOR: Juan Pablo Romero
"""
def contar_palabras (palabra , frase):
    indice_p = 0
    lista = []
    con_frase = len (frase)
    con_palabra = len (palabra)

    # contar aparciciones para cada palabra
    while indice_p < con_palabra :
        cuenta = 0
        indice_f = 0

        # ir sumando la cantidad encontrada en cada frase
        while indice_f < con_frase :
            cuenta = cuenta + frase[indice_f].count(palabra[indice_p])
            indice_f = indice_f + 1

        # añadir la cuenta total a la lista
        lista.append((palabra[indice_p], cuenta))
        indice_p = indice_p + 1

    return tuple(lista)

"""
ejercicio 4: recibe una lista de tuplas y retorna una lista de combinaciones de pares

entradas: lista
salidas: lista de combinaciones

autor: Fernando González
"""
def juegos_de_bola(equipos):
  if not isinstance(equipos, list) or len(equipos) < 2:
    return False

  for tupla in equipos:
    if not isinstance(tupla, tuple):
      return False

  combinaciones = []

  # descontar el final
  for i, equipo_1 in enumerate(equipos[:-1]):
    # empezar desde los que le siguen al actual equipo_1, hasta el final
    for equipo_2 in equipos[i + 1:]:
      combinaciones.append( (equipo_1[0], equipo_2[0]) )

  return combinaciones

"""
Función auxiliar para ej 5: retorna el n-ésimo término de la secuencia de Fibonacci
Entrada: número n
Salida: término n-ésimo de la secuencia

Autor: Sebastián de Jesús Padilla Escalante
"""
def secuencia_fibonacci(numero):
    inst_1 = 0
    inst_2 = 1
    inst_n = 0
    contador_instancias = 0

    while contador_instancias < numero - 1:

        inst_n = inst_1 + inst_2
        inst_2 = inst_1
        inst_1 = inst_n
        contador_instancias += 1

    return inst_n


"""
Ejercicio 5: obtiene los primeros n términos de la secuencia de Fibonacci

Entrada: numero máximo de elementos de la escala de fibonaccia a dar.
Salida: los primeros n elementos de la escala de fibonacci (a partir del 0).

Autor: Sebastián de Jesús Padilla Escalante
"""
def fibonacci(numero):
    #Entrada: numero de instancias en la secuencia de fibonacci a dar.
    #Salida: tupla con el numero establecido de instancias en la secuencia fibonacci.

    tupla_final = ()
    lista_aux_1 = []
    contador = 1

    while contador <= numero:
        lista_aux_1.append(secuencia_fibonacci(contador))
        contador += 1

    tupla_final += tuple(lista_aux_1)

    return tupla_final

"""
6: ES PALABRA PALINDROMO
ENTRADAS: Recibe una palabra (string no vacio)
SALIDAS: Retorna un valor booleano segun si la palabra recibida es palindromo o no
AUTOR: Juan Pablo Romero
"""
def es_palabra_palindromo(palabra):
    if isinstance(palabra, str) == True and palabra != "":
        contador = len(palabra)
        string = ""
        indice = contador - 1
        if contador % 2  != 0:
            while indice >= 0:
                string = string + palabra[indice]
                indice = indice - 1
            if string == palabra:
                return True
            else:
                return False
        else:
          return False

    else:
        return "ERROR: LA ENTRADA DEBE SER UN STRING DIFERENTE DE VACÍO"

"""
ejercicio 7: toma un string de letras, números y puntos, y extrae sus números (enteros o decimales)

entrada: string
salida: lista de números

autor: Fernando González
"""
def extrae_números(string):
  números = []
  str_actual = ""
  for i, char in enumerate(string):
    # números
    if char.isdigit():
      str_actual += char

    # puntos
    elif char == ".":
      # para "." revisar:
      # (1) que le preceda un número
      # (2) que preceda a un número
      # (3) que no haya un punto en el string actual


      if not str_actual:
        continue

      # comprobar si le precede un número
      if i != len(string) - 1 and string[i + 1].isdigit():
        # sabiendo eso, reviso que no haya ya un punto en el string
        if "." in str_actual:
          números.append(str_actual)
          str_actual = ""
        else:
          # si le precede un número y es el único punto, se puede añadir
          str_actual += char
      else:
        # si no, necesito agarrar de una vez el string actual y ponerlo en números
        números.append(str_actual)
        str_actual = ""

    # letras
    else:
      if str_actual:
        números.append(str_actual)
        str_actual = ""

  # por si quedó un número al final
  if str_actual:
    números.append(str_actual)

  # ahora, tenemos una lista de strings con posibles enteros o flotantes
  # mapear cada uno a su tipo

  for i, num in enumerate(números):
    if num.isnumeric():
      números[i] = int(num)
    else:
      números[i] = float(num)

  return números

"""
Ejercicio 8
Obtiene la producción total de tabletas entre todas las plantas

Entrada: lista con la producción total de cada planta del fabricante.
Salida: cantidad total de tabletas producidas con su código de modelo.

Autor: Sebastián de Jesús Padilla Escalante
"""

def produccion_total(lista_produccion):
    lista_codigos = []
    lista_cantidades = []

    for planta in lista_produccion:
        #El tercer elemento siempre será una tupla.
        for produccion in planta[2:]:
            codigo_tableta = produccion[0]
            cantidad = produccion[1]

            #Se comprueba si el código de la tableta ya está en la lista.
            encontrado = False
            indice = 0
            while indice < len(lista_codigos):
                if lista_codigos[indice] == codigo_tableta:
                    #Si se encuentra, suma la cantidad a la lista de cantidades.
                    lista_cantidades[indice] += cantidad
                    encontrado = True
                    break
                indice += 1

            if not encontrado:
                lista_codigos.append(codigo_tableta)
                lista_cantidades.append(cantidad)

    lista_final = []
    indice = 0
    while indice < len(lista_codigos):
        lista_final.append((lista_codigos[indice], lista_cantidades[indice]))
        indice += 1

    return lista_final

"""
9.a) LEER MATRIZ
ENTRADAS: Recibe la cantidad de filas y columnas de una matriz, y lee cada uno de los elementos de la matriz
SALIDAS: Retorna una lista representando la matriz por filas
AUTOR: Juan Pablo Romero
"""
def leer_matriz(filas, columnas):
    cont_f = 0
    listaf = []
    # por cada fila, lee todos sus valores según columna
    while cont_f < filas:
        cont_c = 0
        cont_f += 1
        lista = []
        while cont_c < columnas:
            elemento = int(input(""))
            lista.append(elemento)
            cont_c += 1
        listaf.append(lista)
    return listaf

"""
#9.b) IMPRIMIR MATRIZ
ENTRADAS: Recibe una matriz
SALIDAS: Imprime la matriz, con cada fila en una linea separada
AUTOR: Juan Pablo Romero
"""
def imprimir_matriz(matriz):
    n_filas = len(matriz)
    n_columnas = len(matriz[0])
    contador = 0

    # para cada fila, imprime los valores separados por espacios
    while contador < n_filas:
        fila = matriz[contador]
        indice = 0
        while indice < n_columnas:
            print(str(fila[indice]).rjust(10), end = "")
            indice += 1
        # termina cada fila con una nueva línea
        print(end="\n")
        contador += 1

"""
ejercicio 10: suma o resta dos matrices y retorna el resultado. las matrices deben ser del mismo tamaño

entradas: dos matrices
salida: matriz resultante

autor: Fernando González
"""
def suma_resta_matrices(mat_1, mat_2, operación):
  if len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
    return "ERROR: LAS MATRICES DEBEN TENER LA MISMA DIMENSIÓN"

  if operación not in "+-":
    return "ERROR: LA OPERACIÓN DEBE SER \"+\" PARA SUMA Y \"-\" PARA RESTA"

  mat_resultado = []

  # por cada índice i y j, suma el valor asociado en mat_1 con el de mat_2
  for fila in range(len(mat_1)):
    lista_col = []

    for columna in range(len(mat_1[0])):
      if operación == "+":
        lista_col.append(mat_1[fila][columna] + mat_2[fila][columna])
      else:
        lista_col.append(mat_1[fila][columna] - mat_2[fila][columna])

    mat_resultado.append(lista_col)

  return mat_resultado

"""
Ejercicio 11: traspone una matriz

Entrada: matriz que se va a transponer.
Salida: matriz transpuesta.

Autor: Sebastián de Jesús Padilla Escalante
"""
def matriz_transpuesta(matriz):
    transpuesta = []
    lista_aux_1 = []
    lista_aux_2 = []
    lista_aux_3 = []
    indice_aux_1 = 0
    indice_aux_2 = 0
    indice_aux_3 = 0
    contador = 1
    corte_aux = len(matriz[0])

    columnas_final = len(matriz)
    filas_final = len(matriz[0])
    """En una matriz, todas las filas deben tener
    la misma cantidad de elementos. Por eso, se puede usar cualquier indice."""

    for ver_aux_1 in matriz: #Extrae todos los elementos de cada fila.
        for ver_aux_2 in ver_aux_1:
            lista_aux_1.append(ver_aux_2)

    indice_aux_2 = len(lista_aux_1)

    while contador <= filas_final: #Distribuye los elementos en nuevas filas.
        lista_aux_2.append(lista_aux_1[indice_aux_1:indice_aux_2:corte_aux])
        lista_aux_3.append(lista_aux_2)
        lista_aux_2 = []
        indice_aux_1 += 1
        contador += 1

    while indice_aux_3 <= len(lista_aux_3) - 1: #Se organizan las filas bien.
        transpuesta.append(lista_aux_3[indice_aux_3][0])
        indice_aux_3 += 1

    return transpuesta

"""
12: TRIANGULO DE PASCAL
ENTRADAS: Recibe un entero n >= 1
SALIDAS: Retorna una lista de tuplas representando el triángulo de Pascal
AUTOR: Juan Pablo Romero (Hecho con apoyo del programa de Daniel Monterrosa, colgado en "EJEMPLOS DE PROGRAMAS" en TecDigital
"""
def triángulo_de_pascal(n):
    fila = 1
    lista_f = []
    lista_n = []

    # para cada fila, se obtiene su lista correspondiente de su fila en el triángulo Pascal
    while fila <= n:
        elemento = lista_n
        lista_n = [1]
        maximo = fila-1

        # sumar el inicial con su sucesor
        indice_f = 1
        indice_i = 0
        # no corre en la fila 1
        while indice_f < maximo:
            lista_n.append(elemento[indice_f]+elemento[indice_i])
            indice_i += 1
            indice_f += 1
        if maximo != 0:
            lista_n.append(1)
        lista_f.append(tuple(lista_n))
        fila += 1
    return lista_f

"""
ejercicio 13: devuelve una tupla de tuplas que representa el triángulo simétrico
(de arriba o de abajo, según especificado) de una matriz diagonal

entradas: matriz cuadrada, código "A" o "D"
salida: tupla de tuplas que representa el triángulo simétrico

autor: Fernando González
"""
def triangulo_simetrico(matriz, código):
  # matrices cuadradas empiezan desde un 2 x 2
  if len(matriz) != len(matriz[0]) or len(matriz) < 2:
    return "ERROR: LA MATRIZ DEBE SER CUADRADA"

  tuplas = ()

  for i, fila in enumerate(matriz):
    if código == "A":
      posible = fila[i + 1 :]
    elif código == "D":
      posible = fila[: i]
    else:
      return "ERROR: EL CÓDIGO DEL TRIÁNGULO DEBE SER \"A\" O \"D\""

    # en la primera o última fila podría retornar vacío, se debe descartar
    if posible:
      tuplas += (tuple(posible),)

  return tuplas

"""
Ejercicio 14: crea una matriz unitaria número x número

Entrada: número que representa tanto las filas como columnas de la matriz.
Salida: matriz unitaria de las dimensiones indicadas.

Autor: Sebastián de Jesús Padilla Escalante
"""
def crear_matriz_unitaria(numero):
    filas = numero
    columnas = numero
    contador_aux_1 = 0
    contador_aux_2 = 0
    indice = 0
    unitaria = []

    while contador_aux_1 < filas:
        unitaria.append([])
        contador_aux_1 += 1

    for ver_filas in unitaria:
        while contador_aux_2 < columnas:
            ver_filas.append(0)
            contador_aux_2 += 1
        contador_aux_2 = 0

    for ver_unitaria in unitaria:
        unitaria[indice][indice] += 1
        indice += 1

    return unitaria

"""
15: MULTIPLICA MATRICES
ENTRADAS: Recibe dos matrices
SALIDAS: Retorna la multiplicacion de dichas matrices
AUTOR: Juan Pablo Romero
"""
def multiplica_matrices(matriz1, matriz2):
  # verificar que ambas matrices sean listas
  if isinstance(matriz1, list) == True and isinstance(matriz2, list) == True:
    # verificar que el tamaño de columnas de uno sea el de filas del otro
    if len(matriz1[0]) == len(matriz2):
      indice4 = 0
      n = 0
      multi = 0
      lista_sf = []
      lista_f = []
      # se usa este while para reiniciar los indices, y aumentar "indice4", la cual se usa para obtener la columna de la matriz2 por la que se va a multiplicar
      while indice4 < len(matriz2[0]):
        indice1 = 0
        indice2 = 0
        indice3 = 0
        # aqui, se obtiene la fila de la matriz1 y la columna de la matriz2
        while indice3 < len(matriz1):
          lista_c = []
          elemento1 = matriz1[indice3]
          elemento2 = matriz2[indice1]
          indice2 = 0
          multi = 0
          # con este while, se realiza la multiplicacion, multiplicando el subindice respetivo de la fila de matriz1 con el subindice de la columna de matriz2
          while indice2 < len(matriz1[0]):
            multi = multi + elemento1[indice2] * elemento2[indice4]
            indice2 += 1
            lista_c.append(multi)
            # este if es para evitar un error por estar fuera de rango
            if len(lista_c) == len(elemento1):
              break
            elemento2 = matriz2[indice2]
          lista_f.append(multi)
          indice3 += 1
        indice4 += 1
      # una vez termina, la lista_f contiene todos los elementos de la multiplicación, pero están en desorden, por lo que hay que ordenarlos y convertirlos en una matriz
      i1 = 0
      i2 = len(matriz1[0])
      lista_k = []
      lista_fn = []
      # con este while, se obtienen los respectivos digitos de las filas de la nueva matriz, se añaden como listas a lista_fn
      while i2 < len(lista_f):
        lista_k.append(lista_f[i1])
        lista_k.append(lista_f[i2])
        lista_fn.append(lista_k)
        lista_k = []
        i1 += 1
        i2 += 1
      return lista_fn
    else:
      return "ERROR: LA CANTIDAD DE COLUMNAS DE LA PRIMERA MATRIZ DEBE SER IGUAL A LA CANTIDAD DE FILAS DE LA SEGUNDA FILA"
  else:
    return "ERROR: LAS ENTRADAS DEBEN SER MATRICES"

"""
Función auxiliar para ejercicio 16
Devuelve el primer elemento de la sublista (la palabra) para el ordenamiento
"""
def obtener_clave(ver_palabra):
    return ver_palabra[0]

"""
Ejercicio 16: según una serie de líneas, devuelve una lista de listas, en donde cada palabra tiene las líneas donde aparece
Entrada: tupla de strings con líneas de texto.
Salida: lista de listas donde cada sublista tiene la palabra y las líneas donde aparece.
Autor: Sebastián de Jesús Padilla Escalante
"""
def indice_palabras(lineas):

    palabras_unicas = []

    #Se extraen las palabras de cada línea.
    for num_linea, linea in enumerate(lineas, 1):
        palabras = linea.split()
        for palabra in palabras:
            existe = False
            for ver_palabra in palabras_unicas:
                if ver_palabra[0] == palabra:
                    if num_linea not in ver_palabra[1:]:
                        ver_palabra.append(num_linea)
                    existe = True
                    break
            if not existe:
                palabras_unicas.append([palabra, num_linea])

    #Ordenar según su primer elemento
    palabras_unicas.sort(key=obtener_clave)

    #Se asegura de que los números de linea en cada lista están ordenados.
    for ver_palabra in palabras_unicas:
        ver_palabra[1:] = sorted(set(ver_palabra[1:]))

    return palabras_unicas

"""
ejercicio 17: verifica una contraseña secuencialmente, y si encuentra un error
retorna el código asociado a dicho error

entrada: string de contraseña
salida: 0, 1, 2, 3, 4 o 5 según el caso

autor: Fernando González
"""
def validar_contraseña(contraseña):
  if not isinstance(contraseña, str):
    return 9

  ##### mayúsculas
  cont = 0
  i = 0
  while cont < 2:
    # cuando ya se pasó del último índice, tuvo menos que dos mayúsculas
    if i == len(contraseña):
      return 1

    # compara el caracter con los valores ascii de A y Z
    if contraseña[i] >= "A" and contraseña[i] <= "Z":
      cont += 1

    i += 1

  ##### minúsculas
  cont = 0
  i = 0
  while cont < 2:
    # cuando ya se pasó del último índice, tuvo menos que dos minúsculas
    if i == len(contraseña):
      return 2

    # compara el caracter con los valores ascii de a y z
    if contraseña[i] >= "a" and contraseña[i] <= "z":
      cont += 1

    i += 1

  ##### números
  cont = 0
  i = 0
  while cont < 2:
    # cuando ya se pasó del último índice, tuvo menos que dos números
    if i == len(contraseña):
      return 3

    # revisa membresía en un string con todos los números
    if contraseña[i] in "0123456789":
      cont += 1

    i += 1

  ##### otros (usu. símbolos)
  cont = 0
  i = 0
  while cont < 2:
    # cuando ya se pasó del último índice, tuvo menos que dos caracteres extra
    if i == len(contraseña):
      return 4

    # revisar existencia de caracteres fuera de las mayúsculas, minúsculas y números
    if not (contraseña[i] >= "A" and contraseña[i] <= "Z") \
      and not (contraseña[i] >= "a" and contraseña[i] <= "z") \
      and not (contraseña[i] in "0123456789"):
      cont += 1

    i += 1

  ##### verificar no adyacencia de caracteres del mismo tipo
  tipo_anterior = -1
  for char in contraseña:
    if char >= "A" and char <= "Z":
      tipo = 1
    elif char >= "a" and char <= "z":
      tipo = 2
    elif char in "0123456789":
      tipo = 3
    else:
      tipo = 4

    if tipo == tipo_anterior:
      return 5

    tipo_anterior = tipo

  return 0

"""
18: MATERIAS Y ESTUDIANTES
ENTRADAS: Una lista de estudiantes, donde cada estudiante tiene su carné, nombre, y tuplas con nombres y notas de materias
SALIDAS: Retorna una lista con la informacion organizada de tal forma que cada materia esta representada por otra lista, que sigue la estructura del nombre de la materia, y una tupla por cada estudiante que lleva la materia, conteniendo el carné, nombre, y la nota de la materia
AUTOR: Juan Pablo Romero, Fernando González
"""
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

"""
Función auxiliar de ej. 18
Retornar el índice de una materia en la lista de materias, o -1 si no existe
ENTRADAS: nombre de la materia (string), materias (lista)
SALIDAS: índice (int) o -1
"""
def índice_en_materias(materia, materias):
    for i, m in enumerate(materias):
        if m[0] == materia:
            return i
    else:
        return -1

"""
ejercicio 19: extrae una submatriz a base de una matriz de entrada

entradas: matriz, cantidad de filas y columnas de la submatriz, fila y columna inicial de la submatriz
salida: submatriz

autor: Fernando González
"""
def extraer_matriz(matriz, filas, columnas, fila_inicial, columna_inicial):
  # (1) revisar tipos
  if not (isinstance(matriz, list) and isinstance(filas, int) and isinstance(columnas, int) \
          and isinstance(fila_inicial, int) and isinstance(columna_inicial, int)):
          return -1


  # en este orden para priorizar -4 y -5 antes que -2 y -3:

  # (4) revisar que la fila inicial exista en la matriz
  if len(matriz) <= fila_inicial:
    return -4

  # (5) revisar que la columna inicial exista en la matriz
  if len(matriz[0]) <= columna_inicial:
    return -5

  # (2) revisar que la cantidad de filas se puedan formar
  if len(matriz) < fila_inicial + filas:
    return -2

  # (3) revisar que la cantidad de columnas se puedan formar
  if len(matriz[0]) < columna_inicial + columnas:
    return -3


  # sabiendo que todo se cumple a cabalidad, se puede crear la submatriz
  submatriz = []
  for fila in matriz[fila_inicial : fila_inicial + filas]:
    submatriz.append(fila[columna_inicial : columna_inicial + columnas])

  return submatriz

"""
Ejercicio 20: valida si un string puede usarse como variable en Python
Entrada: string con el nombre hipotetico de una variable.
Salida: valor booleano que determina si el nombre de la variable es admitido en Python o no.

Autor: Sebastián de Jesús Padilla Escalante
"""
def validar_nombre_variable(string):
    if not isinstance(string, str):
        return False

    return string.isidentifier()
