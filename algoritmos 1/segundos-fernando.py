# Fernando González
# programa 2: convertir una cantidad de segundos en sus horas, minutos y segundos respectivos

segundos = int(input("¿cuántos segundos? "))
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(horas, "horas")
print(minutos, "minutos")
print(segundos, "segundos")