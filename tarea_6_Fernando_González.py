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

print()
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

print()
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

print()
print("--- informe índice")
informe_indice(palabras)

"""
ejercicio 5: dada una lista de palabras, retorna un diccionario con
    las palabras con máxima longitud (llaves) y sus apariciones (valores)
entrada: list (lista de palabras)
salida: dict (palabras con máxima longitud y sus apariciones)
"""
def longitudes_máximas(palabras: list) -> dict:
    # validar que sea una lista
    if not isinstance(palabras, list):
        return "ERROR: EL VALOR DE ENTRADA DEBE SER UNA LISTA"
    
    dict_palabras_máximas = {}
    max_len = 0

    for i, palabra in enumerate(palabras):
        # validar que cada elemento de la lista sea string
        if not isinstance(palabra, str):
            return "ERROR: TODOS LOS ELEMENTOS DE LA LISTA DEBEN SER STRINGS"
        
        # si hay un nuevo máximo, reemplazar el diccionario con la nueva palabra
        if len(palabra) > max_len:
            max_len = len(palabra)
            dict_palabras_máximas = { palabra: (i,) }
        # si el máximo se mantiene, se añade la aparición al diccionario
        elif len(palabra) == max_len:
            if palabra not in dict_palabras_máximas:
                dict_palabras_máximas[palabra] = (i,)
            else:
                dict_palabras_máximas[palabra] += (i,)
        # si es menor al máximo, no se hace nada

    return dict_palabras_máximas

print()
print("--- longitudes máximas")
print(longitudes_máximas( [ "de", "y", "hola", "al", "hola", "allá" ] ))
print(longitudes_máximas( [ "sin", "hay", "es", "su", "sin", "con", "su", "con", "sin", "a", "con", "sin" ] ))
print(longitudes_máximas( ("de", "y", "hola", "al", "hola", "allá") ))
print(longitudes_máximas( [ "de", "346234", "hola", True, 2023, "allá" ] ))


"""
ejercicio 6: se tienen las siguientes matrices
- proveedores (1 a m) con costos por material (mat_1 a mat_n)
- proyectos (1 a p) con cantidad de material necesitado (mat_1 a mat_n)
por cada proyecto, se evalúa cuál proveedor brinda el costo total menor,
    y se añade a un diccionario con el número de proyecto (llave) y una tupla (i_proveedor, costo_total)
"""
def seleccionar_proveedores(proveedores, proyectos):
    seleccionados = {}

    # para cada proyecto se selecciona el mejor proveedor
    for i, proyecto in enumerate(proyectos):
        min_proveedor = (0, 0)

        for j, proveedor in enumerate(proveedores):
            costo_total = 0
            # se obtiene la cantidad y costo simultáneamente con ambas listas
            # y se multiplican y suman al costo total
            for cantidad, costo in zip(proyecto, proveedor):
                costo_total += cantidad * costo

            # actualizar el mínimo si es el primero o el actual es menor
            if min_proveedor[1] == 0 or costo_total < min_proveedor[1]:
                min_proveedor = (j + 1, costo_total)

        # añadir la tupla de costo mínimo al diccionario
        seleccionados[i + 1] = min_proveedor

    return seleccionados

print()
print("--- seleccionar proveedores")
print(seleccionar_proveedores([ [8, 13, 6, 6], [6, 12, 7, 8], [7, 14, 6, 7] ],
[ [24, 5, 12, 18], [20, 7, 15, 20], [20, 4, 15, 15] ]))
        
"""
ejercicio 7: dada una matriz de cualquier tamaño, un índice (i, j) inicial y uno final,
    retornar índices y valores entre esos índices tal que formen una L
entrada: list (matriz n x m), tuple (inicio), tuple (final)
salida: list (elementos como tuplas tal que forman una L)
"""
def extraer_ele(matriz, inicio, final):
    lista_L = []
    # se usan rangos en lugar de comparaciones de longitud
    # para no tener que verificar también que los índices sean números
    rango_filas, rango_cols = (range(len(matriz)), range(len(matriz[0])))

    if inicio[0] not in rango_filas:
        return f"ERROR: NO EXISTE FILA {inicio[0]}"
    
    if final[0] not in rango_filas:
        return f"ERROR: NO EXISTE FILA {final[0]}"

    if inicio[1] not in rango_cols:
        return f"ERROR: NO EXISTE COLUMNA {inicio[1]}"

    if final[1] not in rango_cols:
        return f"ERROR: NO EXISTE COLUMNA {final[1]}"

    # si pasa estas validaciones se tiene que los índices son números
    # en la matriz. se comprueba que la fila/col de inicio sea menor a la de final
    if inicio[0] >= final[0]:
        return f"ERROR: FILA INICIAL DEBE SER MENOR A LA FINAL"
    
    if inicio[1] >= final[1]:
        return f"ERROR: COLUMNA INICIAL DEBE SER MENOR A LA FINAL"
    
    # ahora se tienen índices que son certeros harán una L
    # se empieza añadiendo los valores verticales
    # se recorre desde la fila inicial (incl.) a la final (incl.)
    for i, fila in enumerate(matriz[inicio[0] : final[0] + 1]):
        # la porción fila tiene un offset de inicio[0] que hay que añadir
        # se toma como valor el elemento inicio[1] de la fila
        lista_L.append((i + inicio[0], inicio[1], fila[inicio[1]]))
    
    # ahora se añaden los valores horizontales en la fila de final
    # se recorre desde la columna inicial (excl.) a la final (incl.)
    # aquí tambien hay un offset pero de inicio[1] + 1 en la columna
    for i, elem in enumerate(matriz[final[0]][inicio[1] + 1 : final[1] + 1]):
        lista_L.append((final[0], i + inicio[1] + 1, elem))

    return lista_L

print()
print("--- extraer L")
print(extraer_ele([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (0, 1), (2, 2)))
print(extraer_ele([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (1, 0), (3, 2)))
print(extraer_ele([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], ("A", 1), (2, 2)))
print(extraer_ele([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (1, 1), (20, 2)))
print(extraer_ele([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (0, 12), (1, 2)))
print(extraer_ele ([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (0, 1), (2, 25)))
print(extraer_ele ([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (0, 1), (0, 2)))
print(extraer_ele ([ [10, 15, 20], [25, 30, 35], [40, 45, 50], [55, 60, 65] ], (2, 2), (3, 1)))