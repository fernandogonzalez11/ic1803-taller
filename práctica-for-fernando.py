# retorna el factorial de un número usando el estatuto for
# entrada: número natural
# salida: n!
def factorial(n):
    if not isinstance(n, int) or n < 0:
        return "ERROR: LA ENTRADA DEBE SER UN NÚMERO NATURAL"
    
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

# imprime la tabla de multiplicación de un primer número,
# en un rango del segundo al tercer número
# entrada: número, inicio, fin
# salida: tabla de multiplicación del número
def tabla_multiplos(número, inicio, fin):
    if not (isinstance(número, int) and isinstance(inicio, int) and isinstance(fin, int)):
        return "ERROR: ENTRADAS DEBEN SER NÚMEROS"

    if número < 0 or inicio < 0 or fin < 0:
        return "ERROR: ENTRADAS DEBEN SER NATURALES"

    if inicio > fin:
        return "ERROR: INICIO DEBE SER <= FIN"
    
    for número_2 in range(inicio, fin + 1):
        print(número * número_2)


# función principal
for i in range(5):
    print("fact", i, factorial(i))

print("-----")

print("tabla de múltiplos:")
tabla_multiplos(12, 3, 7)
