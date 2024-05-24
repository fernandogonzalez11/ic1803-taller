"""
hacer un diccionario de traducción, y luego traducir una frase con ese diccionario
"""
def traducir():
    traducciones = {}

    cont = 1
    while True:
        valor = input(f"traducción {cont} ")

        if valor == "C":
            break
        
        español, inglés = valor.split(":")
        traducciones[español] = inglés

        cont += 1

    print()
    frase = input("frase: ").split(" ")
    for i, palabra in enumerate(frase):
        if palabra in traducciones:
            frase[i] = traducciones[palabra]
    
    return " ".join(frase)

def desCSVear(csv: str) -> dict:
    dict_csv = {}

    líneas = csv.split("\n")
    headings = líneas[0].split(";")

    for línea in líneas[1:]:
        dict_línea = {}
        valores = línea.split(";")
        
        for i, valor in enumerate(valores[1:]):
            if i == 3:
                valor = float(valor)
            dict_línea[headings[i + 1]] = valor

        dict_csv[valores[0]] = dict_línea

    return dict_csv

des = desCSVear("nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7")
print(des)

