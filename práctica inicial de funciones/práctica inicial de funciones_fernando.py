# Fernando González
# carné 2024201276

# función 1: descompone un número de 3 dígitos en sus unidades, decenas y centenas respectivamente
def descomponer_numero(n):
    if n < 100 or n >= 1000:
        return "ERROR: el número no es de 3 dígitos"

    unidades = n % 10
    decenas = n // 10 % 10
    centenas = n // 100
    return unidades, decenas, centenas

# función 2: descompone un número de 3 dígitos en sus unidades, decenas y centenas respectivamente
# no obstante, en lugar de usar parámetros, la función lee e imprime directamente los datos
def descomponer_numero_v2():
    n = int(input("Proporcione el número por descomponer: "))

    if n < 100 or n >= 1000:
        return "ERROR: el número no es de 3 dígitos"

    print("Unidades en el número:", n % 10)
    print("Decenas en el número:", n // 10 % 10)
    print("Centenas en el número:", n // 100)

# función 3: componer un número dados las unidades, decenas y centenas brindadas respectivamente
def componer_numero(u, d, c):
    if u < 0 or d < 0 or c <= 0:
        return "ERROR: las unidades proporcionadas no se pueden componer a un número de 3 dígitos"

    return c * 100 + d * 10 + u

# función 4: componer un número dados las unidades, decenas y centenas brindadas respectivamente
# no obstante, en lugar de usar parámetros, la función lee e imprime directamente los datos
def componer_numero_v2():
    u = int(input("Unidades: "))
    d = int(input("Decenas: "))
    c = int(input("Centenas: "))

    if u < 0 or d < 0 or c <= 0:
        return print("ERROR: las unidades proporcionadas no se pueden componer a un número de 3 dígitos")

    print("Número representado:", c * 100 + d * 10 + u)

# función 5: recibe un número de 5 dígitos y retorna el número con los dígitos al revés
def al_reves(n):
    if n < 10000 or n >= 100000:
        return "ERROR: el número no es de 5 dígitos"
    
    n1 = n // 10000
    n2 = n // 1000 % 10
    n3 = n // 100 % 10
    n4 = n // 10 % 10
    n5 = n % 10
    return n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1

# función 6: lee una cantidad de segundos e imprime sus horas, minutos y segundos respectivos
def tiempo():
    s = int(input("Cantidad de segundos: "))

    if s < 0:
        return "ERROR: los segundos deben ser un número positivo"
    
    print("Representan:")
    print(s // 3600, "horas")
    print(s % 3600 // 60, "minutos")
    print(s % 3600 % 60, "segundos")

# función 7: calcular la cantidad de pinos, eucaliptos y cedros por reforestar dada una cantidad de hectáreas
def reforestar(hectareas):
    if hectareas <= 0:
        return "ERROR: las hectáreas deben ser un número positivo"
    
    m2 = hectareas * 10000
    pinos = int(m2 * 0.5 * 8 / 10)
    eucaliptos = int(m2 * 0.3)
    cedros = int(m2 * 0.2 * 10 / 18)

    return pinos, eucaliptos, cedros

# función 8: lee el tiempo terrestre y el marítimo en su formato específico, e imprime su suma en el mismo formato
def tiempo_total():
    # leer y verificar
    maritima = int(input("Tiempo que duró la parte marítima: "))
    terrestre = int(input("Tiempo que duró la parte terrestre: "))

    if maritima < 100000 or maritima >= 1000000 or terrestre < 100000 or terrestre >= 1000000:
        return print("ERROR: los tiempos deben ser de 6 dígitos, en formato hhmmss")

    # horas
    mar_h = maritima // 10000
    ter_h = terrestre // 10000

    # dada la condición de arriba, el número nunca llegará a tener más de 99 horas

    # minutos
    mar_m = maritima // 100 % 100
    ter_m = terrestre // 100 % 100

    if mar_m < 0 or mar_m > 59 or ter_m < 0 or ter_m > 59:
        return print("ERROR: los minutos deben ser entre 00 y 59")
    
    # segundos
    mar_s = maritima % 100
    ter_s = terrestre % 100

    if mar_s < 0 or mar_s > 59 or ter_s < 0 or ter_m > 59:
        return print("ERROR: los segundos deben ser entre 00 y 59")
    
    # calcular total y formatear
    total_s = (mar_h + ter_h) * 3600 + (mar_m + ter_m) * 60 +  (mar_s + ter_s)
    total_h = total_s // 3600
    total_m = total_s % 3600 // 60
    total_s = total_s % 3600 % 60
    total_formato = total_h * 10000 + total_m * 100 + total_s
    print("Tiempo total:", total_formato)

# función 9: imprime la tabla de multiplicar de un número leído
def tabla_de_multiplicar():
    num = int(input("Tabla de multiplicar del número: "))

    print(num, "x 0 =", num * 0)
    print(num, "x 1 =", num * 1)
    print(num, "x 2 =", num * 2)
    print(num, "x 3 =", num * 3)
    print(num, "x 4 =", num * 4)
    print(num, "x 5 =", num * 5)
    print(num, "x 6 =", num * 6)
    print(num, "x 7 =", num * 7)
    print(num, "x 8 =", num * 8)
    print(num, "x 9 =", num * 9)
    print(num, "x 10 =", num * 10)

# función 10: lee una cantidad de colones e imprime su desglose de billetes
def desglosar_moneda():
    colones = int(input("Cantidad de colones: "))
    if colones < 5000 or colones % 5000 != 0:
       return  print("ERROR: la cantidad debe ser un entero positivo múltiplo de 5000")
    
    cincuenta = colones // 50000
    colones %= 50000
    veinte = colones // 20000
    colones %= 20000
    diez = colones // 10000
    colones %= 10000
    cinco = colones // 5000

    print(cincuenta, "de 50000")
    print(veinte, "de 20000")
    print(diez, "de 10000")
    print(cinco, "de 5000")
    print("Total de billetes:", cincuenta + veinte + diez + cinco)

