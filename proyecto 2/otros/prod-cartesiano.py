"""
obtiene los pares del producto cartesiano de un conjunto con sí mismo,
excluyendo a los pares reflexivos

entrada: diccionarios con los equipos: las llaves son sus códigos y los valores otra información
salida: lista de pares como tuplas
"""
def producto_cartesiano(elementos: dict) -> list:
    pares = []

    llaves = list(elementos.keys())
    for i, elem_1 in enumerate(llaves[:-1]):
        for elem_2 in llaves[i + 1:]:
            # solo añadir el código de cada equipo
            pares.append((elem_1, elem_2))

    return pares