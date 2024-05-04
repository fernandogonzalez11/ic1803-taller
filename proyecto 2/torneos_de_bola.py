"""
Torneos de bola

Fernando Andrés González Robles
Carné 2024201276
Taller de programación
Prof. William Mata
Grupo 4
"""

########################################
# Módulos ##############################
########################################

# utilizado para obtener información sobre el sistema operativo
import os

# utilizado para leer y escribir datos en archivos
import pickle

########################################
# Variables principales ################
########################################

# variables establecidas en la configuración
nombre_torneo = ""
equipos_participantes = 0
equipos_clasifican = 0
puntos_ganado = 0
puntos_empatado = 0

# diccionario con los equipos y su información
equipos = {}


########################################
# Funcionalidades base #################
########################################

"""
menú principal
pide infinitamente entradas para enramarse a otros menús o funciones
se puede salir del menú digitando "0"
"""
def menú_principal():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print()
        print("1. Configuración del torneo")
        print("2. Registrar equipos")
        print("3. Crear calendario de juegos")
        print("4. Consultar calendario de juegos")
        print("5. Registrar los resultados")
        print("6. Tabla de posiciones")
        print("7. Tabla de goleadores")
        print("8. Ayuda")
        print("9. Acerca de")
        print("0. Fin")
        print()

        # pedir opción
        opción = input("   OPCIÓN: ")

        match opción:
            case "1":
                menú_config_torneo()
            case "2":
                menú_registrar_equipos()
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
                error("La opción digitada no es válida")

"""
menú de opción 1: configuración del torneo
se configura el nombre del torneo, los participantes, cuántos equipos clasifican, cuánto equivale un gane y un empate
"""
def menú_config_torneo():
    # bloquea al usuario cuando ya hay equipos registrados
    if len(equipos):
        error("Ya hay equipos registrados, no se puede cambiar la configuración")
        return

    global nombre_torneo, equipos_participantes, equipos_clasifican, puntos_ganado, puntos_empatado
    
    limpiar_terminal()

    print("TORNEOS DE BOLA".center(50))
    print("CONFIGURACIÓN DEL TORNEO".center(50))
    print()

    datos = ["", 0, 0, 0, 0]

    # pedir el nombre del torneo
    while True:
        datos[0] = input("Nombre del torneo: ")

        if len(datos[0]) >= 5 and len(datos[0]) <= 40:
            break
        else:
            error("El nombre del torneo debe ser entre 5 y 40 caracteres")

    # pedir la cantidad de equipos participantes
    while True:
        datos[1] = input("Cantidad de equipos participantes: ")

        if not datos[1].isnumeric():
            error("La cantidad de equipos participantes debe ser un entero")
        else:
            datos[1] = int(datos[1])

            if datos[1] < 2 or datos[1] % 2 != 0:
                error("La cantidad de equipos participantes debe ser par y mayor que 2")
            else:
                break
    
    # pedir la cantidad de equipos que clasifican
    while True:
        datos[2] = input("Cantidad de equipos que clasifican directamente: ")

        if not datos[2].isnumeric():
            error("La cantidad de equipos que clasifican debe ser un entero")
        else:
            datos[2] = int(datos[2])

            if datos[2] < 1 or datos[2] >= datos[1]:
                error("La cantidad de equipos participantes debe ser mayor o igual a 1 y menor que los equipos participantes")
            else:
                break

    # pedir la cantidad de puntos por partido ganado
    while True:
        datos[3] = input("Puntos ganados por cada partido ganado: ")

        if not datos[3].isnumeric():
            error("Los puntos del gane deben ser un entero")
        else:
            datos[3] = int(datos[3])

            if datos[3] < 1:
                error("Los puntos del gane deben ser mayor o igual a 1")
            else:
                break

    # pedir la cantidad de puntos por partido empatado
    while True:
        datos[4] = input("Puntos ganados por cada partido empatado: ")

        if not datos[4].isnumeric():
            error("Los puntos del empate deben ser un entero")
        else:
            datos[4] = int(datos[4])

            if datos[4] < 1 or datos[4] >= datos[3]:
                error("Los puntos del empaten deben ser mayor o igual a 1 y menor que los puntos del gane")
            else:
                break
    
    # pedir confirmación
    if confirmar():
        nombre_torneo = datos[0]
        equipos_participantes = datos[1]
        equipos_clasifican = datos[2]
        puntos_ganado = datos[3]
        puntos_empatado = datos[4]


"""
menú de opción 2: registrar equipos
maneja un CRUD de los equipos
0 para volver al menú principal
"""
def menú_registrar_equipos():
        while True:
            limpiar_terminal()

            # título, nueva línea adicional
            print("TORNEOS DE BOLA".center(50))
            print("REGISTRAR EQUIPOS".center(50))
            print()
            print("1. Agregar equipos")
            print("2. Consultar equipos")
            print("3. Modificar equipos")
            print("4. Eliminar equipos")
            print("0. Fin")
            print()

            # pedir opción
            opción = input("   OPCIÓN: ")

            match opción:
                case "1":
                    equipos_agregar()
                case "2":
                    equipos_consultar()
                case "3":
                    equipos_modificar()
                case "4":
                    equipos_eliminar()
                case "0":
                    # finalizar el ciclo, y en turno volver al menú principal
                    break
                case _:
                    error("La opción digitada no es válida")

"""
funcionalidad 2.1: agregar equipos
asocia un código de equipo con su nombre y posición en un escalafón, y lo añade al diccionario de equipos
para accesar esta funcionalidad se debe configurar el torneo antes
"""
def equipos_agregar():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR EQUIPOS: AGREGAR EQUIPOS".center(50))
        print()

        # con que uno de los valores sea el inicial se sabe que no se ha configurado
        if not nombre_torneo:
            error("Se debe primero configurar el torneo")
            return

        # pedir código del equipo
        while True:
            código_equipo = input("Código del equipo".ljust(30))

            # volver al menú con C
            if código_equipo == "C":
                return

            if len(código_equipo) != 3 or not código_equipo.isupper():
                error("El nombre del equipo deben ser tres letras en mayúscula")
                continue

            if código_equipo in equipos:
                error("El equipo ya está registrado, no se puede agregar")
            else:
                break
        
        # pedir nombre del equipo
        while True:
            nombre_equipo = input("Nombre del equipo".ljust(30))

            if len(nombre_equipo) < 3 or len(nombre_equipo) > 40:
                error("El nombre del equipo debe tener entre 3 y 40 caracteres")
                continue

            for eq in equipos:
                if equipos[eq][0] == nombre_equipo:
                    error("Ya existe un equipo con este nombre")
                    break
            else:
                break
            
        
        # pedir posición en el escalafón
        while True:
            posición = input("Posición en el escalafón".ljust(30))

            if not posición.isnumeric():
                error("La posición debe ser un número")
                continue
        
            posición = int(posición)
            if posición < 1:
                error("La posición debe ser 1 o mayor")
                continue
                
            for eq in equipos:
                if equipos[eq][1] == posición:
                    error("Ya existe un equipo con esta posición")
                    break
            else:
                break

        if confirmar():
            equipos[código_equipo] = (nombre_equipo, posición)

"""
funcionalidad 2.2: consultar equipos
muestra información de un equipo según su código
"""
def equipos_consultar():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR EQUIPOS: CONSULTAR EQUIPOS".center(50))
        print()

        código_equipo = input("Código del equipo: ")

        if código_equipo == "C":
            break

        if código_equipo not in equipos:
            error("El equipo no está registrado, no se puede consultar")
            continue

        equipo = equipos[código_equipo]
        print("Nombre del equipo".ljust(30), equipo[0])
        print("Posición en el escalafón".ljust(30), equipo[1])
        print()

        confirmar(solo_aceptar=True)

"""
funcionalidad 2.3: modificar equipos
solicita el código y permite modificar los valores del equipo asociado
"""
def equipos_modificar():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR EQUIPOS: MODIFICAR EQUIPOS".center(50))
        print()

        código_equipo = input("Código del equipo: ")

        if código_equipo == "C":
            break

        if código_equipo not in equipos:
            error("El equipo no está registrado, no se puede consultar")
            continue

        # obtener el equipo actual
        equipo = equipos[código_equipo]

        print(" " * 55 + "NUEVOS VALORES")

        # pedir nombre del equipo
        while True:
            nuevo_nombre = input("Nombre del equipo".ljust(30) + equipo[0].rjust(20) + " =>  ")

            # llenar automáticamente el valor y salir
            if nuevo_nombre == "":
                nuevo_nombre = equipo[0]
                break
            
            if len(nuevo_nombre) < 3 or len(nuevo_nombre) > 40:
                error("El nombre del equipo debe tener entre 3 y 40 caracteres")
                continue

            for eq in equipos:
                if equipos[eq][0] == nuevo_nombre:
                    error("Ya existe un equipo con este nombre")
                    break
            else:
                break
        
        # pedir posición en el escalafón
        while True:
            nueva_posición = input("Posición en el escalafón".ljust(30) + str(equipo[1]).rjust(20) + " =>  ")

            # llenar automáticamente el valor y salir
            if nueva_posición == "":
                nueva_posición = equipo[1]
                break
            
            if not nueva_posición.isnumeric():
                error("La posición debe ser un número")
                continue
        
            nueva_posición = int(nueva_posición)
            if nueva_posición < 1:
                error("La posición debe ser 1 o mayor")
                continue
                
            for eq in equipos:
                if equipos[eq][1] == nueva_posición:
                    error("Ya existe un equipo con esta posición")
                    break
            else:
                break

        if confirmar():
            equipos[código_equipo] = (nuevo_nombre, nueva_posición)

"""
funcionalidad 2.4: eliminar equipos
solicita el código y elimina al equipo asociado del diccionario
solo se pueden eliminar grupos si no se creó ya el calendario
"""
def equipos_eliminar():
    # TODO: Las eliminaciones de equipos se permiten solo cuando el calendario de juegos no esté hecho.

    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR EQUIPOS: ELIMINAR EQUIPOS".center(50))
        print()

        código_equipo = input("Código del equipo: ")

        if código_equipo == "C":
            break

        if código_equipo not in equipos:
            error("El equipo no está registrado, no se puede consultar")
            continue

        equipo = equipos[código_equipo]

        print("Nombre del equipo".ljust(30), equipo[0])
        print("Posición en el escalafón".ljust(30), equipo[1])
        print()

        # debe pasar dos confirmaciones para borrar el equipo
        if confirmar() and confirmar("CONFIRMA LA ELIMINACIÓN"):
            del equipos[código_equipo]



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
imprime un mensaje de error
"""
def error(mensaje="Ocurrió un error imprevisto"):
    input("[ERROR] " + mensaje + ". Presione <INTRO> ")

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


########################################
# Pruebas ##############################
########################################

########################################
# Función principal ####################
########################################
menú_principal()