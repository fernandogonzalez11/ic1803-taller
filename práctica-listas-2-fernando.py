from random import randint

# obtener dígitos de un string
# entradas: un string
# salidas: string con solo los dígitos
def obtener_digitos(s):
    resultado = ""
    indice = 0
    largo_s = len(s)
    while indice < largo_s:
        if s[indice] in "0123456789":
            resultado = resultado + s[indice]
        indice = indice + 1

    return resultado

def obtener_digitos_for(s):
    resultado = ""
    for char in s:
        if char in "0123456789":
            resultado += char

    return resultado

# obtener string sin espacios
# entradas: un string
# salidas: string sin espacios
def eliminar_espacios(s):
    resultado = ""
    for char in s:
        if char != " ":
            resultado += char

    return resultado, len(s) - len(resultado)

# cuenta las apariciones de una lista de palabras (en una tupla)
# con una lista de frases (en otra tupla)
# entrada: tupla de palabras, tupla de frases
# salida: lista con tuplas: palabra y cantidad de apariciones
def contar_palabras(palabras, frases):
    if not (isinstance(palabras, tuple) and isinstance(frases, tuple)):
        return "ERROR: LAS ENTRADAS DEBEN SER TUPLAS"
    
    resultado = []
    for palabra in palabras:
        contador = 0
        for frase in frases:
            contador += frase.count(palabra)

        resultado.append((palabra, contador))

    return resultado

# recibe una cantidad entera n y devuelve una n-tupla con números aleatorios
# entrada: número entero
# salida: n-tupla
def numeros_random(n):
    resultado = ()
    while n > 0:
        resultado += ( randint(-100, 100), )
        n -= 1

    return resultado

#función principal
print(obtener_digitos("am2 s8b0"))
print(obtener_digitos("abcxyz"))

print(obtener_digitos_for("am2 s8b0"))
print(obtener_digitos_for("abcxyz"))

print(eliminar_espacios("hoy es martes"))

print(contar_palabras( ( "calor", "ayer", "el", "mañana"), ("ayer hizo bastante calor", "en el laboratorio hace calor") ))
print(contar_palabras( "calor", ("ayer hizo bastante calor", "en el laboratorio hace calor") ))

print(numeros_random(10))
