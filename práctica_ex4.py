# ej 1
print("--- sumatoria")

def sumatoria_cuadrados_iter(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m > n:
        return -1
    
    suma = 0
    for i in range(m, n + 1):
        suma += i**2

    return suma

print(sumatoria_cuadrados_iter(4, 7))

def sumatoria_cuadrados_pila(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m > n:
        return -1

    return s_c_pila_aux(m, n)

def s_c_pila_aux(m, n):
    if m == n:
        return m ** 2

    return m ** 2 + sumatoria_cuadrados_pila(m + 1, n)

print(sumatoria_cuadrados_pila(4, 7))

def sumatoria_cuadrados_cola(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m > n:
        return -1

    return s_c_cola_aux(m, n, 0)

def s_c_cola_aux(m, n, suma):
    if m > n:
        return suma

    return s_c_cola_aux(m + 1, n, suma + m ** 2)

print(sumatoria_cuadrados_cola(4, 7))

# ej 2
print("--- pares impares")

def pares_impares_iter(num):
    if not isinstance(num, int):
        return ()

    num = abs(num)
    p_i = (0, 0)

    while num != 0:
        p, i = p_i
        if num % 2 == 0:
            p_i = (p + 1, i)
        else:
            p_i = (p, i + 1)

        num //= 10

    return p_i

print(pares_impares_iter(-18006))
print(pares_impares_iter("abc"))

def pares_impares_pila(num):
    if not isinstance(num, int):
        return ()

    if num == 0:
        return (1, 0)

    num = abs(num)
    
    return p_i_pila_aux(num)

def p_i_pila_aux(num):
    if num == 0:
        return (0, 0)
    
    sig = p_i_pila_aux(num // 10)

    if num % 2 == 0:
        return (1 + sig[0], sig[1])
    else:
        return (sig[0], 1 + sig[1])

print(pares_impares_pila(3214))
print(pares_impares_pila(0))

def pares_impares_cola(num):
    if not isinstance(num, int):
        return ()

    if num == 0:
        return (1, 0)

    num = abs(num)

    return p_i_cola_aux(num, 0, 0)

def p_i_cola_aux(num, p, i):
    if num == 0:
        return p, i
    
    if num % 2 == 0:
        return p_i_cola_aux(num // 10, p + 1, i)
    else:
        return p_i_cola_aux(num // 10, p, i + 1)

print(pares_impares_cola(1))
print(pares_impares_cola(178496))

# ej 3
print("--- matriz unitaria")

def matriz_unitaria_iter(n):
    arr = []

    for i in range(n):
        fila = [0] * n
        fila[i] = 1

        arr.append(fila)

    return arr

print(matriz_unitaria_iter(3))

def matriz_unitaria_pila(n):
    return m_u_pila_aux(n, n)

def m_u_pila_aux(m, n):
    if m == 0:
        return []

    fila = [0] * n
    fila[m - 1] = 1

    return m_u_pila_aux(m - 1, n) + [fila]

print(matriz_unitaria_pila(3))

def matriz_unitaria_cola(n, m=0, actual=[]):
    if n == m:
        return actual

    fila = [0] * n
    fila[m] = 1

    return matriz_unitaria_cola(n, m + 1, actual + [fila])

print(matriz_unitaria_cola(3))

# ej 4
print("--- tipo matriz")

def tipo_matriz_iter(mat, tipo):
    for i, fila in enumerate(mat):
        if tipo == 1 or tipo == 3:
            fila = [0] * i + fila[i:]
        
        if tipo == 2 or tipo == 3:
            fila = fila[:i + 1] + [0] * (len(mat) - 1 - i)

        mat[i] = fila

    return mat

for i in range(1, 4):
    print(tipo_matriz_iter([
        [1, 7, -2],
        [1, -3, 4],
        [3, 5, 6]
    ], i))

def tipo_matriz_pila(mat, tipo, i=0):
    if i == len(mat):
        return []

    fila = mat[i]
    
    if tipo == 1 or tipo == 3:
        fila = [0] * i + fila[i:]
    
    if tipo == 2 or tipo == 3:
        fila = fila[:i + 1] + [0] * (len(mat) - 1 - i)

    return [fila] + tipo_matriz_pila(mat, tipo, i + 1)

for i in range(1, 4):
    print(tipo_matriz_pila([
        [1, 7, -2],
        [1, -3, 4],
        [3, 5, 6]
    ], i))

def tipo_matriz_cola(mat, tipo, mat_actual=[]):
    if len(mat_actual) == len(mat):
        return mat_actual

    i = len(mat_actual)
    fila = mat[i]    

    if tipo == 1 or tipo == 3:
        fila = [0] * i + fila[i:]
    
    if tipo == 2 or tipo == 3:
        fila = fila[:i + 1] + [0] * (len(mat) - 1 - i)

    return tipo_matriz_cola(mat, tipo, mat_actual + [fila])

for i in range(1, 4):
    print(tipo_matriz_cola([
        [1, 7, -2],
        [1, -3, 4],
        [3, 5, 6]
    ], i))

# ej 5
print("--- aplanar lista")

def aplanar_lista_pila(lista):
    aplanada = []
    for elem in lista:
        if isinstance(elem, list):
            aplanada += aplanar_lista_pila(elem)
        else:
            aplanada += [elem]
    
    return aplanada

print(aplanar_lista_pila([ 10, 15, [ 5, 40], 8, [ [ 10, 75, 6], 8 ] ]))
print(aplanar_lista_pila([ [ [ [ 2], [ 99, 4, 6 ] ], 8 ], 10, 75, 15, [ 100, [ 90, 80, [ 5, 8 ] ], 85] ]))

def aplanar_lista_cola(lista, i=0, nueva_lista=[]):
    if i == len(lista):
        return nueva_lista

    elem = lista[i]
    if isinstance(elem, list):
        return aplanar_lista_cola(lista, i + 1, nueva_lista + aplanar_lista_cola(elem))
    else:
        return aplanar_lista_cola(lista, i + 1, nueva_lista + [elem])

print(aplanar_lista_cola([ 10, 15, [ 5, 40], 8, [ [ 10, 75, 6], 8 ] ]))
print(aplanar_lista_cola([ [ [ [ 2], [ 99, 4, 6 ] ], 8 ], 10, 75, 15, [ 100, [ 90, 80, [ 5, 8 ] ], 85] ]))
