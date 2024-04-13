"""
Tarea 4
Fernando Andrés González Robles
Carné 2024201276
"""

# INICIO: 4:11
# FIN: 5:03
# 52 minutos


"""
función pre-1: verifica si un número es primo
entrada: n (entero)
salida: bool
"""
def es_primo(n):
    cont = 2
    while cont ** 2 <= n:
        if n % cont == 0:
            return False
        cont += 1

    return True

"""
función pre-1: devuelve el reverso de un número
entrada: n (entero)
salida: reverso de n
"""
def reverso(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    
    return rev

"""
ejercicio 1: imprime todos los números en un rango que sean primos y palíndromos
    también imprime la cantidad de números impresos
entrada: n, m (enteros >= 2, n <= m)
salida: primos palíndromos
"""
def primos_palindromos(n, m):
    cantidad = 0
    while n <= m:
        # si es primo y el número es igual al reverso (palíndromo)
        if es_primo(n) and n == reverso(n):
            print(n)
            cantidad += 1
        n += 1

    print("Cantidad de primos palíndromos:", cantidad)
    
"""
función pre-2: retorna la suma de dígitos de un número
entrada: n (entero)
salida: suma de dígitos de n
"""
def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10

    return suma

"""
ejercicio 2: verifica si un número es bonito
    lo es cuando para un n, la suma de sus dígitos es la misma que la suma de dígitos de 3n + 11
entrada: n (número)
salida: bool
"""
def es_numero_bonito(n):
    if not isinstance(n, int) or n < 0:
        return "ERROR: DEBE SER UN NÚMERO NATURAL"

    return suma_digitos(n) == suma_digitos(3 * n + 11)

"""
ejercicio 3: encuentra las apariciones de un dígito en un número,
    y las repite cuantas veces se solicita en cada ocasión
entrada: digito, numero, repeticiones (enteros)
    digito de 0 a 9, numero >= 0, repeticiones >= 1
salida: número con dígitos repetidos
"""
def repetir_digito(digito, numero, repeticiones):
    n_nuevo = 0
    potencia_diez = 0

    while numero > 0:
        dig_actual = numero % 10

        if dig_actual == digito:
            cont = 1
        else:
            cont = repeticiones

        # lo hace "repeticiones" veces cuando es el dígito esperado
        # lo hace 1 vez si no lo es
        while cont <= repeticiones:
            n_nuevo += dig_actual * pow(10, potencia_diez)
            potencia_diez += 1
            cont += 1

        numero //= 10

    return n_nuevo

"""
ejercicio 4: verifica si un número de 3 dígitos es un número de Keith
    esto pasa si en una secuencia que empieza con los primeros 3 dígitos
    y sigue con la suma de los últimos 3 términos
    tiene al mismo número en ella
entrada: n (entero de 3 dígitos)
salida: bool
"""
def es_keith3(n):
    n1 = n // 100
    n2 = n // 10 % 10
    n3 = n % 10

    while n3 < n:
        n1, n2, n3 = n2, n3, n1 + n2 + n3

    if n3 == n:
        return True
    else:
        return False
