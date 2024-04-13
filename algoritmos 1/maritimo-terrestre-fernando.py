# Fernando González
# programa 3: sumar tiempos marítimo y terrestre en un formato específico,
# y entregar el resultado en ese mismo formato

maritimo = int(input("ingrese el tiempo de la parte marítima: "))
terrestre = int(input("ingrese el tiempo de la parte terrestre: "))

# descomponer marítimo
m_segundos = maritimo % 100
m_minutos = (maritimo // 100) % 100
m_horas = maritimo // 10000
# descomponer terrestre
t_segundos = terrestre % 100
t_minutos = (terrestre // 100) % 100
t_horas = terrestre // 10000
# sumar y descomponer
total = (m_horas + t_horas) * 3600 + (m_minutos + t_minutos) * 60 + (m_segundos + t_segundos)
total_segundos = total % 60
total_minutos = (total // 60) % 60
total_horas = total // 3600

total_formateado = total_horas * 10000 + total_minutos * 100 + total_segundos
print("el total formateado es", total_formateado)