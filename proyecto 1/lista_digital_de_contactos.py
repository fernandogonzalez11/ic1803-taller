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

# usado para revisar expresiones en los filtros de la lista de contactos
import re

# usados para crear PDFs
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet

# usado para abrir un PDF en el programa designado para tal
import webbrowser

# usado para obtener el tiempo actual
import datetime

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

# lista de grupos (solo con sus nombres)
grupos = []

# lista de contactos asociados a cada grupo de la lista anterior
contactos_por_grupo = []

# URL del manual de usuario
URL_MANUAL = "https://youtu.be/cByPqUmF3MQ"

# versión del proyecto
VERSIÓN = "1.0.0"

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
                menú_administrar_grupos()
            case "5":
                menú_lista_contactos()
            case "6":
                menú_ayuda()
            case "7":
                menú_acerca_de()
            case "0":
                # finalizar el ciclo, y en turno todo el programa
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO> ")


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

            if confirmar():
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

            # confirmar pero solo permitir el valor de aceptar
            confirmar(solo_aceptar = True)

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

            if confirmar():
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
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO> ")
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

            if confirmar() and confirmar("CONFIRMA LA ELIMINACIÓN"):
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

            if área == "C":
                return

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
            
            if tipo in TIPOS_TELEFONO[::2]:
                ind_abreviatura = TIPOS_TELEFONO[::2].index(tipo)
                tipo = TIPOS_TELEFONO[ind_abreviatura * 2 + 1]

            break
    
    
    # parte 3: confirmar los valores
    print()
    if confirmar():
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
    while True:
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

                if telf < pow(10, 4) or telf >= pow(10, 12):
                    input("El teléfono debe ser de 5 a 12 dígitos. Presione <INTRO> ")
                elif área not in dict_áreas:
                    input("Esta área no está registrada, no se puede seleccionar. Presione <INTRO> ")
                elif (telf, área) in dict_contactos:
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
                # pasar M, T, C, O a sus descripciones
                if tipo in TIPOS_TELEFONO[::2]:
                    ind_abreviatura = TIPOS_TELEFONO[::2].index(tipo)
                    tipo = TIPOS_TELEFONO[ind_abreviatura * 2 + 1]

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
        if confirmar():
            contactos.append(contacto)
            dict_contactos[(telf, área)] = len(contactos) - 1
        
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

            área = input("Área" + " " * 21)

            if not área:
                área = área_por_defecto
            else:
                área = int(área)

            if (telf, área) not in dict_contactos:
                input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el contacto asociado al teléfono
            contacto = contactos[dict_contactos[(telf, área)]]

            # lista de grupos a los que pertenece
            lista_grupos = grupos_de_contacto(contacto)

            # imprimir todos los valores
            print(" " * 25 + areas[dict_áreas[área]][1])
            print("Tipo teléfono (M,C,T,O)  " + contacto[2])
            print("Nombre contacto          " + contacto[3])
            print("Correo electrónico       " + contacto[4])
            print("Dirección física         " + contacto[5])
            print("Fecha de nacimiento      " + contacto[6])
            print("Pasatiempos              " + contacto[7])
            print("Notas                    " + contacto[8])
            
            if lista_grupos:
                print("Grupos                   " + ", ".join(lista_grupos) + "\n")

            # confirmar, pero solo permitir el valor de aceptar
            confirmar(solo_aceptar = True)

        # sucede cuando teléfono o área no se puede convertir a int
        except ValueError as error:
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

            área = input("Área" + " " * 21)

            if not área:
                área = área_por_defecto
            else:
                área = int(área)

            if (telf, área) not in dict_contactos:
                input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el contacto asociado al teléfono
            # hacer un copy para no interferir con el elemento global
            contacto = contactos[dict_contactos[(telf, área)]].copy()

            # longitudes los valores del tipo en adelante
            longitudes = [len(s) for s in contacto[2:]]
            # esto es útil para tener el tamaño adecuado para emular columnas
            max_long = max(20, max(longitudes))
            # ahora, que cada longitud más bien sea el margen
            longitudes = [max_long - longitud + 2 for longitud in longitudes]

            nombre_área = areas[dict_áreas[área]][1]

            print(" " * 25 + nombre_área + " " * (max_long - len(nombre_área) + 2) + "NUEVOS VALORES")

            # pedir cada dato secuencialmente y editarlo en contacto (solo localmente)

            # tipo de teléfono
            while True:
                tipo = input("Tipo teléfono (M,C,T,O)  " + contacto[2] + " " * longitudes[0])

                # cuando no se pone tipo, preferí saltarlo en lugar de cambiarlo al defecto
                if not tipo:
                    break

                if tipo in TIPOS_TELEFONO:
                    # pasar M, T, C, O a sus descripciones
                    if tipo in TIPOS_TELEFONO[::2]:
                        ind_abreviatura = TIPOS_TELEFONO[::2].index(tipo)
                        tipo = TIPOS_TELEFONO[ind_abreviatura * 2 + 1]

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
                

            if confirmar():
                contactos[dict_contactos[(telf, área)]] = contacto

        # sucede cuando teléfono o área no se puede convertir a int
        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
funcionalidad 3.4: eliminar contactos
"""
def contactos_eliminar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "REGISTRAR CONTACTOS: ELIMINAR" + "\n")

        # pedir teléfono
        try:
            telf = input("Teléfono" + " " * 17)

            # regresar al menú de registro
            if telf == "C":
                break
            
            telf = int(telf)

            área = input("Área" + " " * 21)

            if not área:
                área = área_por_defecto
            else:
                área = int(área)

            if (telf, área) not in dict_contactos:
                input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                continue
            
            # encontrar el contacto asociado al teléfono
            índice_contacto = dict_contactos[(telf, área)]
            contacto = contactos[índice_contacto]

            # imprimir todos los valores
            print(" " * 25 + areas[dict_áreas[área]][1])
            print("Tipo teléfono (M,C,T,O)  " + contacto[2])
            print("Nombre contacto          " + contacto[3])
            print("Correo electrónico       " + contacto[4])
            print("Dirección física         " + contacto[5])
            print("Fecha de nacimiento      " + contacto[6])
            print("Pasatiempos              " + contacto[7])
            print("Notas                    " + contacto[8] + "\n")
            
            # una lista con los índices de los grupos en los que está el contacto
            grupos_de_contacto = []
            for i, grupo in enumerate(contactos_por_grupo):
                if (telf, área) in grupo:
                    grupos_de_contacto.append(i)

            # actúa como bloqueo si existen grupos asociados
            if grupos_de_contacto and not confirmar("Este contacto está asociado a grupos, por lo que se borrará al contacto de ellos. Confirme este procedimiento."):
                continue

            if confirmar("CONFIRMA LA ELIMINACIÓN"):
                del contactos[índice_contacto]

                # si no hay grupos asociados, este ciclo no corre
                for i_grupo in grupos_de_contacto:
                    # el índice del contacto en cada lista de contactos por grupo
                    j_contacto = contactos_por_grupo[i_grupo].index((telf, área))
                    del contactos_por_grupo[i_grupo][j_contacto]

                construir_diccionarios()

        # sucede cuando teléfono o área no se puede convertir a int
        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        # imprimir y manifestar cualquier otro error
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")


""" 
menú de opción 4: administrar grupos de contactos
pide infinitamente entradas para sus funciones particulares
se puede regresar digitando "0"
"""
def menú_administrar_grupos():
    opciones = {
        "1": "Agregar grupos",
        "2": "Agregar contactos a los grupos",
        "3": "Modificar grupos",
        "4": "Eliminar grupos",
        "5": "Eliminar contactos de los grupos",
        "0": "Fin"
    }

    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS" + "\n")

        # imprimir todas las opciones
        for num, nombre in opciones.items():
            print(num + ". " + nombre)

        # pedir opción
        opción = input("   OPCIÓN: ")

        match opción:
            case "1":
                grupos_agregar()
            case "2":
                grupos_agregar_contacto()
            case "3":
                grupos_modificar()
            case "4":
                grupos_eliminar()
            case "5":
                grupos_eliminar_contacto()
            case "0":
                # finalizar el ciclo, esto regresa al menú principal
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO> ")

"""
funcionalidad 4.1: agregar grupos
"""
def grupos_agregar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS")
        print(" " * 10 + "Agregar grupos" + "\n")

        # solicitar el nombre del grupo
        nombre = input("Nombre del grupo" + " " * 4)

        if nombre == "C":
            break
        elif len(nombre) > 40:
            input("[ERROR] El nombre del grupo debe ser entre 1 y 40 caracteres. Presione <INTRO> ")
        elif nombre in grupos:
            input("Este grupo ya está registrado, no se puede agregar. Presione <INTRO> ")
        else:
            print()
            if confirmar():
                # agrega tanto el nombre como una lista vacía de contactos
                grupos.append(nombre)
                contactos_por_grupo.append([])

"""
funcionalidad 4.2: agregar contactos a grupos
"""
def grupos_agregar_contacto():
    while True:
        try:
            limpiar_terminal()

            # 10 espacios, título, nueva línea adicional
            print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
            print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS")
            print(" " * 10 + "Agregar contactos a los grupos" + "\n")

            nombre = input("Nombre del grupo" + " " * 4)

            if nombre == "C":
                break
            elif nombre not in grupos:
                input("Este grupo no existe, no puede agregarle contactos. Presione <INTRO> ")
                continue
            
            print()

            while True:
                telf = int(input("Teléfono" + " " * 12))
                área = input("Área" + " " * 16)

                if not área:
                    área = área_por_defecto
                else:
                    área = int(área)

                if (telf, área) not in dict_contactos:
                    input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                else:
                    break
            
            índice_grupo = grupos.index(nombre)
            contacto = contactos[dict_contactos[(telf, área)]]

            # mandar un error en caso de duplicados
            if (telf, área) in contactos_por_grupo[índice_grupo]:
                input("Este contacto ya está registrado en el grupo, no se puede añadir. Presione <INTRO> ")
                continue

            print(" " * 20 + areas[dict_áreas[área]][1])
            print("Nombre contacto" + " " * 5 + contacto[3] + "\n")

            if confirmar():
                if (telf, área) not in contactos_por_grupo[índice_grupo]:
                    contactos_por_grupo[índice_grupo].append((telf, área))

        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        except Exception as error:
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
funcionalidad 4.3: modificar grupos
"""
def grupos_modificar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS")
        print(" " * 10 + "Modificar grupos" + "\n")
        
        print(" " * 36 + "NUEVO VALOR")
        nombre = input("Nombre del grupo" + " " * 4)

        if nombre == "C":
            break
        elif nombre not in grupos:
            input("Este grupo no existe, no se puede modificar. Presione <INTRO> ")
            continue

        nuevo_nombre = input(" " * 36)

        # si el grupo nuevo existe, guarda el índice aquí para unirlos
        índice_original = grupos.index(nombre)
        índice_nuevo = None

        if nuevo_nombre in grupos:
            índice_nuevo = grupos.index(nuevo_nombre)
            print("Grupo ya existe, en caso de aceptar la operación los contactos se le agregarán")
        
        if confirmar():
            if índice_nuevo:
                # unir ambos en uno, y borrar el otro

                # hacer una unión de sets, para no tener posibles duplicados
                set_nuevos_contactos = set(contactos_por_grupo[índice_original]) \
                    .union(set(contactos_por_grupo[índice_nuevo]))

                # pasar el set -> list, asignarlo al original
                contactos_por_grupo[índice_original] = list(set_nuevos_contactos)
                del grupos[índice_nuevo]
                del contactos_por_grupo[índice_nuevo]

            # sin importar el nuevo índice, se debe cambiar el nombre
            grupos[índice_original] = nuevo_nombre

"""
funcionalidad 4.4: eliminar grupos
"""
def grupos_eliminar():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS")
        print(" " * 10 + "Eliminar grupos" + "\n")

        # solicitar el nombre del grupo
        nombre = input("Nombre del grupo" + " " * 4)

        if nombre == "C":
            break
        elif nombre not in grupos:
            input("Este grupo no existe, no se puede eliminar. Presione <INTRO> ")
        else:
            print()
            if confirmar() and confirmar("CONFIRMA LA ELIMINACIÓN"):
                # agrega tanto el nombre como una lista vacía de contactos
                índice_grupo = grupos.index(nombre)

                del grupos[índice_grupo]
                del contactos_por_grupo[índice_grupo]

"""
funcionalidad 4.5: eliminar contactos de grupos
"""
def grupos_eliminar_contacto():
    while True:
        try:
            limpiar_terminal()

            # 10 espacios, título, nueva línea adicional
            print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
            print(" " * 10 + "ADMINISTRAR GRUPOS DE CONTACTOS")
            print(" " * 10 + "Eliminar contactos de los grupos" + "\n")

            nombre = input("Nombre del grupo" + " " * 4)

            if nombre == "C":
                break
            elif nombre not in grupos:
                input("Este grupo no existe, no se puede modificar. Presione <INTRO> ")
                continue

            índice_grupo = grupos.index(nombre)
            
            while True:
                telf = int(input("Teléfono" + " " * 12))
                área = input("Área" + " " * 16)

                if not área:
                    área = área_por_defecto
                else:
                    área = int(área)

                if (telf, área) not in dict_contactos:
                    input("Este contacto no está registrado, no se puede consultar. Presione <INTRO> ")
                else:
                    break

            contacto = contactos[dict_contactos[(telf, área)]]

            print(" " * 20 + areas[dict_áreas[área]][1])
            print("Nombre contacto" + " " * 5 + contacto[3] + "\n")

            print()
            if (telf, área) not in contactos_por_grupo[índice_grupo]:
                input("Este contacto no existe en el grupo, no puede eliminarlo. Presione <INTRO> ")
                continue

            if confirmar() and confirmar("CONFIRMA LA ELIMINACIÓN"):
                índice_contacto = contactos_por_grupo[índice_grupo] \
                    .index((telf, área))

                del contactos_por_grupo[índice_grupo][índice_contacto]

        except ValueError:
            input("[ERROR] El número y área de teléfono deben ser números. Presione <INTRO> ")
        except Exception as error:
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")


""" 
menú de opción 5: lista de contactos
obtiene diferentes filtros para varios campos de los contactos, y con ellos obtiene una lista filtrada
luego la traslada a una tabla en un archivo PDF
"""
def menú_lista_contactos():
    while True:
        limpiar_terminal()

        # 10 espacios, título, nueva línea adicional
        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        print(" " * 10 + "LISTA DE CONTACTOS" + "\n")
        
        # pide pada filtro secuencialmente y los popula automáticamente en una lista
        # cada filtro está asociado al índice del campo que trata
        # excepto el filtro de grupo; se trata diferente

        filtros = [
            (3, "Filtros:  Nombre contacto      "),
            (0, "          Teléfono             "),
            (1, "          Área                 "),
            (6, "          Fecha de nacimiento  "),
            (7, "          Pasatiempos          "),
        ]

        # hecho un iterador para mantener la consistencia (pues filter() retorna iteradores)
        contactos_finales = contactos

        # todos los filtros excepto el de grupo
        i = 0
        while i < len(filtros):
            filtro = filtros[i]

            entrada = input(filtro[1])

            if i == 0 and entrada == "C":
                return

            entrada = generar_patrón_regex(entrada)

            # si el filtro no es None
            if entrada != None and entrada != -1:
                """
                toma el valor de contacto en el índice del filtro y lo compara con el patrón del filtro respectivo
                devuelve un bool dependiendo de si hay match con el patrón

                entrada: contacto como lista
                salida: bool

                función local al ciclo for
                """
                def func_filtro_individual(contacto: list):
                    índice = filtro[0]

                    if entrada.match(str(contacto[índice])):
                        return True
                    
                    return False

                # se filtran los únicos elementos que cumplan el filtro respectivo
                contactos_finales = [c for c in contactos_finales if func_filtro_individual(c)]

            elif entrada == -1:
                input("[ERROR] El filtro es incorrecto (tiene más de 3 comodines). Presione <INTRO> ")
                continue
            

            i += 1

        # filtro de grupo
        filtro_grupo = -1
        while filtro_grupo == -1:
            filtro_grupo = generar_patrón_regex(input("          Grupo                "))
            if filtro_grupo == -1:
                input("[ERROR] El filtro es incorrecto (tiene más de 3 comodines). Presione <INTRO> ")

        """
        retorna si el contacto está en un grupo que tiene match con el regex del filtro de grupo

        entrada: contacto como lista de elementos
        salida: bool

        función local, solo para uso de su pariente
        """
        def func_filtro_grupo(contacto: tuple):
            # obtener los grupos en donde está contacto
            lista_grupos = grupos_de_contacto(contacto)

            for grupo in lista_grupos:
                # y el respectivo nombre de ese grupo hace match, es verdadero
                if filtro_grupo.match(grupo):
                    return True

            # si no existe tal grupo, retorna falso
            return False


        if filtro_grupo:
            contactos_finales = [c for c in contactos_finales if func_filtro_grupo(c)]

        if confirmar():
            try:
                tiempo = datetime.datetime.now()
                # formatear el tiempo para que sea colocable en un archivo
                tiempo_str = tiempo.strftime("_%Y%m%d_%H%M")

                nombre_archivo = "tabla_contactos" + tiempo_str + ".pdf"
                generar_tabla_pdf(nombre_archivo, contactos_finales)
                
                webbrowser.open(nombre_archivo)
                break
            except Exception as error:
                print(error)
                input("[ERROR] Sucedió un error no previsto. Presione <INTRO> ")

"""
funcionalidad 6: muestra el manual de usuario (como es un video, lo abre en el navegador)
"""
def menú_ayuda():
    limpiar_terminal()

    print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
    print(" " * 10 + "AYUDA" + "\n")

    webbrowser.open(URL_MANUAL)

    print("Si no se abre el video, puede insertar el URL en su navegador: " + URL_MANUAL)
    confirmar(solo_aceptar=True)


"""
funcionalidad 7: información del programa
"""
def menú_acerca_de():
    limpiar_terminal()

    # al lado derecho imprime un pequeñito teléfono
    print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
    print(" " * 10 + "ACERCA DE" + "\n")

    print("Versión: " + VERSIÓN + " " * (41 - len(VERSIÓN)) +      " _____")
    print("Fecha de creación: " + "2024/04/13" + " " * 21 +        "(.---.)-._.-.")
    print("Autor: " + "Fernando González Robles" + " " * 19 +      " /:::\\ _.---'")
    print("Programa 1 - IC1803 Taller de Programación" + " " * 8 + "'-----'")
    print()
    confirmar(solo_aceptar=True)


########################################
# Funciones auxiliares #################
########################################

"""
pide una confirmación de datos,
retorna True si se escribe "A", False si se escribe "C", y repite el proceso si no es ninguno de los dos
si la opción solo_aceptar se activa, solo se permite colocar "A"

entrada: string de mensaje (default es "OPCIÓN"), bool de solo tener opción de aceptar (default es falso)
salida: bool, o repite el proceso
"""
def confirmar(mensaje = "OPCIÓN", solo_aceptar = False) -> bool:
    mensaje_conf = mensaje + " " * 4 + "<A>Aceptar  <C>Cancelar "
    mensaje_error = '[ERROR] La opción debe ser "A" o "C". Presione <INTRO> '

    if solo_aceptar:
        mensaje_conf = mensaje_conf[:-12]
        mensaje_error = mensaje_error[:30] + mensaje_error[36:]

    confirmación = input(mensaje_conf)

    if confirmación == "A":
        return True
    elif not solo_aceptar and confirmación == "C":
        return False
    else:
        input(mensaje_error)
        # vuelve a llamar a la función y retorna el valor que esa devuelve (True o False)
        return confirmar(mensaje, solo_aceptar)

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
def área_registrada(área: int) -> bool:
    for registrada in areas:
        if registrada[0] == área:
            return True

    return False

"""
construye el diccionario de áreas y contactos
con base en la lista de áreas actuales
"""
def construir_diccionarios():
    # primero, limpiar ambos diccionarios
    dict_áreas.clear()
    dict_contactos.clear()

    # mapear cada número de área a su índice en la lista
    for índice, área in enumerate(areas):
        dict_áreas[área[0]] = índice

    # mapear cada tupla de teléfono a su índice en la lista
    for índice, contacto in enumerate(contactos):
        dict_contactos[(contacto[0], contacto[1])] = índice

"""
verifica si una fecha es correcta, y retorna "0", -1 o la fecha original, dependiendo de su validez

entrada: fecha como string
salida: fecha válida como string, o -1 si no es válida, o "0" si está incompleta
"""
def validar_fecha(fecha: str) -> str | int:
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
parte1@parte2, sin espacios

entrada: string
salida: bool
"""
def verificar_correo(correo: str) -> bool:
    # \S: caracteres que no sean espacios
    # \S+: 1 o más de esos
    # \S+@S+: cccc@cccc
    # ^\S+@\S+$: no permitir más caracteres fuera de cccc@cccc
    patrón = re.compile("^\\S+@\\S+$")
    # fullmatch retorna None o un objeto, pasar eso a bool (False y True, respectivamente)
    return bool(patrón.fullmatch(correo))

"""
generar un patrón de regex con base en los comodines
si entra un string vacía, devuelve None
abc -> ^abc$
%abc -> .*abc$
%ab%c% -> .*ab.*c$

entrada: string
salida: re.Pattern (objeto del patrón de regex), None o -1 (error)
"""
def generar_patrón_regex(string: str) -> re.Pattern | None | int:
    if not string:
        return None
    
    # si hay más de 3 %, devuelve un error
    if string.count("%") > 3:
        return -1

    # escapar caracteres especiales de regex
    string_nuevo = ""
    for char in string:
        # el backslash \ se debe a su vez escapar en python -> \\
        if char == "%":
            string_nuevo += ".*"
        elif char in ".^$*+?{}()[]\\|()":
            string_nuevo += "\\" + char
        else:
            string_nuevo += char

    string_nuevo = "^" + string_nuevo + "$"

    # compilar patrón con marca de ignorar mayúsculas
    # funciona para ignorarlas tanto en el patrón como en el objetivo
    return re.compile(string_nuevo, re.IGNORECASE)


"""
generar una tabla con información de los contactos
en un PDF usando PLATYPUS de la librería reportlab

entrada: nombre de archivo como string, lista de contactos
salida: None, pero genera un PDF
"""
def generar_tabla_pdf(nombre_archivo: str, contactos: list):
    # matriz con sus encabezados, se le añaden los contactos al final
    datos = [
        ["Número de teléfono", "Área", "Tipo", "Nombre", "Correo electrónico",
        "Dirección física", "Fecha de nacimiento", "Pasatiempos", "Notas"]
    ] + contactos

    # crear un nuevo documento con el nombre dado, tamaño carta, en modo horizontal
    doc = SimpleDocTemplate(nombre_archivo, pagesize=landscape(letter))

    # lista de elementos que PLATYPUS interpreta (párrafos, tablas, etc)
    flowables = []

    # estilos de texto
    estilos_texto = getSampleStyleSheet()

    # estilo de la tabla
    estilos_tabla = TableStyle([
        # tuplas       (columna, fila)
        # -1 lleva el estilo hasta la última columna/fila
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("0xB0C4DE"))
    ])
    
    texto_1 = Paragraph("Lista digital de contactos", style=estilos_texto["Heading1"])
    texto_2 = Paragraph("Tabla de contactos según filtros", style=estilos_texto["Heading2"])
    flowables += [texto_1, texto_2]

    # crear tabla, ponerle el estilo y colocarla en los flowables
    tabla = Table(datos, longTableOptimize=True)

    tabla.setStyle(estilos_tabla)
    flowables.append(tabla)

    doc.build(flowables)

"""
genera una lista con los nombres de los grupos en los que está un contacto
el contacto puede ser abreviado o completo

entrada: contacto como tupla
salida: lista de nombres de grupos a los que pertenece
"""
def grupos_de_contacto(contacto: tuple) -> list:
    lista_grupos = []
    for i, grupo in enumerate(contactos_por_grupo):
        # agarrar los primeros dos valores solamente y convertirlos a una tupla
        if tuple(contacto[:2]) in grupo:
            lista_grupos.append(grupos[i])

    return lista_grupos

########################################
# Función principal ####################
########################################
menú_principal()