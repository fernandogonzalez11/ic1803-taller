def retiro(saldo, monto):
    if saldo < 0:
        return 'ERROR: saldo debe ser un número natural'
    if monto < 0:
        return 'ERROR: monto debe ser un número natural'
    if saldo < monto:
        return 'ERROR: no hay saldo suficiente'
    return saldo - monto
    
def cajero():
    colones = int(input('digite los colones: '))
    if colones < 0 or colones % 5000 != 0:
        return 'ERROR: la cantidad debe ser un número positivo múltiplo de 5000'

    cincuenta, colones = divmod(colones, 50000)
    veinte, colones = divmod(colones, 20000)
    diez, colones = divmod(colones, 10000)
    cinco = colones // 5000

    print(cincuenta, "de 50000   ", cincuenta * 50000)
    print(veinte, "de 20000   ", veinte * 20000)
    print(diez, "de 10000   ", diez * 10000)
    print(cinco, "de 5000    ", cinco * 5000)

def tiempo(maritima, terrestre):
    if maritima < 100000 or maritima >= 1000000:
        return "ERROR: parte marítima debe ser número natural de 6 dígitos"

    if terrestre < 100000 or terrestre >= 1000000:
        return "ERROR: parte terrestre debe ser número natural de 6 dígitos"

    # descomposición de marítima
    m_horas = maritima // 10000
    m_minutos = maritima // 100 % 100
    m_segundos = maritima % 100

    if m_minutos >= 60:
        return "ERROR: minutos marítimos deben ser entre 0 y 59"
    if m_segundos >= 60:
        return "ERROR: segundos marítimos deben ser entre 0 y 59"

    # descomposición de terrestre
    t_horas = terrestre // 10000
    t_minutos = terrestre // 100 % 100
    t_segundos = terrestre % 100

    if t_minutos >= 60:
        return "ERROR: minutos terrestres deben ser entre 0 y 59"
    if t_segundos >= 60:
        return "ERROR: segundos terrestres deben ser entre 0 y 59"

    # composición y formateo
    total_segundos = (m_horas + t_horas) * 3600 + (m_minutos + t_minutos) * 60 + (m_segundos + t_segundos)
    total_horas, total_segundos = divmod(total_segundos, 3600)
    total_minutos, total_segundos = divmod(total_segundos, 60)

    return total_horas * 10000 + total_minutos * 100 + total_segundos
