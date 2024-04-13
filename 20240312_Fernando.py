"""
obtiene divisores de n
entrada: n (entero >= 1)
salida: los divisores
"""
def divisores(n):
    if not (isinstance(n, int) and n >= 1):
        return "ERROR: LA ENTRADA DEBE SER UN ENTERO >= 1"

    contador = 1
    while contador <= n:
        if n % contador == 0:
            print(contador)

        contador += 1

"""
devuelve si un número es primo
solución 1: revisa divisibilidad en cada número desde 2 hasta n - 1
entrada: n (entero >= 2)
salida: booleano (si es o no primo)
"""
def primo_v0(n):
    if not isinstance(n, int):
        return "ERROR: n debe ser un entero"

    if n < 2:
        return False

    contador = 2
    while contador < n:
        if n % contador == 0:
            return False

        contador += 1

    return True

"""
devuelve si un número es primo
solución 2: revisa divisibilidad desde 2 hasta sqrt(n)
entrada: n (entero >= 2)
salida: booleano (si es o no primo)
"""
def primo(n):
    if not isinstance(n, int):
        return "ERROR: n debe ser un entero"

    if n < 2:
        return False

    contador = 2

    # contador <= sqrt(n) ==> contador ^ 2 <= n
    while contador ** 2 <= n:
        if n % contador == 0:
            return False
        contador += 1

    return True

"""
obtiene todos los primos entre un rango de n a m
solución 1: dos ciclos anidados
entrada: n, m (enteros >= 2, n <= m)
salida: todos los primos en el rango
"""
def rango_primos_1(n, m):
    if not (isinstance(n, int) and isinstance(m, int)):
        return "ERROR: n y m deben ser enteros"

    if n < 2 or m < 2:
        return "ERROR: n y m deben ser mayores a 2"

    if n > m:
        return "ERROR: n debe ser menor o igual a m"

    hubo_primo = False
    while n <= m:
        contador = 2

        # contador <= sqrt(n) ==> contador ^ 2 <= n
        while contador ** 2 <= n:
            if n % contador == 0:
                break
            contador += 1
        # si nunca se salió del ciclo, n es primo
        else:
            hubo_primo = True
            print(n)
            
        n += 1

    if not hubo_primo:
        return "No hay primos"

"""
obtiene todos los primos entre un rango de n a m
solución 2: un ciclo
entrada: n, m (enteros >= 2, n <= m)
salida: todos los primos en el rango
"""
def rango_primos_2(n, m):
    if not (isinstance(n, int) and isinstance(m, int)):
        return "ERROR: n y m deben ser enteros"

    if n < 2 or m < 2:
        return "ERROR: n y m deben ser mayores a 2"

    if n > m:
        return "ERROR: n debe ser menor o igual a m"

    hubo_primo = False
    while n <= m:
        if primo(n):
            hubo_primo = True
            print(n)
            
        n += 1

    if not hubo_primo:
        return "No hay primos"

"""
obtiene el factorial de un número n
entrada: n (número natural)
salida: n!
"""
def factorial(n):
    if not (isinstance(n, int) and n >= 0):
        return "ERROR: n debe ser un número natural"

    if n == 0:
        return 1

    fact = 1
    contador = 1
    
    while contador <= n:
        fact *= contador
        contador += 1

    return fact
