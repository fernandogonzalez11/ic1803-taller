import math

# índices donde se encuentra un elemento
# entradas: un elemento y una lista
# salidas: lista de índices donde se encuetra el elemento
def indices(elemento, lista):
    lista_indices = []
    indice = 0
    max_indice = len(lista) - 1
    while indice <= max_indice:
        if elemento == lista[indice]:
            lista_indices.append(indice)
            
        indice += 1

    return lista_indices

print("***** indices:", indices(100, [200, 250, 100, 125, 100]))

# lista de divisores de un entero
# entrada: número entero
# salida: lista de sus divisores
def divisores(n):
    divs = []

    cont = 1
    while cont <= n:
        if n % cont == 0:
            divs.append(cont)
        cont += 1

    return divs

print("***** divisores:", divisores(10))

# obtiene cálculos varios de notas de admisión
# entrada: lista con notas entre 0 y 800
# salida: nota más alta, más baja, promedio, notas mayores y menores al promedio
def analizar_notas_admisión(notas):
    alta = max(notas)
    baja = min(notas)
    cantidad = len(notas)
    promedio = sum(notas) / cantidad

    segun_promedio = [0] * 2
    rangos = [0] * 4
    
    i = 0
    while i < cantidad:
        nota = notas[i]
        if nota < promedio:
            segun_promedio[0] += 1
        elif nota > promedio:
            segun_promedio[1] += 1

        if nota <= 500:
            rangos[0] += 1
        elif nota <= 600:
            rangos[1] += 1
        elif nota <= 700:
            rangos[2] += 1
        else:
            rangos[3] += 1
            
        i += 1

    print("Cantidad total de notas:", cantidad)
    print("Nota más alta:", alta)
    print("Nota más baja:", baja)
    print("Nota promedio:", promedio)
    print("Cantidad de notas menores al promedio:", segun_promedio[0])
    print("Cantidad de notas mayores al promedio:", segun_promedio[1])
    print("Cantidad de notas por rangos:")
    print("    0-500:     ", rangos[0])
    print("    501-600:   ", rangos[1])
    print("    601-700:   ", rangos[2])
    print("    701-800:   ", rangos[3])

print("***** notas:") 
analizar_notas_admisión([750, 450, 795, 790, 300, 790, 600, 700, 500, 650])

# retorna lista con factoriales de otra lista de entradas
# entrada: lista con números naturales
# salida: lista con factoriales de cada número
def factoriales(numeros):
    if not isinstance(numeros, list):
        return "ERROR: LA ENTRADA DEBE SER UNA LISTA"
    
    factoriales = []
    i = 0
    while i < len(numeros):
        num = numeros[i]
        if not isinstance(num, int) or num < 0:
            return "ERROR: LA ENTRADA DEBE SER UNA LISTA DE NÚMEROS NATURALES"

        factoriales.append(math.factorial(num))
        i += 1 

    return factoriales

print("***** factoriales:")
print(factoriales([5, 0, 6, 10, 4]))
print(factoriales((5, 0, 6, 1, 4)))
print(factoriales([5, 0, "HOLA", 4]))

# retorna una lista con los primeros n términos de la secuencia de fibonacci
# entrada: número entero
# salida: n términos de fibonacci como una lista
def sucesión_fibonacci(n):
    terminos  = [0, 1]
    if n < 3:
        return terminos[:n]

    term = 2
    while term < n:
        terminos.append(terminos[-1] + terminos[-2])
        term += 1

    return terminos

print("***** fibs:", sucesión_fibonacci(12))
