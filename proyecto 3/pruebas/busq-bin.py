def búsqueda(lista):
    # encontrar los campos llenos
    i_campos_llenos = []
    for i, campo in enumerate(lista):
        if campo:
            i_campos_llenos.append(i)

    # si el inicio o el final no están llenos, escoger esos
    if not i_campos_llenos or i_campos_llenos[0] != 0:
        return 0
    
    if i_campos_llenos[-1] != len(lista) - 1:
        return len(lista) - 1

    # si no, buscar la diferencia más grande, y calcular el medio en ese espacio
    max_diferencia = -1
    nuevo_campo = -1
    
    for j in range(1, len(i_campos_llenos)):
        dif_actual = i_campos_llenos[j] - i_campos_llenos[j - 1]

        if dif_actual > max_diferencia:
            max_diferencia = dif_actual
            nuevo_campo = (i_campos_llenos[j] - i_campos_llenos[j - 1]) // 2 + i_campos_llenos[j - 1]

    return nuevo_campo

print(búsqueda([[1], [5], [6], [3], [7], [4], [8], [2]]))