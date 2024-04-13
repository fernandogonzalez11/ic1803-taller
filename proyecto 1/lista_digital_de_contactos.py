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
        opción = input("  OPCIÓN: ")

        match opción:
            case "1":
                menú_registrar()
            case "2":
                pass
            case "3":
                pass
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
def menú_registrar():
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
        opción = input("  OPCIÓN: ")

        match opción:
            case "1":
                registrar_agregar()
            case "2":
                registrar_consultar()
            case "3":
                registrar_modificar()
            case "4":
                registrar_eliminar()
            case "0":
                # finalizar el ciclo, esto regresa al menú principal
                break
            case _:
                input("[ERROR] La opción digitada no es válida. Presione <INTRO>")      

"""
funcionalidad 1.1: agregar áreas
pide un número y nombre de área y lo registra (con respectivas verificaciones)
"""
def registrar_agregar():
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
                input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO>")
                # retorna al inicio del while
                continue
            
            # revisar si el número existe en alguna área registrada
            if área_registrada(número):
                input("Esta área ya está registrada, no se puede agregar. Presione <INTRO>")
                continue
            
            nombre = input("Nombre del área" + " " * 5)

            if len(nombre) < 1 or len(nombre) > 40:
                input("[ERROR] El nombre de área debe ser entre 1 y 40 caracteres. Presione <INTRO>")
                continue

            confirmación = input("OPCIÓN    <A>Aceptar    <C>Cancelar  ")

            if confirmación == "A":
                areas.append((número, nombre))
                dict_áreas[número] = len(areas) - 1

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO>")
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO>")

"""
funcionalidad 1.2: consultar áreas
imprime información de un área (si está registrada) con su número
"""
def registrar_consultar():
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
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO>")
                continue
            
            # encontrar el nombre usando el diccionario
            nombre = areas[dict_áreas[número]][1]

            print()
            print("Nombre del área" + " " * 5 + nombre)

            input("OPCIÓN    <A>Aceptar  ")

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO>")
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO>")

"""
funcionalidad 1.3: modificar áreas
pide el área, y modifica su nombre (si está registrada)
"""
def registrar_modificar():
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
                input("Esta área no está registrada, no se puede consultar. Presione <INTRO>")
                continue
            
            nombre = areas[dict_áreas[número]][1]

            print(" " * 33 + "NUEVO VALOR")
            print("Nombre del área  " + nombre)

            nuevo = input(" " * 33)

            if nuevo == "":
                nuevo = nombre

            elif len(nuevo) > 40:
                input("[ERROR] El nuevo nombre debe ser entre 1 y 40 caracteres. Presione <INTRO>")
                continue

            confirmación = input("OPCIÓN    <A>Aceptar  <C>Cancelar ")

            if confirmación == "A":
                areas[dict_áreas[número]] = (número, nuevo)

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO>")
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO>")
    
"""
funcionalidad 1.4: eliminar áreas
pide el área, elimina su entrada en el registro (si está registrada), y actualiza el diccionario de índices
"""
def registrar_eliminar():
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
            
            # TODO: verificar que no hayan contactos asociados

            # encontrar el nombre usando el diccionario
            índice = dict_áreas[número]

            print()
            print("Nombre del área" + " " * 5 + areas[índice][1])

            confirmación = input("CONFIRMA LA ELIMINACIÓN    <A>Aceptar  <C>Cancelar ")

            if confirmación == "A":
                del areas[índice]
                construir_dict_áreas()

        # sucede cuando número no se puede convertir a int
        except ValueError:
            input("[ERROR] El área debe ser un número entre 0 y 999. Presione <INTRO>")
        except Exception as error:
            print(error)
            input("[ERROR] Sucedió un error no previsto. Presione <INTRO>")


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
def área_registrada(área):
    for registrada in areas:
        if registrada[0] == área:
            return True

    return False

"""
construye el diccionario de áreas con base en la lista de áreas actuales
"""
def construir_dict_áreas():
    for índice, área in enumerate(areas):
        dict_áreas[área[0]] = índice


########################################
# Pruebas ##############################
########################################
areas = [(502, "Guatemala"), (506, "Costa Rica"), (507, "Nicaragua")]
construir_dict_áreas()


########################################
# Función principal ####################
########################################
menú_principal()