# Tarea 2
# IC1803 Taller de Programación
# William Mata, grupo 4
# Fernando Andrés González Robles
# Carné 2024201276

# función 1: obtiene la cantidad de dígitos pares en un número de 5 dígitos
# entrada: num (número de 5 dígitos)
# salida: cantidad de pares
def contar_pares(num):
    if num < 10000 or num >= 100000:
        return "ERROR: DEBE SER UN NÚMERO NATURAL DE 5 DÍGITOS"

    contador = 0
    
    # descomponer
    num1 = num // 10000
    num2 = num // 1000 % 10
    num3 = num // 100 % 10
    num4 = num // 10 % 10
    num5 = num % 10

    # verificar pares
    if num1 % 2 == 0:
        contador += 1
    
    if num2 % 2 == 0:
        contador += 1

    if num3 % 2 == 0:
        contador += 1

    if num4 % 2 == 0:
        contador += 1

    if num5 % 2 == 0:
        contador += 1

    return contador

# función 2: convierte una calificación de escala numérica a alfabética
# entrada: nota (entero entre 0 y 100)
# salida: string del equivalente alfabético
def calificacion(nota):
    if nota < 0 or nota > 100:
        return "ERROR: NOTA DEBE ESTAR ENTRE 0 Y 100"

    # no es necesario revisar el límite superior porque se usan returns
    # al retornar una nota x, se descarta que sea mayor que su rango
    # porque de otro modo, este hubiera retornado en un rango mayor
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

# función 3: asevera si un número es el doble de un impar
# entrada: num (número natural)
# salida: valor booleano (si es o no el doble de un impar)
def doble_de_impar(num):
    if num < 0:
        return "ERROR: EL NÚMERO DEBE SER NATURAL"
    
    # primero, revisar si es par en el primer lugar
    if num % 2 != 0:
        return False

    # luego, revisar si la mitad del número es impar
    if num % 4 == 0:
        return False

    return True

# función 4: asevera si dos números comparten paridad (y en tal caso, cuál) o si difieren en paridad
# entrada: n1, n2 (números naturales)
# salida: string con el tipo de paridad
def tipo_paridad(n1, n2):
    # definir booleanos con el valor de verdad de si n1 y n2 son pares
    n1_par = n1 % 2 == 0
    n2_par = n2 % 2 == 0

    if n1_par and n2_par:
        return "Paridad Par"
    elif not n1_par and not n2_par:
        return "Paridad Impar"
    else:
        return "DIFERENTE PARIDAD"

# función 5: extrae los dígitos pares e impares de un número en orden de izquierda a derecha
# entrada: num (número natural de 5 dígitos)
# salida: números pares e impares; si no hay alguno de los dos -1
def extraer_pares_impares(num):
    if num < 10000 or num >= 100000:
        return "ERROR: DEBE SER UN NÚMERO NATURAL DE 5 DÍGITOS"

    pares = impares = 0

    n1 = num // 10000
    n2 = num // 1000 % 10
    n3 = num // 100 % 10
    n4 = num // 10 % 10
    n5 = num % 10

    hay_par = hay_impar = False

    # primer dígito
    if n1 % 2 == 0:
        pares = n1
        hay_par = True
    else:
        impares = n1
        hay_impar = True

    # segundo dígito
    if n2 % 2 == 0:
        pares = pares * 10 + n2
        hay_par = True
    else:
        impares = impares * 10 + n2
        hay_impar = True

    # tercer dígito
    if n3 % 2 == 0:
        pares = pares * 10 + n3
        hay_par = True
    else:
        impares = impares * 10 + n3
        hay_impar = True

    # cuarto dígito
    if n4 % 2 == 0:
        pares = pares * 10 + n4
        hay_par = True
    else:
        impares = impares * 10 + n4
        hay_impar = True

    # quinto dígito
    if n5 % 2 == 0:
        pares = pares * 10 + n5
        hay_par = True
    else:
        impares = impares * 10 + n5
        hay_impar = True

    if not hay_par:
        pares = -1
    if not hay_impar:
        impares = -1

    return pares, impares

# función 6: maneja una cuenta bancaria con depósitos y retiros
# entrada: saldo, operación (1 o 2), monto
# salida: nuevo saldo
def cuenta_bancaria(saldo, operacion, monto):
    match operacion:
        # depósito
        case 1:
            if monto % 1000 != 0:
                return -2

            return saldo + monto
        # retiro
        case 2:
            if saldo < monto:
                return -1

            if monto % 1000 != 0:
                return -2

            return saldo - monto

# función 7: calcula el monto a pagar de servicios de telefonía,
# tomando en cuenta minutos de llamadas, mensajes y plan de internet
# entrada: minutos_llamada, mensajes, plan_internet (números enteros)
# salida: monto total, con IVA y aporte a Cruz Roja
def pago_celular(minutos_llamada, mensajes, plan_internet):
    if minutos_llamada < 0 or mensajes < 0:
        return "ERROR: LOS MINUTOS DE LLAMADA Y LOS MENSAJES DEBEN SER NÚMEROS NATURALES"
    if plan_internet < 0 or plan_internet > 3:
        return "ERROR: EL PLAN DE INTERNET DEBE SER 0, 1, 2 o 3"

    total = 0

    # primer cálculo: minutos de llamada
    if minutos_llamada <= 60:
        total = 2750
    elif minutos_llamada <= 120:
        total = 2750 + 50 * (minutos_llamada - 60)
    else:
        total = 2750 + 50 * 60 + 35 * (minutos_llamada - 120)

    # segundo cálculo: mensajes
    total += 3 * mensajes

    # tercer cálculo: plan de internet
    match plan_internet:
        case 0:
            pass
        case 1:
            total += 12000
        case 2:
            total += 15000
        case 3:
            total += 25000

    # cuarto cálculo: IVA
    total += total * 0.13

    # quinto cálculo: aporte a Cruz Roja
    total += 200

    return total


# función 8: retorna el número más cercano de 4 diferentes, con respecto al primer número de la entrada
# entrada: un entero de referencia y 4 enteros más de comparación
# salida: el número de comparación más cercano al de referencia
def cercano(ref, n1, n2, n3, n4):
    # validaciones
    if ref <= 0 or n1 <= 0 or n2 <= 0 or n3 <= 0 or n4 <= 0:
        return "ERROR: LAS ENTRADAS DEBEN SER ENTEROS MAYORES A 0"

    if ref == n1 or ref == n2 or ref == n3 or ref == n4 or n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
        return "ERROR: LAS ENTRADAS DEBEN SER DIFERENTES ENTRE SÍ"

    # la mínima diferencia entre el número de referencia y comparación
    # y el número asociado a esta diferencia
    # se empieza asumiendo que es n1 para tener un valor inicial
    min_dif = abs(ref - n1)
    min_num = n1
    
    if abs(ref - n2) < min_dif or (abs(ref - n2) == min_dif and n2 < min_num):
        min_dif = abs(ref - n2)
        min_num = n2

    if abs(ref - n3) < min_dif or (abs(ref - n3) == min_dif and n3 < min_num):
        min_dif = abs(ref - n3)
        min_num = n3

    if abs(ref - n4) < min_dif or (abs(ref - n4) == min_dif and n4 < min_num):
        min_dif = abs(ref - n4)
        min_num = n4

    return min_num

# función 9: retorna si un año es o no bisiesto
# entrada: año (número natural >= 1800 de 4 dígitos)
# salida: booleano (si es o no bisiesto)
def bisiesto(año):
    if año < 1800 or año >= 10000:
        return False
    
    # es bisiesto si es divisible entre 4, salvo que sea divisible por 100,
    # en cuyo caso debe ser también divisible por 400
    # (no obstante, si es div por 400, es div por 100)
    return (año % 4 == 0 and año % 100 != 0) or año % 400 == 0

# función 10: valida una fecha y retorna si es correcta o no
# entrada: fecha en formato ddmmaaaa
# 0 < dd < 28-31 (depende), 0 < mm < 12, 1800 <= aaaa
def valida_fecha(num):
    dias = num // 1000000
    meses = num // 10000 % 100
    años = num % 10000

    # primera comparación: años
    if años < 1800:
        return False

    # segunda comparación: meses
    if meses < 1 or meses > 12:
        return False

    # tercera comparación: días
    # máximo de días en el mes actual; el predeterminado sirve para 
    # ene, mar, may, jul, ago, oct, dic
    max_dias_en_mes = 31

    # para abr, jun, sept, nov
    if meses == 4 or meses == 6 or meses == 9 or meses == 11:
        max_dias_en_mes = 30
    # para feb
    elif meses == 2:
        if bisiesto(años):
            max_dias_en_mes = 29
        else:
            max_dias_en_mes = 28

    # este valor solo se retornará True si los otros dos también lo fueron
    return dias <= max_dias_en_mes 

# función pre-11: retorna el número con los dígitos al revés
# entrada: n (número de 5 dígitos)
# salida: número con dígitos al revés
def al_reves(n):
    if n < 10000 or n >= 100000:
        return "ERROR: el número no es de 5 dígitos"
    
    n1 = n // 10000
    n2 = n // 1000 % 10
    n3 = n // 100 % 10
    n4 = n // 10 % 10
    n5 = n % 10
    return n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1

# función 11: valida si un número es palíndromo
# entrada: número (natural de 5 dígitos)
# salida: booleano (si es o no palíndromo)
def es_palindromo(num):
    return num == al_reves(num)

# función 12: calcula qué día de la semana es cierta fecha en el calendario gregoriano, según el algoritmo de Zeller
# entrada: fecha en formato ddmmaaaa
# salida: string entre "Lunes" y "Domingo"
def nombre_dia(num):
    if not valida_fecha(num):
        return False

    dias = num // 1000000
    meses = num // 10000 % 100
    años = num % 10000

    siglo = años // 100

    # si es enero o febrero, necesito realizar los siguientes pasos:
    if meses <= 2:
        meses += 12
        años -= 1

    # se calcula así en lugar de mod por si acaso siglo cambia por ene/feb
    mod_siglo = años - siglo * 100

    dia_semana = (dias + (meses + 1) * 13 // 5 + mod_siglo + mod_siglo // 4 + siglo // 4 - 2 * siglo) % 7

    match dia_semana:
        case 0:
            return "Sábado"
        case 1:
            return "Domingo"
        case 2:
            return "Lunes"
        case 3:
            return "Martes"
        case 4:
            return "Miércoles"
        case 5:
            return "Jueves"
        case 6:
            return "Viernes"
