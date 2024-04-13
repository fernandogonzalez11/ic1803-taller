# función sucesor: incrementa en 1 un valor
def sucesor(num):
    suc = num + 1
    return suc

# programa principal: leer datos, llamar a la función, imprimir
n = int(input("Dé un número: "))
s = sucesor(n) # el resultado de la función sucesor
print("El sucesor de", n, "es", s)
print("El doble de", s, "es", s*2)
