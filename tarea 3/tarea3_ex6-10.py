def pares_impares(n):
    if not isinstance(n,int) or n<0:
        return "ERROR: LA ENTRADA DEBE SER UN NUMERO NATURAL"
    pares = 0
    impares = 0
    potencia1=0
    potencia2=0

    while n>0:
        digito = n % 10
        
        if digito % 2 == 0:
            pares += digito*pow(10,potencia1)
            potencia1+=1
        else:
            impares += digito*pow(10,potencia2)
            potencia2+=1

        n //= 10

    if pares == 0 and impares !=0:
        return "No hay", impares
    elif pares !=0 and impares ==0:
        return pares,"No hay"
    else:
        return pares,impares
    

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

    print("Nota mas alta: ", nota_mayor)
    print("Nota mas baja: ", nota_menor)
    print("Nota promedio: ", promedio)
    print("Cantidad de notas validas(entre 0 y 800): ", notas_validas)
    print("Cantidad de notas invalidas(>800): ", notas_invalidas)




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


    formula = ((fact1)/((fact2)*(fact3))) 
    return formula
    


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
