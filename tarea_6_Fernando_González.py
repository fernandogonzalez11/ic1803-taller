"""
Tarea 6
Fernando Andrés González Robles
Carné 2024201276

IC1803 Taller de Programación
William Mata Rodríguez
Grupo 4
"""

"""
ejercicio 1: recibe una lista de números y devuelve un diccionario con los números como llaves, y dónde están como sus valores
entrada: list (lista de números)
salida: dict (diccionario de apariciones)
"""
def compactar(nums: list) -> dict:
    apariciones = {}

    for i, num in enumerate(nums):
        if num not in apariciones:
            apariciones[num] = (i,)
        else:
            apariciones[num] = apariciones[num] + (i,)

    return apariciones

print("--- compactar")
print(compactar([ 8, 8, 8, 75, 2, 2, 2, 2, 8, 1, 1, 100, 1, 2, 75, 75 ]))

"""
ejercicio 2: recibe una lista de n diccionarios, y retorna un solo diccionario con los nombres de productos (llaves)
    y la cantidad total de ese producto (valores)
entrada: list (lista de diccionarios con la producción por fábrica)
salida: dict (diccionario con la producción total por cada producto)
"""
def pedidos_totales(fábricas: list) -> dict:
    prod_total = {}

    for fábrica in fábricas:
        for producto in fábrica:
            if producto not in prod_total:
                prod_total[producto] = fábrica[producto]
            else:
                prod_total[producto] += fábrica[producto]

    return prod_total

print("--- pedidos totales")
print(pedidos_totales([ {"tableta 10": 1000, "tableta 7": 850, "tableta 10.1": 3000}, {"tableta 7": 600, "tableta 10": 1500, "tableta 8": 500} ]))
print(pedidos_totales([{"tableta 7": 2000, "tableta 10": 800, "tableta 8": 5000}, {"tableta 10": 200}, {"tableta 10": 1000, "tableta 8": 5000} ]))

"""
ejercicio 3: dada una tupla de frases, obtiene en cuál(es) frases se encuentra cada palabra
    y las coloca en un diccionario (llave: palabra, valor: frases donde aparece)
entrada: tuple (tupla de frases)
salida: dict (diccionario de apariciones por palabra)
"""
def indice_palabras(frases: tuple) -> dict:
    dict_palabras = {}
    for i, frase in enumerate(frases):
        for palabra in frase.split(" "):
            if palabra not in dict_palabras:
                dict_palabras[palabra] = [i + 1]
            else:
                dict_palabras[palabra].append(i + 1)

    return dict_palabras

print("--- índice de palabras")
palabras = indice_palabras( ("en el aprendizaje de",
"la programación de computadoras",
"hay que practicar el desarrollo de",
"algoritmos hay que practicar mucho") )
print(indice_palabras(palabras))

"""
ejercicio 4: recibe un diccionario como el generado por el ej 3
    y lo imprime con formato. imprime las palabras en orden alfabético,
    y las apariciones están separadas por comas
entrada: dict (diccionario de apariciones de palabras)
salida: (impresión de) palabras y sus apariciones
"""
def informe_indice(palabras: dict):
    # items devuelve una lista de tuplas (ítem, valor)
    # luego, sorted las ordena. el ordenamiento por defecto 
    # se hace con los primeros valores de la tupla
    lista_palabras = sorted(palabras.items())
    print("ÍNDICE DE PALABRAS".ljust(25) + "LÍNEAS DONDE APARECE")
    for palabra, apariciones in lista_palabras:
        # convertir la lista de números a strings
        apariciones = [str(i) for i in apariciones]
        print(palabra.ljust(25) + ", ".join(apariciones))

print("--- informe índice")
informe_indice(palabras)

"""
ejercicio 5: dada una lista de palabras, retorna un diccionario con
    las palabras con máxima longitud (llaves) y sus apariciones (valores)
entrada: list (lista de palabras)
salida: dict (palabras con máxima longitud y sus apariciones)
"""
def longitudes_máximas(palabras: list) -> dict:
    pass