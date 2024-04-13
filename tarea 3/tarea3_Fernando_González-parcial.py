"""
Tarea 3: práctica para examen 1
Fernando Andrés González Robles
Mauricio González Prendas
Rodrigo Sebastián Donoso Chaves
"""

"""
función 1: devuelve el factorial de un número
entrada: n (número natural)
salida: n!
"""
def factorial(n):
    if not (isinstance(n, int) and n >= 0):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO NATURAL"

    resultado = 1
    contador = 1
    while contador <= n:
        resultado *= contador
        contador += 1

    return resultado

"""
función 2: pasa una calificación de escala numérica a alfabética
entrada: calificación (número natural entre 0 y 100)
salida: calificación en escala numérica
"""
def calificación(nota):
    if not (isinstance(nota, int) and nota >= 0 and nota <= 100):
        return "ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100"
    
    if nota >= 90:
        return "A - Excelente (Aprobado)"
    elif nota >= 80:
        return "B - Bien (Aprobado)"
    elif nota >= 70:
        return "C - Suficiente (Aprobado)"
    elif nota >= 50:
        return "D - Deficiente (Reprobado)"
    else:
        return "F - Muy deficiente (Reprobado)"

"""
función 3: retorna la sumatoria de números en un rango
entrada: inicio y fin (números enteros, inicio <= fin)
salida: sumatoria
"""
def sumatoria(inicio, fin):
    if not (isinstance(inicio, int) and isinstance(fin, int)):
        return "ERROR: LAS ENTRADAS DEBEN SER NÚMEROS ENTEROS"
    
    if inicio > fin:
        return "ERROR: EL INICIO DEL RANGO DEBE SER <= AL FIN DEL RANGO"

    resultado = 0
    while inicio <= fin:
        resultado += inicio
        inicio += 1

    return resultado

"""
función 4: retorna la suma y la multiplicación de los dígitos de un número
entrada: n (número natural)
salida: (suma, multiplicación) de los dígitos
"""
def suma_multiplica_digitos(n):
    if not (isinstance(n, int) and n >= 0):
        return "ERROR: EL NÚMERO DEBE SER NATURAL"
    
    if n == 0:
        return 0, 0

    suma = 0
    mult = 1

    while n > 0:
        dig = n % 10
        suma += dig
        mult *= dig
        
        n //= 10

    return suma, mult

"""
función 5: retorna la cantidad de pares e impares en un número
entrada: n (número natural)
salida: (pares, impares)
"""
def contar_pares_impares(n):
    if not (isinstance(n, int) and n >= 0):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO NATURAL"

    pares = impares = 0

    if n == 0:
        pares = 1
    
    while n > 0:
        if n % 10 % 2 == 0:
            pares += 1
        else:
            impares += 1

        n //= 10

    return pares, impares

"""
función 11: recibe un número y lo retorna al revés, manteniendo el signo
entrada: n (número entero)
salida: número al revés
"""
def numero_al_reves(n):
    if not isinstance(n, int):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO ENTERO"

    reves = 0
    usar_n = abs(n)
    while usar_n > 0:
        reves = reves * 10 + usar_n % 10
        usar_n //= 10

    if n < 0:
        return -reves
    else:
        return reves   

""". 
función 12: verifica si un número es palíndromo, usando numero_al_reves()
entrada: n (número entero)
salida: booleano (si es o no palíndromo)
"""
def palindromo(n):
    if not isinstance(n, int):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO ENTERO"
    
    return abs(n) == abs(numero_al_reves(n))

"""
función 13: imprime los primeros n números naturales palíndromos
entrada: n (número entero >= 1)
salida: primeros n palíndromos
"""
def imprimir_palindromos(n):
    if not (isinstance(n, int) and n >= 1):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO NATURAL >= 1"

    cont_palindromos = 1
    cont_nums = 0

    # solo aumentar el cont_palindromo cuando obtiene un palíndromo,
    # pero siempre aumentar cont_nums
    while cont_palindromos <= n:
        if palindromo(cont_nums):
            print(cont_palindromos, ".  ", cont_nums)
            cont_palindromos += 1
        cont_nums += 1

"""
función pre-14, pre-24: verifica que un dígito esté en un número
entrada: dig, num (números asumidos naturales)
salida: booleano (si díg está o no en num)
"""
def digito_en_numero(dig, num):
    if num == 0:
        return dig == 0

    while num > 0:
        if dig == num % 10:
            return True
        
        num //= 10

    return False

"""
función pre-14: obtiene la cantidad de dígitos de un número
entrada: num (número asumido natural)
salida: cantidad de dígitos
"""
def digitos(n):
    if n == 0:# sin la condición
        return 1

    cont = 0
    while n > 0:
        cont += 1
        n //= 10

    return cont


"""
función 14: retorna si dos conjuntos, representados usando números enteros, son iguales
entrada: conj1, conj2 (números enteros)
salida: booleano (si son o no iguales)
"""
def igualdad(conj1, conj2):
    if not (
        isinstance(conj1, int) and isinstance(conj2, int) 
        and conj1 >= 0 and conj2 >= 0
    ):
        return "ERROR: ENTRADAS DEBEN SER NÚMEROS NATURALES"

    # primero, deben tener la misma cantidad de elementos
    # sin la condición, estaríamos probando una inclusión, no igualdad
    if digitos(conj1) != digitos(conj2):
        return False

    # ya asumiendo que sea cierto, podemos ver si cada dígito del primero está en el segundo
    while conj1 > 0:
        if not digito_en_numero(conj1 % 10, conj2):
            return False

        conj1 //= 10

    return True


"""
función pre-15: retorna la suma de divisores de un número
entrada: n (número asumido entero >= 6)
salida: suma de divisores
"""
def suma_divisores(n):
    suma_divs = 0
    cont = 1

    # revisar divisor por cada número de 1 a n (excl.)
    while cont < n:
        if n % cont == 0:
            suma_divs += cont

        cont += 1

    return suma_divs

"""
función 15: imprime los primeros n números perfectos
entrada: n (número entero >= 1)
salida: primeros n números perfectos
"""
def lista_numeros_perfectos(n):
    if not (isinstance(n, int) and n >= 1):
        return "ERROR: ENTRADA DEBE SER NÚMERO ENTERO >= 1"
    
    cont_nums = 6
    cont_perfectos = 1
    
    # revisar perfecto por cada número, y solo sumar cont_perfectos si encuentra un perfecto
    while cont_perfectos <= n:
        if suma_divisores(cont_nums) == cont_nums:
            print(cont_perfectos, "-", cont_nums)
            cont_perfectos += 1
        cont_nums += 1

"""
función 24: obtiene la diferencia simétrica entre dos conjuntos
entrada: conj1, conj2 (números naturales)
salida: diferencia simétrica entre conj1 y conj2
"""
def diferencia_simetrica(conj1, conj2):
    if not (isinstance(conj1, int) and isinstance(conj2, int) and conj1 >= 0 and conj2 >= 0):
        return "ERROR: ENTRADAS DEBEN SER NÚMEROS NATURALES"

    dif_sim = 0

    # esto va a ayudar para discernir entre una diferencia que legítimamente sea 0, y una que sea vacía
    hubo_dif_sim = False

    conj1_temp = conj1
    conj2_temp = conj2

    while conj1_temp > 0:
        dig = conj1_temp % 10

        # solo si el dígito de conj1 NO ESTÁ en conj2, vamos a actualizar dif_sim
        # también hay que verificar que no esté ya en dif_sim, por si se repiten números en conj1
        # (en teoría no deberían repetirse, pues los conjuntos no tienen elementos repetidos
        # pero algunas entradas repiten entonces se necesita asumir esta lógica)
        if not digito_en_numero(dig, conj2) and not digito_en_numero(dig, dif_sim):
            dif_sim = dif_sim * 10 + dig
            hubo_dif_sim = True

        conj1_temp //= 10

    while conj2_temp > 0:
        dig = conj2_temp % 10

        if not digito_en_numero(dig, conj1) and not digito_en_numero(dig, dif_sim):
            dif_sim = dif_sim * 10 + dig
            hubo_dif_sim = True

        conj2_temp //= 10

    if not hubo_dif_sim:
        return -1
    else:
        return dif_sim


"""
función 10: fibonacci
"""
#### REVISAR RESTRICCIONES ####
def fibonacci(n):
    n1 = 0
    n2 = 1

    n_term = 0

    cont = 2
    while cont < n:
        n_term = n1 + n2
        
        n1 = n2
        n2 = n_term

        cont += 1

    return n_term
