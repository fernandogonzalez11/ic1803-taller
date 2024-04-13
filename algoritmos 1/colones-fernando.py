# Fernando González
# programa 4: mostrar cantidad de billetes de varias denominaciones según el monto en colones

colones = int(input("¿cuántos colones son? "))
cincueta_mil = colones // 50000
colones %= 50000
veinte_mil = colones // 20000
colones %= 20000
diez_mil = colones // 10000
colones %= 10000
cinco_mil = colones // 5000

# prints
print(cincueta_mil, "de 50000")
print(veinte_mil, "de 20000")
print(diez_mil, "de 10000")
print(cinco_mil, "de 5000")
print("cantidad de billetes ocupados:", cincueta_mil + veinte_mil + diez_mil + cinco_mil)