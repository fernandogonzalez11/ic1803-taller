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



########################################
# Funcionalidades base #################
########################################
def menu_principal():
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

        print(" " * 10 + "LISTA DIGITAL DE CONTACTOS" + "\n")
        # imprimir todas las opciones
        for num, nombre in opciones.items():
            print(num + ". " + nombre)
        # pedir opción
        opción = input("  OPCIÓN: ")

        match opción:
            case "1":
                pass
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

                

########################################
# Funciones auxiliares #################
########################################
def limpiar_terminal():
    # en windows
    if os.name == "nt":
        os.system("cls")
    # linux, mac, etc
    else:
        os.system("clear")

########################################
# Pruebas ##############################
########################################

########################################
# Función principal ####################
########################################
menu_principal()