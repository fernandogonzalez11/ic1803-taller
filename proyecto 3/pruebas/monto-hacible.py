def monto_posible(monto: int, monedas: list, billetes: list) -> bool:
    i = 0;
    denoms = billetes + monedas
    denoms.sort(reverse=True)

    for denom in denoms:
        if monto // denom:
            monto %= denom
    
    return monto == 0

def monto_posible_realista(monto: int, cantidades_denominaciones: list) -> dict|int:
    denoms = []
    saldos = {}
    distribución = {}

    for denom, (ent, sal) in (cantidades_denominaciones[0] | cantidades_denominaciones[1]).items():
        denoms.append(denom)
        saldos[denom] = ent - sal
    
    denoms.sort(reverse=True)
    
    for denom in denoms:
        if saldos[denom] != 0:
            uso_posible = min(saldos[denom], monto // denom)
            distribución[denom] = uso_posible
            monto -= denom * uso_posible

    if monto != 0:
        return -1
    else:
        return distribución

a = [{50: [2, 0], 100: [2, 0], 500: [1, 0]}, {1000: [1, 0], 2000: [0, 0], 5000: [0, 0], 10000: [0, 0], 20000: [0, 0]}]
