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
        return "Error: solo se admiten numeros naturales"

    # Valida el valor de datos
    if base != 2 and base != 5 and base != 8:
        return "Error: solo se admiten las bases 2, 5 y 8"

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

    # Valida los tipos de datos
    if isinstance(num, int) == False or num < 2:
        return "Error: La entrada debe ser un entero y >= 2"
    
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
        n += 1


"""
Ejercicio 18, Version b

Imprime todos los números primos en el rango [n, m].

Parámetros:
- n (int): El número inicial del rango.
- m (int): El número final del rango.

Imprime:
- Esta función imprime unicamente los numeros que sean primos en el rango dado.

Si los parámetros n y m no son números enteros mayores o iguales a 2, o si n es mayor que m,
se mostrará un mensaje de error.

Autor: Mauricio González
"""
def rango_primos_b(n, m):

    if isinstance(n, int) == False or isinstance(m, int) == False \
       or n < 2 or m < 2 or n > m:
        return "Error: deben ser numeros enteros, >= 2 y n debe ser <= m"
    while n <= m:
        if primo(n):
            print(n)
        n += 1


"""
Ejercicio 19

Función que encuentra y muestra los números primos gemelos en un intervalo dado.

La función solicita al usuario el inicio y fin del intervalo.
Luego verifica si los números ingresados son válidos.
A continuación, itera desde el inicio hasta el fin del intervalo e imprime los números primos gemelos encontrados.

Imprime:
    Esta funcion imprime los numeros primos gemelos encontrados en el intervalo dado.

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
    while inicio <= fin:
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

    if isinstance(num, int) == False or num < 2:
        return "Error: solo se admiten enteros >= 2"
    divisor = 2
    while num > 1:
        #Si el divisor es un factor primo
        if num % divisor == 0: 
            print(divisor, end=" x ") # Esto mostrara una "x" al final del ultimo factor primo
            num = num // divisor
        else: #Si no es un factor primo incrementa el valor
            divisor += 1
            

"""

Calcula la suma de todos los divisores de un número dado.

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
"""
def determinar_numeros_amistosos(num1, num2):

    # Valida el tipo de dato y los valores
    if isinstance(num1, int) == False or isinstance(num2, int) == False \
       or num1 < 2 or num2 < 2:
        return "Error: La entrada debe ser un entero y >= 2"
    if num1 == num2:
        return "Error: Las entradas deben ser numeros diferentes"

    # Retorna True cuando la suma de los divisores es igual al otro numero
    # Se llama a la función pre-21 localizada antes del ejercicio 15
    if suma_de_divisores(num1) == num2 and suma_de_divisores(num2) == num1:
        return True
    else:
        return False