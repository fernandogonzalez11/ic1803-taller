"""
Lista digital de contactos

Fernando Andrés González Robles
Carné 2024201276
Taller de programación
Prof. William Mata
Grupo 4
"""

########################################
# Módulos ##############################
########################################

# usado para limpiar consola
import os


########################################
# Variables principales ################
########################################

# áreas: una lista de tuplas (número de área, nombre)
# el número de área es un entero de 1 a 999, el nombre un string de 1 a 40 caracteres
areas = []

# diccionario de áreas: mapea cada número de área a su índice respectivo
dict_áreas = {}

# constante de tipos de teléfono permitidos
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")

# área por omisión en la generación de contactos
área_por_defecto = None

# tipo de teléfono por omisión (debe pertenecer a TIPOS_TELÉFONO)
tipo_por_defecto = None

# lista de contactos
# cada contacto es una lista con el orden
# [teléfono, área, tipo, nombre, correo, dirección, nacimiento, pasatiempos, notas]
contactos = []

# diccionario de contactos: mapea cada tupla de teléfonos a su índice en contactos
dict_contactos = {}

########################################
# Funcionalidades base #################
########################################

"""
menú principal
pide infinitamente entradas para enramarse a otros menús o funciones
se puede salir del menú digitando "0"
"""
def menú_principal():
    opciones = {
        "1": "Registrar áreas",
        "2": "Configuración de lista de contactos",
        "3": "Registrar contactos",
        "4": "Administrar grupos de contactos",
        "5": "Lista de contactos",
        "6": "Ayuda",
        "7": "Acerca de",
        "0": "Fin"
    }

    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")

        # imprimir todas las opciones
        for num, nombre in opciones.items():
            print(num + ". " + nombre)

        # pedir opción
        opción = input("   OPCIÓN: ")

        match opción:
            case "1":
                menú_registro_áreas()
            case "2":
                menú_config_contactos()
            case "3":
                menú_registro_contactos()
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "0":
                # finalizar el ciclo, y en turno todo el programa
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO>")

"""
menú de opción 1: registrar áreas
pide infinitamente entradas para sus funciones particulares
se puede regresar digitando "0"
"""
def menú_registro_áreas():
    opciones = {
        "1": "Agregar áreas",
        "2": "Consultar áreas",
        "3": "Modificar áreas",
        "4": "Eliminar áreas",
        "0": "Fin"
    }

    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR ÁREAS" + "\n")

        # imprimir todas las opciones
        for num, nombre in opciones.items():
            print(num + ". " + nombre)

        # pedir opción
        opción = input("   OPCIÓN: ")

        match opción:
            case "1":
                áreas_agregar()
            case "2":
                áreas_consultar()
            case "3":
                áreas_modificar()
            case "4":
                áreas_eliminar()
            case "0":
                # finalizar el ciclo, esto regresa al menú principal
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO> ")      

"""
funcionalidad 1.1: agregar áreas
pide un número y nombre de área y lo registra (con respectivas verificaciones)
"""
def áreas_agregar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR ÁREAS: AGREGAR" + "\n")

        # pedir área
        try:
            número = input("Área" + " " * 16)

            # regresar al menú de registro
            if número == "C":
                break

            número = int(número)

            if número <= 0 or número >= 1000:
                input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
                # retorna al inicio del while
                continue
            
            # revisar si el número existe en alguna área registrada
            if área_registrada(número):
                input("Esta área ya está registrada, no se puede agregar. Presione <INTRO> ")
                continue
            
            nombre = input("Nombre del área" + " " * 5)

            if len(nombre) < 1 or len(nombre) > 40:
                input("[ERROR] El nombre de área debe ser entre 1 y 40 caracteres. Presione <INTRO> ")
                continue

            confirmación = input("OPCIÓN    <A>Aceptar    <C>Cancelar  ")

            if confirmación == "A":
                areas.append((número, nombre))
                dict_áreas[número] = len(areas) - 1

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
funcionalidad 1.2: consultar áreas
imprime información de un área (si está registrada) con su número
"""
def áreas_consultar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR ÁREAS: CONSULTAR" + "\n")

        # pedir área
        try:
            número = input("Área" + " " * 16)

            # regresar al menú de registro
            if número == "C":
                break
            
            número = int(número)

            # revisar que esté registrada
            if not área_registrada(número):
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el nombre usando el diccionario
            nombre = areas[dict_áreas[número]][1]

            print()
            print("Nombre del área" + " " * 5 + nombre)

            input("OPCIÓN    <A>Aceptar  ")

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
funcionalidad 1.3: modificar áreas
pide el área, y modifica su nombre (si está registrada)
"""
def áreas_modificar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR ÁREAS: MODIFICAR" + "\n")

        # pedir área
        try:
            número = input("Área" + " " * 13)

            # regresar al menú de registro
            if número == "C":
                break
            
            número = int(número)

            # revisar que esté registrada
            if not área_registrada(número):
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO> ")
                continue
            
            nombre = areas[dict_áreas[número]][1]

            print(" " * 33 + "NUEVO VALOR")
            print("Nombre del área  " + nombre)

            nuevo = input(" " * 33)

            if nuevo == "":
                nuevo = nombre

            elif len(nuevo) > 40:
                input("[ERROR] El nuevo nombre debe ser entre 1 y 40 caracteres. Presione <INTRO> ")
                continue

            confirmación = input("OPCIÓN    <A>Aceptar  <C>Cancelar ")

            if confirmación == "A":
                areas[dict_áreas[número]] = (número, nuevo)

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")
    
"""
funcionalidad 1.4: eliminar áreas
pide el área, elimina su entrada en el registro (si está registrada), y actualiza el diccionario de índices
"""
def áreas_eliminar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR ÁREAS: ELIMINAR" + "\n")

        # pedir área
        try:
            número = input("Área" + " " * 16)

            # regresar al menú de registro
            if número == "C":
                break
            
            número = int(número)

            # revisar que esté registrada
            if not área_registrada(número):
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO>")
                continue
            
            # verificar que no hayan contactos asociados
            hay_contactos = False

            for contacto in contactos:
                if contacto[1] == número:
                    input("En esta área hay contactos asociados, no se puede eliminar. Presione <INTRO> ")
                    hay_contactos = True
                    break
            
            if hay_contactos:
                break

            # encontrar el nombre usando el diccionario
            índice = dict_áreas[número]

            print()
            print("Nombre del área" + " " * 5 + areas[índice][1])

            confirmación = input("CONFIRMA LA ELIMINACIÓN    <A>Aceptar  <C>Cancelar ")

            if confirmación == "A":
                del areas[índice]
                construir_diccionarios()

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")


"""
menú de opción 2: configuración de la lista de contactos

pide el área y el tipo de elemento por omisión, y los establece en las configuraciones
"""
def menú_config_contactos():
    global área_por_defecto, tipo_por_defecto

    limpiar_terminal()

    # 10 espacios, título, nueva línea adicional
    print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
    print(" " * 10 + "CONFIGURACIÓN DE LA LISTA DE CONTACTOS" + "\n")

    # primera parte: obtener el área por defecto
    while True:
        try:
            área = input("Área por omisión:" + " " * 5)
            
            área = int(área)

            # verificar que esté registrado
            if not área_registrada(área):
                input("Esta área no está registrada, no se puede seleccionar. Presione <INTRO> ")
                print()
                continue

            print(" " * 22 + areas[dict_áreas[área]][1])
            print()

            break

        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

    # parte 2: obtener el tipo de número por defecto
    while True:
            tipo = input("Tipo de teléfono por omisión (M: Móvil, C: Casa, T: Trabajo, O: Otro): ")

            if tipo not in TIPOS_TELEFONO:
                input("Este tipo de teléfono no existe, no se puede seleccionar. Presione <INTRO> ")
                print()
                continue

            break
    
    
    # parte 3: confirmar los valores
    print()
    confirmación = input("OPCIÓN    <A>Aceptar  <C>Cancelar  ")

    if confirmación == "A":
        área_por_defecto = área
        tipo_por_defecto = tipo    
        
"""
menú de opción 3: registro de contactos
pide infinitamente entradas para sus funciones particulares
se puede regresar digitando "0"
"""
def menú_registro_contactos():
    opciones = {
        "1": "Agregar contactos",
        "2": "Consultar contactos",
        "3": "Modificar contactos",
        "4": "Eliminar contactos",
        "0": "Fin"
    }

    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR CONTACTOS" + "\n")

        # imprimir todas las opciones
        for num, nombre in opciones.items():
            print(num + ". " + nombre)

        # pedir opción
        opción = input("   OPCIÓN: ")

        match opción:
            case "1":
                contactos_agregar()
            case "2":
                contactos_consultar()
            case "3":
                contactos_modificar()
            case "4":
                contactos_eliminar()
            case "0":
                # finalizar el ciclo, esto regresa al menú principal
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO> ")

"""
funcionalidad 3.1: agregar contactos
pide los diferentes campos para llenar. no necesariamente se llenan todos, para ello hay defaults
"""
def contactos_agregar():
    limpiar_terminal()

    # 10 espacios, título, nueva línea adicional
    print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
    print(" " * 10 + "REGISTRAR CONTACTOS: AGREGAR" + "\n")

    contacto = []

    # parte 1: pedir el teléfono (número y área)
    # teléfono: número natural de 5 a 12 dígitos
    # área: número natural entre 1 y 999
    while len(contacto) < 2:
        try:
            telf = input("Teléfono" + " " * 17)

            if telf == "C":
                return
            else:
                telf = int(telf)

            área = input("Área" + " " * 21)

            if not área:
                área = área_por_defecto
            else:
                área = int(área)

            if telf < pow(10, 5) or telf > pow(10, 12):
                input("El teléfono debe ser de 5 a 12 dígitos. Presione <INTRO> ")
            elif área not in dict_áreas:
                input("Esta área no está registrada, no se puede seleccionar. Presione <INTRO> ")
            elif (área, telf) in dict_contactos:
                input("Este teléfono ya está registrado, no se puede agregar. Presione <INTRO> ")
            else:
                contacto += [telf, área]
                print(" " * 25 + areas[dict_áreas[área]][1])

        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        except Exception as error:
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

    # parte 2: tipo de teléfono
    while len(contacto) < 3:
        tipo = input("Tipo teléfono (M,C,T,O)" + " " * 2)

        if not tipo:
            tipo = tipo_por_defecto
        
        if tipo not in TIPOS_TELEFONO:
            input("Este tipo de teléfono no existe, no se puede seleccionar. Presione <INTRO> ")
        else:
            contacto.append(tipo)

    # parte 3: nombre de contacto
    while len(contacto) < 4:
        nombre = input("Nombre contacto" + " " * 10)

        if len(nombre) < 1 or len(nombre) > 50:
            input("[ERROR] El nombre del contacto debe ser entre 1 y 50 caracteres. Presione <INTRO> ")
        else:
            contacto.append(nombre)

    # parte 4: correo electrónico
    while len(contacto) < 5:
        correo = input("Correo electrónico" + " " * 7)

        if not verificar_correo(correo):
            input("El correo no es válido. Presione <INTRO> ")
        else:
            contacto.append(correo)

    # parte 5: dirección física
    while len(contacto) < 6:
        dirección = input("Dirección física" + " " * 9)

        if len(dirección) > 80:
            input("[ERROR] La dirección física debe ser entre 0 y 80 caracteres. Presione <INTRO> ")
        else:
            contacto.append(dirección)
        
    # parte 6: fecha de nacimiento
    while len(contacto) < 7:
        nacimiento = input("Fecha de nacimiento" + " " * 6)
       
        posible_fecha = validar_fecha(nacimiento)
        if posible_fecha == -1:
            input("[ERROR] La fecha no es válida. Presione <INTRO> ")
        else:
            contacto.append(posible_fecha)

    # parte 7: pasatiempos
    while len(contacto) < 8:
        pasatiempos = input("Pasatiempos" + " " * 14)

        if len(pasatiempos) > 60:
            input("[ERROR] Los pasatiempos deben ser entre 0 y 60 caracteres. Presione <INTRO> ")
        else:
            contacto.append(pasatiempos)

    # parte 8: notas
    while len(contacto) < 9:
        notas = input("Notas" + " " * 20)

        if len(pasatiempos) > 60:
            input("[ERROR] Las notas deben ser entre 0 y 60 caracteres. Presione <INTRO> ")
        else:
            contacto.append(notas)

    # parte 9: confirmar
    print()
    confirmación = input("OPCIÓN  <A>Aceptar <C>Cancelar  ")

    if confirmación == "A":
        contactos.append(contacto)
        dict_contactos[(área, telf)] = len(contactos) - 1
        
"""
funcionalidad 3.2: consultar contactos
"""
def contactos_consultar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR CONTACTOS: CONSULTAR" + "\n")

        # pedir teléfono
        try:
            telf = input("Teléfono" + " " * 17)

            # regresar al menú de registro
            if telf == "C":
                break
            
            telf = int(telf)

            área = int(input("Área" + " " * 21))

            if (telf, área) not in dict_contactos:
                input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el contacto asociado al teléfono
            contacto = contactos[dict_contactos[(telf, área)]]

            # imprimir todos los valores
            print(" " * 25 + areas[dict_áreas[área]][1])
            print("Tipo teléfono (M,C,T,O)  " + contacto[2])
            print("Nombre contacto          " + contacto[3])
            print("Correo electrónico       " + contacto[4])
            print("Dirección física         " + contacto[5])
            print("Fecha de nacimiento      " + contacto[6])
            print("Pasatiempos              " + contacto[7])
            print("Notas                    " + contacto[8] + "\n")

            input("OPCIÓN    <A>Aceptar  ")

        # sucede cuando teléfono o área no se puede convertir a int
        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")


"""
funcionalidad 3.3: modificar contactos
"""
def contactos_modificar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR CONTACTOS: MODIFICAR" + "\n")

        # pedir teléfono
        try:
            telf = input("Teléfono" + " " * 17)

            # regresar al menú de registro
            if telf == "C":
                break
            
            telf = int(telf)

            área = int(input("Área" + " " * 21))

            if (telf, área) not in dict_contactos:
                input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el contacto asociado al teléfono
            # hacer un copy para no interferir con el elemento global
            contacto = contactos[dict_contactos[(telf, área)]].copy()

            # longitudes los valores del tipo en adelante
            longitudes = [len(s) for s in contacto[2:]]
            # esto es útil para tener el tamaño adecuado para emular columnas
            max_long = max(longitudes)
            # ahora, que cada longitud más bien sea el margen
            longitudes = [max_long - longitud + 2 for longitud in longitudes]

            nombre_área = areas[dict_áreas[área]][1]

            print(" " * 25 + nombre_área + " " * (max_long - len(nombre_área) + 2) + "NUEVOS VALORES")

            # pedir cada dato secuencialmente y editarlo en contacto (solo localmente)

            # tipo de teléfono
            while True:
                tipo = input("Tipo teléfono (M,C,T,O)  " + contacto[2] + " " * longitudes[0])
                if not tipo:
                    break
                elif tipo in TIPOS_TELEFONO:
                    contacto[2] = tipo
                    break
                else:
                    input("Este tipo de teléfono no existe, no se puede seleccionar. Presione <INTRO> ")
            
            # nombre
            while True:
                nombre = input("Nombre contacto          " + contacto[3] + " " * longitudes[1])

                if not nombre:
                    break
                elif len(nombre) <= 50:
                    contacto[3] = nombre
                    break
                else:
                    input("[ERROR] El nombre del contacto debe ser entre 1 y 50 caracteres. Presione <INTRO> ")

            # correo
            while True:
                correo = input("Correo electrónico       " + contacto[4] + " " * longitudes[2])

                if not correo:
                    break
                elif verificar_correo(correo):
                    contacto[4] = correo
                    break
                else:
                    input("El correo no es válido. Presione <INTRO> ")
            
            # dirección
            while True:
                dirección = input("Dirección física         " + contacto[5] + " " * longitudes[3])

                if not dirección:
                    break
                elif len(dirección) <= 80:
                    contacto[5] = dirección
                    break
                else:
                    input("[ERROR] La dirección física debe ser entre 0 y 80 caracteres. Presione <INTRO> ")

            # fecha de nacimiento
            while True:
                nacimiento = input("Fecha de nacimiento      " + contacto[6] + " " * longitudes[4])

                if not nacimiento:
                    break
                elif validar_fecha(nacimiento) != -1:
                    contacto[6] = validar_fecha(nacimiento)
                    break
                else:
                    input("[ERROR] La fecha no es válida. Presione <INTRO> ")

            # pasatiempos
            while True:
                pasatiempos = input("Pasatiempos              " + contacto[7] + " " * longitudes[5])

                if not pasatiempos:
                    break
                elif len(pasatiempos) <= 60:
                    contacto[7] = pasatiempos
                    break
                else:
                    input("[ERROR] Los pasatiempos deben ser entre 0 y 60 caracteres. Presione <INTRO> ")

            # notas
            while True:
                notas = input("Notas                    " + contacto[8] + " " * longitudes[6])

                if not notas:
                    break
                elif len(notas) <= 60:
                    contacto[8] = notas
                    break
                else:
                    input("[ERROR] Las notas deben ser entre 0 y 60 caracteres. Presione <INTRO> ")
                

            confirmación = input("OPCIÓN    <A>Aceptar  <C>Cancelar ")

            if confirmación == "A":
                contactos[dict_contactos[(telf, área)]] = contacto

        # sucede cuando teléfono o área no se puede convertir a int
        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
TODO funcionalidad 3.4: eliminar contactos
"""
def contactos_eliminar():
    pass



########################################
# Funciones auxiliares #################
########################################

"""
limpia la terminal, con el comando "cls" o "clear" según el sistema operativo
"""
def limpiar_terminal():
    # en windows
    if os.name == "nt":
        os.system("cls")
    # linux, mac, etc
    else:
        os.system("clear")

"""
retorna si un área está registrada

entrada: área como número
salida: bool
"""
def área_registrada(área: int):
    for registrada in areas:
        if registrada[0] == área:
            return True

    return False

"""
construye el diccionario de áreas y contactos
con base en la lista de áreas actuales
"""
def construir_diccionarios():
    for índice, área in enumerate(areas):
        dict_áreas[área[0]] = índice

    for índice, contacto in enumerate(contactos):
        dict_contactos[(contacto[0], contacto[1])] = índice


"""
verifica si una fecha es correcta, y retorna "0", -1 o la fecha original, dependiendo de su validez

entrada: fecha como string
salida: fecha válida como string, o -1 si no es válida, o "0" si está incompleta
"""
def validar_fecha(fecha: str):
    if not "/" in fecha:
        return -1

    lista_fecha = fecha.split("/")

    # debe estar completa; si no lo está, devuelve "0"
    if len(lista_fecha) != 3:
        return "0"

    for i, parte in enumerate(lista_fecha):
        # todos los caracteres deben ser números (descarta negativos también)
        if not parte.isnumeric():
            return -1

        lista_fecha[i] = int(parte)
    
    día, mes, año = lista_fecha

    # es bisiesto si se divide en cuatro pero no en 100, pero cuando se divide en 400 sí cuenta
    bisiesto = (año % 4 == 0 and año % 100 != 0) or año % 400 == 0

    # verificar mes
    if mes > 12:
        return -1

    # verificar día
    # máximo de días en el mes actual; el predeterminado sirve para 
    # ene, mar, may, jul, ago, oct, dic
    max_dias_en_mes = 31

    # para abr, jun, sept, nov
    if mes in (4, 6, 9, 11):
        max_dias_en_mes = 30
    # para feb
    elif mes == 2:
        if bisiesto:
            max_dias_en_mes = 29
        else:
            max_dias_en_mes = 28
    
    if día > max_dias_en_mes:
        return -1

    # si todo está correcto, se puede retornar la fecha original
    return fecha

"""
verifica si un correo es correcto
parte1@parte2, sin espacio

entrada: string
salida: bool
"""
def verificar_correo(correo: str):
    if not "@" in correo or " " in correo:
        return False
    
    # como debe estar tanto parte1 como parte2, si aparece el delimitador al inicio o final uno de ellos falta
    if correo[0] == "@" or correo[-1] == "@":
        return False

    return len(correo.split("@")) == 2



########################################
# Pruebas ##############################
########################################
areas = [(502, "Guatemala"), (506, "Costa Rica"), (507, "Nicaragua")]
contactos = [[12341234, 506, 'M', 'a', 'b@c.com', '', '11/11/2006', '', '']]
área_por_defecto = 506
tipo_por_defecto = "M"
construir_diccionarios()


########################################
# Función principal ####################
########################################
menú_principal()