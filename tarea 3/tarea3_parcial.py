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

autor: Fernando González
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

autor: Fernando González
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

autor: Fernando González
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

autor: Fernando González
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

autor: Fernando González
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
función 6: encripta un número con base en otro número codificador
entrada: codificador (entero entre 1 y 9), n (número entero)
salida: número encriptado

autor: Sebastián Donoso
"""
def encriptar(codificador,n):
    if not isinstance(n,int) or n < 0:
        return "ERROR: EL NUMERO A ENCRIPTAR DEBE DE SER ENTERO MAYOR A 0"
    if codificador < 1 or codificador > 9 :
        return "ERROR: EL CODIFICADOR DEBE ESTAR ENTRE 1 Y 9"
    n_encriptado = 4
    potencia = 1
    while n>0:
        digito = n % 10
        n_encriptado += ((codificador + digito) % 10)*pow(10,potencia)
        potencia +=1
        n //= 10

    return n_encriptado


"""
función 7: obtiene la nota más alta, más baja, el promedio, notas válidas e inválidas
entrada: nota (entre 0 y 800, o negativo para salirse)
salida: nota más alta, más baja, promedio, notas válidas, notas invalidas.
autor: Sebastián Donoso
"""
def analizar_notas_admision():
    nota = 1
    nota_mayor = nota
    nota_menor = 801
    sumatoria_nota = 0
    notas_validas = 0
    notas_invalidas = 0
    
    
    while nota > 0:
        nota = int(input("Nota: "))
        if nota < 0:
            break
        elif nota <=800:
            sumatoria_nota += nota
            notas_validas += 1
            if nota > nota_mayor:
                nota_mayor = nota
            if nota < nota_menor:
                nota_menor = nota
        else:
            notas_invalidas +=1

    promedio = sumatoria_nota / notas_validas

    print("Nota más alta:", nota_mayor)
    print("Nota más baja:", nota_menor)
    print("Nota promedio:", promedio)
    print("Cantidad de notas validas (entre 0 y 800):", notas_validas)
    print("Cantidad de notas invalidas (> 800):", notas_invalidas)



"""
función 8a: obtiene las combinaciones sin repetición de un grupo de n elementos con subconjuntos de x elementos
solución 1: no utiliza funciones externas
entrada: n, x (números enteros)
salida: C(n, x)

autor: Sebastián Donoso
"""
def combinatoria_1(n,x):
    fact1 = 1
    contador1 = 1
    fact2 = 1
    contador2 = 1
    resta = n - x
    fact3 = 1
    contador3 = 1
    
    while contador1 <= n:
        fact1 *= contador1
        contador1 += 1
        while contador2 <= x:
            fact2 *= contador2
            contador2 +=1
            while contador3 <= resta:
                fact3 *= contador3
                contador3 +=1


    formula = ((fact1)//((fact2)*(fact3))) 
    return formula
    

"""
función 8b: obtiene las combinaciones sin repetición de un grupo de n elementos con subconjuntos de x elementos
utiliza la función factorial() ya definida
entrada: n, x (números enteros)
salida: C(n, x)

autor: Sebastián Donoso
"""
def combinatoria_2(n,x):
    combinatoria = (factorial(n))/(factorial(x)*(factorial(n-x)))
    return combinatoria



def fibonacci(n):
    n1 = 0
    n2 = 1
    n_term = 0
    contador = 2
    while contador < n :
        n_term = n1 + n2
        n1 = n2
        n2 = n_term
        contador+=1

    return n_term



def es_altamente_abundante(numero):
    suma_divisores_numero = suma_divisores(numero)
    i = 1
    while i < numero:
        if suma_divisores_numero <= suma_divisores(i):
            return False
        i += 1
    return True


