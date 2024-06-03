"""
Tarea 8
Fernando Andrés González Robles
Carné 2024201276
IC1803 Taller de Programación
William Mata, grupo 4
"""

"""
ejercicio 1: obtiene, de un número m a n, la suma de el cuadrado de cada número
entradas: m, n (ints >= 0, n >= m)
salidas: int (sumatoria)

versión de pila
"""
def sumatoria_cuadrados_pila(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m > n:
        return -1

    return s_c_pila_aux(m, n)

def s_c_pila_aux(m, n):
    if m == n:
        return m ** 2

    return m ** 2 + sumatoria_cuadrados_pila(m + 1, n)

""" versión de cola """
def sumatoria_cuadrados_cola(m, n):
    if not isinstance(m, int) or not isinstance(n, int) or m > n:
        return -1

    return s_c_cola_aux(m, n, 0)

def s_c_cola_aux(m, n, suma):
    if m > n:
        return suma

    return s_c_cola_aux(m + 1, n, suma + m ** 2)

print("--- sumatoria")
print(sumatoria_cuadrados_pila(4, 7))
print(sumatoria_cuadrados_cola(4, 7))

"""
ejercicio 2: obtiene, para un número n, la cantidad de dígitos pares e impares
entrada: int (n)
salida: tuple (cantidad de pares, cantidad de impares)

versión de pila
"""
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

""" versión de cola """
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

print("--- pares impares")
print(pares_impares_pila(3214))
print(pares_impares_pila(0))
print(pares_impares_cola(1))
print(pares_impares_cola(178496))

"""
ejercicio 3: recibe una lista de elementos que deben o no estar en sublistas,
    y retorna una lista donde los elementos de sublistas pasan a la principal
entrada: list (lista de elementos y posibles sublistas)
salida: list (lista aplanada)

versión de pila
"""
def aplanar_lista_pila(lista):
    aplanada = []
    for elem in lista:
        if isinstance(elem, list):
            aplanada += aplanar_lista_pila(elem)
        else:
            aplanada += [elem]
    
    return aplanada

""" versión de cola """
def aplanar_lista_cola(lista, i=0, nueva_lista=[]):
    if i == len(lista):
        return nueva_lista

    elem = lista[i]
    if isinstance(elem, list):
        return aplanar_lista_cola(lista, i + 1, nueva_lista + aplanar_lista_cola(elem))
    else:
        return aplanar_lista_cola(lista, i + 1, nueva_lista + [elem])

print("--- aplanar lista")
print(aplanar_lista_pila([ 10, 15, [ 5, 40], 8, [ [ 10, 75, 6], 8 ] ]))
print(aplanar_lista_pila([ [ [ [ 2], [ 99, 4, 6 ] ], 8 ], 10, 75, 15, [ 100, [ 90, 80, [ 5, 8 ] ], 85] ]))
print(aplanar_lista_cola([ 10, 15, [ 5, 40], 8, [ [ 10, 75, 6], 8 ] ]))
print(aplanar_lista_cola([ [ [ [ 2], [ 99, 4, 6 ] ], 8 ], 10, 75, 15, [ 100, [ 90, 80, [ 5, 8 ] ], 85] ]))

"""
ejercicio 4: recibe una matriz y retorna una lista con la diagonal numerada con positivo o negativo
    diagonal principal es 0, diagonales positivas desplazan la columna de inicio, diagonales negativas desplazan la columna
entradas: list (matriz cuadrada), int (número de diagonal)
salida: list (elementos de la diagonal)

versión de pila
"""
def extrae_diagonal_pila(matriz, diagonal):
    if not isinstance(matriz, list) or not len(matriz) or len(matriz) != len(matriz[0]):
        return "ERROR: NO ES CUADRADA"
    
    if abs(diagonal) >= len(matriz):
        return "ERROR: NO EXISTE LA DIAGONAL"

    # establecer fila y columna de inicio
    i = j = 0
    if diagonal >= 0:
        j = diagonal
    else:
        i = -diagonal

    return ext_diag_pila_aux(matriz, i, j)

def ext_diag_pila_aux(matriz, fila_inicio, col_inicio):
    # no añadir elementos cuando se pasa de los límites
    if fila_inicio >= len(matriz) or col_inicio >= len(matriz):
        return []

    return [matriz[fila_inicio][col_inicio]] + ext_diag_pila_aux(matriz, fila_inicio + 1, col_inicio + 1)

""" versión de cola """
def extrae_diagonal_cola(matriz, diagonal):
    if not isinstance(matriz, list) or not len(matriz) or len(matriz) != len(matriz[0]):
        return "ERROR: NO ES CUADRADA"
    
    if abs(diagonal) >= len(matriz):
        return "ERROR: NO EXISTE LA DIAGONAL"

    # establecer fila y columna de inicio
    i = j = 0
    if diagonal >= 0:
        j = diagonal
    else:
        i = -diagonal

    return ext_diag_cola_aux(matriz, i, j)

def ext_diag_cola_aux(matriz, fila_inicio, col_inicio, diagonal=[]):
    # no añadir elementos cuando se pasa de los límites
    if fila_inicio >= len(matriz) or col_inicio >= len(matriz):
        return diagonal

    return ext_diag_cola_aux(matriz, fila_inicio + 1, col_inicio + 1, diagonal + [matriz[fila_inicio][col_inicio]])


print("--- extraer diagonal")
print(extrae_diagonal_pila([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], 2))
print(extrae_diagonal_pila([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], -3))
print(extrae_diagonal_pila([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], 8))
print(extrae_diagonal_pila([[20, 50, 60], [15, 20, 16]], 1))
print(extrae_diagonal_cola([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], 2))
print(extrae_diagonal_cola([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], -3))
print(extrae_diagonal_cola([[20, 50, 60, 70, 80], [15, 20, 16, 40, 50], [30, 56, 60, 25, 30], [41, 85, 90, 64, 70], [68, 43, 12, 24, 16]], 8))
print(extrae_diagonal_cola([[20, 50, 60], [15, 20, 16]], 1))

"""
ejercicio 5: crear y probar una clase que maneja métodos de tiempo
"""
class Tiempo:
    def __init__(self, horas: int, minutos: int, segundos: int):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
    
    def get_tiempo(self):
        # el parámetro :02 del f string permite llenar con ceros hasta llegar a 2 dígitos
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"

    def sumar_tiempos(self, tiempo_2):
        segundos = self.segundos + tiempo_2.segundos
        # quedarse con el residuo de la suma, el cociente se pasa a los minutos
        carry, segundos = divmod(segundos, 60)
        minutos = carry + self.minutos + tiempo_2.minutos
        carry, minutos = divmod(minutos, 60)
        horas = carry + self.horas + tiempo_2.horas

        return Tiempo(horas, minutos, segundos)

def probar_clase():
    tiempo_1 = Tiempo(13, 20, 30)
    tiempo_2 = Tiempo(2, 10, 50)

    tiempo_suma = tiempo_1.sumar_tiempos(tiempo_2)
    print(tiempo_suma.get_tiempo())

print("--- tiempo")
probar_clase()