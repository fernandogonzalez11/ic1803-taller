"""
Tarea 3: práctica para examen 1
IC1803 Taller de Programación
William Mata Rodríguez, grupo 4

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
función 6: separa a un número en sus dígitos pares e impares
entrada: n (número natural)
salida: (pares, impares) ("No hay" si alguno de los dos no tiene)

Autor: Sebastián Donoso
"""
def pares_impares(n):
    if not isinstance(n, int) or n < 0:
        return "ERROR: LA ENTRADA DEBE SER UN NUMERO NATURAL"
    pares = 0
    impares = 0
    potencia1 = 0
    potencia2 = 0

    hubo_pares = hubo_impares = False

    while n > 0:
        digito = n % 10
        
        if digito % 2 == 0:
            pares += digito * pow(10, potencia1)
            potencia1 += 1
            hubo_pares = True
        else:
            impares += digito * pow(10, potencia2)
            potencia2 += 1
            hubo_impares = True

        n //= 10

    if not hubo_pares:
        return "No hay", impares
    elif not hubo_impares:
        return pares, "No hay"
    else:
        return pares, impares


"""
función 7: encripta un número con base en otro número codificador
entrada: codificador (entero entre 1 y 9), n (número entero)
salida: número encriptado

autor: Sebastián Donoso
"""
def encriptar(codificador, n):
    n_encriptado = 4
    potencia = 1
    while n > 0:
        digito = n % 10
        n_encriptado += ((codificador + digito) % 10) * pow(10, potencia)
        potencia += 1
        n //= 10

    return n_encriptado


"""
función 8: obtiene la nota más alta, más baja, el promedio, notas válidas e inválidas
entrada: nota (entre 0 y 800, o negativo para salirse)
salida: nota más alta, más baja, promedio, notas válidas, notas invalidas.
autor: Sebastián Donoso
"""
def analizar_notas_admisión():
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
función 9a: obtiene las combinaciones sin repetición de un grupo de n elementos con subconjuntos de x elementos
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
función 9b: obtiene las combinaciones sin repetición de un grupo de n elementos con subconjuntos de x elementos
utiliza la función factorial() ya definida
entrada: n, x (números enteros)
salida: C(n, x)

autor: Sebastián Donoso
"""
def combinatoria_2(n, x):
    combinatoria = factorial(n) // (factorial(x) * (factorial(n - x)))
    return combinatoria


"""
función 10: calcula el n-ésimo término de la secuencia de Fibonacci
entrada: n (número entero >= 1)
salida: F(n) (término n de la secuencia)

autor: Sebastián Donoso
"""
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


"""
función 11: recibe un número y lo retorna al revés, manteniendo el signo
entrada: n (número entero)
salida: número al revés

autor: Fernando González
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

"""
función 12: verifica si un número es palíndromo, usando numero_al_reves()
entrada: n (número entero)
salida: booleano (si es o no palíndromo)

autor: Fernando González
"""
def palindromo(n):
    if not isinstance(n, int):
        return "ERROR: ENTRADA DEBE SER UN NÚMERO ENTERO"
    
    return abs(n) == abs(numero_al_reves(n))

"""
función 13: imprime los primeros n números naturales palíndromos
entrada: n (número entero >= 1)
salida: primeros n palíndromos

autor: Fernando González
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
función pre-14, pre-22, pre-24: verifica que un dígito esté en un número
entrada: dig, num (números asumidos naturales)
salida: booleano (si díg está o no en num)

autor: Fernando González
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

autor: Fernando González
"""
def digitos(n):
    if n == 0:
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

autor: Fernando González
"""
def igualdad(conj1, conj2):
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
función pre-15, pre-21

Calcula la suma de todos los divisores de un número dado, sin incluirlo a sí mismo.

Parámetros:
num1 (int): El número del cual se desean calcular los divisores.

Retorna:
int: La suma de todos los divisores del número dado.

Autor: Mauricio González
"""
def suma_de_divisores(num1):
    # Inicializa las variables a utilizar
    resultado = 0
    divisor = 1
    while divisor < num1:
        # Suma el divisor solo si el residuo es 0
        if num1 % divisor == 0:
            resultado += divisor
        divisor += 1
    return resultado

"""
función 15: imprime los primeros n números perfectos
entrada: n (número entero >= 1)
salida: primeros n números perfectos

autor: Fernando González
"""
def lista_numeros_perfectos(n):
    cont_nums = 6
    cont_perfectos = 1
    
    # revisar perfecto por cada número, y solo sumar cont_perfectos si encuentra un perfecto
    while cont_perfectos <= n:
        if suma_de_divisores(cont_nums) == cont_nums:
            print(cont_perfectos, "-", cont_nums)
            cont_perfectos += 1
        cont_nums += 1

"""
Ejercicio 16

Convierte un número en base 10 a base 2, 5 o 8.

Parámetros:
    num (int): El número en base 10 a convertir.
    base (int): La base a la cual se desea convertir el número. Solo se admiten las bases 2, 5 y 8.

Retorna:
    int: El número convertido a la base especificada.

Restricciones:
    Devuelve error si el número no es un número natural o la base no es 2, 5 o 8.

Autor: Mauricio González
"""
def base10a258(num, base):

    # Valida los tipos de datos
    if isinstance(num, int) == False or isinstance(base, int) == False or num < 0:
        return "ERROR: EL NÚMERO A CONVERTIR DEBE SER UN NÚMERO NATURAL"

    # Valida el valor de datos
    if base != 2 and base != 5 and base != 8:
        return "ERROR: BASE DE CONVERSIÓN DEBE SER 2, 5, 8"

    # Inicializa las variables a utilizar
    resultado = 0
    potencia = 1

    while num > 0:
        residuo = num % base
        # Utiliza la potencia para unir el numero en la variable resultado
        resultado += residuo * potencia
        potencia = potencia * 10
        num = num // base

    return resultado


"""
Ejercicio 17

Determina si un número es primo o no.

Parámetros:
num (int): El número a evaluar.

Retorna:
bool: True si el número es primo, False en caso contrario.

Autor: Mauricio González
"""
def primo(num):

    raiz = int(num ** 0.5)
    divisor = 2
    # Mientras divisor sea <= que la raiz cuadrada de num
    while divisor <= raiz:
        # Si el numero no tiene residuo significa que no es primo, por lo que retorna False
        if num % divisor == 0:
            return False
        divisor += 1
    return True


"""
Ejercicio 18, Version a

Función que imprime todos los números primos en el rango [n, m].

Parámetros:
- n (int): El número inicial del rango.
- m (int): El número final del rango.

Retorna:
- None: Esta función no retorna ningún valor, simplemente imprime los números primos en el rango.

Restricciones:
- n y m deben ser números enteros mayores o iguales a 2.
- n debe ser menor o igual a m.

Autor: Mauricio González
"""
def rango_primos_a(n, m):

    if isinstance(n, int) == False or isinstance(m, int) == False \
       or n < 2 or m < 2 or n > m:
        return "Error: deben ser numeros enteros, >= 2 y n debe ser <= m"

    hubo_primos = False
    while n <= m:
        # Calcula la raíz cuadrada de n
        raiz = int(n ** 0.5)
        divisor = 2
        es_primo = True
        # Verifica si n es divisible por algún número desde 2 hasta la raíz cuadrada de n
        while divisor <= raiz:
            if n % divisor == 0:
                es_primo = False
                break
            divisor += 1
        # Si n es primo, lo imprime
        if es_primo:
            print(n)
            hubo_primos = True
        n += 1

    if not hubo_primos:
        print("No hay primos")


"""
Ejercicio 18, Version b

Imprime todos los números primos en el rango [n, m].

Parámetros:
- n (int): El número inicial del rango.
- m (int): El número final del rango.

Imprime:
- Esta función imprime únicamente los números que sean primos en el rango dado.

Si los parámetros n y m no son números enteros mayores o iguales a 2, o si n es mayor que m,
se mostrará un mensaje de error.

Autor: Mauricio González
"""
def rango_primos_b(n, m):

    if isinstance(n, int) == False or isinstance(m, int) == False \
       or n < 2 or m < 2 or n > m:
        return "Error: deben ser numeros enteros, >= 2 y n debe ser <= m"

    hubo_primos = False
    while n <= m:
        if primo(n):
            print(n)
            hubo_primos = True
        n += 1

    if not hubo_primos:
        print("No hay primos")


"""
Ejercicio 19

Función que encuentra y muestra los números primos gemelos en un intervalo dado.

La función solicita al usuario el inicio y fin del intervalo.
Luego verifica si los números ingresados son válidos.
A continuación, itera desde el inicio hasta el fin del intervalo e imprime los números primos gemelos encontrados.

Imprime:
    Esta función imprime los numeros primos gemelos encontrados en el intervalo dado.

Autor: Mauricio González
"""
def primos_gemelos():

    inicio = int(input("Inicio del intervalo: "))
    fin = int(input("Fin del intervalo: "))

    if inicio < 2 or fin < 2:
        return "Error: solo se admiten enteros >= 2"
    if inicio > fin:
        return "Error: el inicio debe ser menor al final del intervalo"

    print("Primos gemelos:")
    # los últimos dos números no pueden ser el primero del par de gemelos
    while inicio <= fin - 2:
        # Si el numero y el siguiente con diferencia de 2 es primo imprime el par
        if primo(inicio) and primo(inicio + 2):
            print(inicio, "y", inicio + 2)
        inicio += 1


"""
Ejercicio 20

Esta función calcula y muestra los factores primos de un número entero mayor o igual a 2.

Parámetros:
- num: Número entero mayor o igual a 2.

Imprime:
- Imprime los factores primos del número dado.

Restriciones:
    Si el parámetro num no es un número entero mayor o igual a 2, la función retorna un mensaje de error.

Autor: Mauricio González
"""
def factores_primos(num):

    divisor = 2
    while num > 1:
        #Si el divisor es un factor primo
        if num % divisor == 0: 
            if num // divisor == 1:
                print(divisor)
            else:
                print(divisor, end=" x ") # Esto mostrara una "x" al final del ultimo factor primo

            num = num // divisor
        else: #Si no es un factor primo incrementa el valor
            divisor += 1


"""
Ejercicio 21

Determina si dos números son amistosos.

Los números amistosos son aquellos en los que la suma de los divisores propios de uno es igual al otro número,
y viceversa.

Parámetros:
    num1 (int): El primer número a evaluar.
    num2 (int): El segundo número a evaluar.

Retorna:
    bool: Devuelve True si los números son amistosos, False si no lo son.
                

Restricciones:
    Si hay algún error en las entradas, devuelve un mensaje de error.

Autor: Mauricio González
"""
def determinar_numeros_amistosos(num1, num2):

    # Valida el tipo de dato y los valores
    if isinstance(num1, int) == False or isinstance(num2, int) == False \
       or num1 < 2 or num2 < 2:
        return "ERROR: LAS ENTRADAS DEBEN SER NÚMEROS NATURALES >= 2"
    if num1 == num2:
        return "ERROR: LAS ENTRADAS DEBEN SER NÚMEROS DIFERENTES"

    # Retorna True cuando la suma de los divisores es igual al otro numero
    # Se llama a la función pre-21 localizada antes del ejercicio 15
    if suma_de_divisores(num1) == num2 and suma_de_divisores(num2) == num1:
        return True
    else:
        return False


"""
función 22: forma un conjunto con un número en el mismo formato, tal que sus elementos no se repitan
entrada: numero (número natural)
salida: conjunto en formato de número natural

autor: Sebastián Donoso
"""
def formar_conjunto(numero):
    conjunto = 0

    while numero > 0:
        dig = numero % 10

        # se llama a la función pre-22 localizada 
        if not digito_en_numero(dig, conjunto):
            conjunto = conjunto * 10 + dig

        numero //= 10

    return conjunto

"""
función 23: imprime todos los números palíndromos en un rango
entrada: inicio, fin (enteros, leídos)
salida: todos los palíndromos entre inicio y fin

autor: Sebastián Donoso
"""
def obtener_palindromos():
    inicio = int(input("Inicio del intervalo: "))
    fin = int(input("Fin del intervalo: "))
    cantidad = 0
    while inicio <= fin:
        if palindromo(inicio) == True:
            print(inicio)
            cantidad += 1
        inicio += 1

    print("Cantidad de palíndromos: ", cantidad)


"""
función 24: obtiene la diferencia simétrica entre dos conjuntos
entrada: conj1, conj2 (números naturales)
salida: diferencia simétrica entre conj1 y conj2

autor: Fernando González
"""
def diferencia_simetrica(conj1, conj2):
    dif_sim = 0

    # esto va a ayudar para discernir entre una diferencia que legítimamente sea 0, y una que sea vacía
    hubo_dif_sim = False

    conj1_temp = conj1
    conj2_temp = conj2

    while conj1_temp > 0:
        dig = conj1_temp % 10

        # solo si el dígito de conj1 NO ESTÁ en conj2, vamos a actualizar dif_sim
        # también hay que verificar que no esté ya en dif_sim, por si se repiten números en conj1
        
        # se llama a la función pre-24 localizada antes del ejercicio 14
        if not digito_en_numero(dig, conj2) and not digito_en_numero(dig, dif_sim):
            dif_sim = dif_sim * 10 + dig
            hubo_dif_sim = True

        conj1_temp //= 10

    # mismo proceso con conj2
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
función 25: retorna si un número es altamente abundante
entrada: numero (número natural)
salida: booleano (si es o no altamente abundante)

autor: Sebastián Donoso
"""
def es_altamente_abundante(numero):
    suma_divisores_numero = suma_de_divisores(numero)
    i = 1
    while i < numero:
        if suma_divisores_numero <= suma_de_divisores(i):
            return False
        i += 1
    return True


