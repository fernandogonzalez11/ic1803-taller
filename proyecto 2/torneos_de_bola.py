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

# diccionario con los equipos y su información, con formato:
# código: (nombre, posición)
equipos = {}

# lista de tuplas con los juegos establecidos a sus fechas respectivas
# esta lista se genera automáticamente con la opción 3
# cada fecha tiene juegos (código_casa, código_visita)
juegos = []

# lista de los resultados de cada juego, tiene relación 1:1 con juegos
# se popula la lista con valores iniciales inmediatamente después de la creación de juegos
# internamente, un resultado no añadido se almacena como () [tupla vacía]
# cada resultado tiene el formato (num_goles_casa, num_goles_visita)
resultados = []

# lista de los goleadores de cada juego, tiene relación 1:1 con juegos (aunque no se vea, jaja)
# se popula la lista con valores iniciales inmediatamente después de la creación de juegos
# internamente, una tupla de goles de casa y visita se almacena como () [tupla vacía]
# cada gol tiene el formato (goleador, minuto, reposición)
goleadores = []

# diccionario con formato "código: [jg, je, jp, gf, gc]"
# jg, je, jp -> juegos ganados, empatados, perdidos
# gf, gc -> goles a favor, en contra
# estos cinco valores se inicializan en 0 para cada equipo
estadísticas = {}

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
                menú_crear_calendario()
            case "4":
                menú_consultar_calendario()
            case "5":
                menú_registrar_resultados()
            case "6":
                menú_tabla_posiciones()
            case "7":
                pass
            case "8":
                pass
            case "9":
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
        print("REGISTRAR EQUIPOS: AGREGAR".center(50))
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
        print("REGISTRAR EQUIPOS: CONSULTAR".center(50))
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
        print("REGISTRAR EQUIPOS: MODIFICAR".center(50))
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
    if juegos:
        error("No se pueden eliminar equipos con el calendario de juegos ya creado")
        return
    
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR EQUIPOS: ELIMINAR".center(50))
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


"""
menú de opción 3: crear calendario de juegos
"""
def menú_crear_calendario():
    # permite editar la variable global juegos
    global juegos

    limpiar_terminal()

    # título, nueva línea adicional
    print("TORNEOS DE BOLA".center(50))
    print("CREAR CALENDARIO DE JUEGOS".center(50))
    print()    

    # verificar que esté configurado y que la longitud de equipos no sea ni más ni menos
    if equipos_participantes == 0 or len(equipos) != equipos_participantes:
        error("Debe primero configurar el torneo y añadir la cantidad correspondiente de equipos")
        return

    print("A continuación se creará automaticamente el calendario de juegos")
    print()

    # lista de fechas, cada fecha es una tupla que adentro tiene tuplas por partido
    fechas = []

    # lista con solo los códigos de los equipos (la llave de cada equipo)
    códigos_equipos = list(equipos.keys())

    # crear una copia de los códigos para manipular manteniendo la original intacta
    copia_códigos_equipos = códigos_equipos.copy()

    # crear las listas de fechas con un algoritmo de calendarización para un torneo todos contra todos
    # referencia: https://en.wikipedia.org/wiki/Round-robin_tournament#Circle_method
    # se desea correr este ciclo por lo menos una vez, para ello el booleano

    ### este ciclo corre hasta que se vuelve a la posición original,
    ### en cuyo caso se tendrían todas los partidos posibles de la primera ronda en sus fechas
    ciclo_empezado = False
    while not ciclo_empezado or copia_códigos_equipos != códigos_equipos:
        ciclo_empezado = True

        ### paso 1: se asocian los oponentes entre sí siguiendo un ordenamiento que emula una elipse
        ### ╭ 1 ⎼ 2 ⎼ 3 ⎼ 4 ╮
        ### │ ⇩   ⇩   ⇩   ⇩ │
        ### ╰ 8 ⎼ 7 ⎼ 6 ⎼ 5 ╯

        # el índice donde termina una mitad y empieza otra
        # como se empieza desde i = 0, representa el centro derecho en listas pares
        centro = len(equipos) // 2

        # primera mitad del inicio hasta el centro (excl.)
        sección_1 = copia_códigos_equipos[:centro]
        
        # segunda mitad del final al centro (incl.), en reversa
        sección_2 = copia_códigos_equipos[-1 : -centro - 1 : -1]

        # para los partidos, se asocia cada índice de sección_1 con el mismo índice en sección_2
        # la función zip permite esta funcionalidad (¡y cada par lo devuelve como tuplas!)
        # zip devuelve una lista, entonces se pasa a tupla
        fecha = tuple(zip(sección_1, sección_2))
        fechas.append(fecha)

        ### paso 2: se fija un elemento (el primero o último son los más convenientes)
        ### y se rotan una posición en modo horario todos los demás elementos
        ### ╭ 1 ⎼ 8 → 2 → 3 ╮
        ### │   ↗           │
        ### ╰ 7 ← 6 ← 5 ← 4 ╯

        # dejar fijo el primer elemento,
        # luego rotar poniendo el último de primero, y todos los restantes a su derecha
        copia_códigos_equipos = [copia_códigos_equipos[0], copia_códigos_equipos[-1]] + copia_códigos_equipos[1:-1]

    if confirmar("CONFIRMA LA CREACIÓN DEL CALENDARIO"):
        # añade la vuelta 1 de fechas generadas
        # se hace una copia para no afectar fechas cuando juegos se modifica
        juegos = fechas.copy()
        
        # y la vuelta 2, con las tuplas revertidas
        for fecha in fechas:
            juegos.append([(b, a) for a, b in fecha])

        # además, se popula tanto resultados como goleadores con las tuplas de cada fecha
        # como siguen el mismo modelo inicial, se puede almacenar la misma tupla
        for fecha in juegos:
            tupla_res_gol = ()

            for partido in fecha:
                tupla_res_gol += ( (), )

            resultados.append(tupla_res_gol)
            goleadores.append(tupla_res_gol)

        # crea la entrada del diccionario de estadísticas para cada equipo
        for equipo in equipos:
            estadísticas[equipo] = [0] * 5


def menú_consultar_calendario():
    limpiar_terminal()

    # título, nueva línea adicional
    print("TORNEOS DE BOLA".center(50))
    print("CONSULTAR CALENDARIO DE JUEGOS".center(50))
    print()

    # verificar que el calendario de juegos esté hecho
    if not juegos:
        error("Debe primero crear el calendario de juegos")
        return

    print(nombre_torneo)
    print()

    # para cada juego, imprimir el número de fecha y sus partidos
    for i, fecha in enumerate(juegos):
        print(f"Fecha {i + 1}")

        for equipo_1, equipo_2 in fecha:
            # obtener los nombres de los equipos con sus códigos
            print(f"{equipos[equipo_1][0]} — {equipos[equipo_2][0]}")

        print()

    confirmar(solo_aceptar=True)
            
"""
menú de opción 4: registrar resultados
maneja un CRUD de los resultados
0 para volver al menú principal
"""
def menú_registrar_resultados():
        while True:
            limpiar_terminal()

            # título, nueva línea adicional
            print("TORNEOS DE BOLA".center(50))
            print("REGISTRAR RESULTADOS".center(50))
            print()
            print("1. Agregar resultados")
            print("2. Consultar resultados")
            print("3. Modificar resultados")
            print("4. Eliminar resultados")
            print("0. Fin")
            print()

            # pedir opción
            opción = input("   OPCIÓN: ")

            match opción:
                case "1":
                    resultados_agregar()
                case "2":
                    resultados_consultar()
                case "3":
                    resultados_modificar()
                case "4":
                    resultados_eliminar()
                case "0":
                    # finalizar el ciclo, y en turno volver al menú principal
                    break
                case _:
                    error("La opción digitada no es válida")

"""
funcionalidad 4.1: agregar resultados

pide el código de casa y visita, el número de goles de cada equipo, y por cada gol pide:
- el nombre del goleador
- el minuto del gol (de 1 a 120, negativo si es autogol)
- si el minuto es 45 o 90, la reposición (sin límite, pero debe empezar con +) (+3, +12, etc.)

al tener todos los goles listos, actualiza resultados y goleadores con sus formatos respectivos

el parámetro modificar es False por defecto. si es True, permite sobreescribir un resultado
"""
def resultados_agregar(modificar=False):
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))

        if modificar:
            encabezado_operación = "MODIFICAR"
        else:
            encabezado_operación = "AGREGAR"

        print(f"REGISTRAR RESULTADOS: {encabezado_operación}".center(50))
        print()
        
        casa = input("Código del equipo casa:".ljust(30))

        # cancelar con C
        if casa == "C":
            return
        
        visita = input("Código del equipo visita:".ljust(30))

        # como juegos comprende a todos los del producto cartesiano equipos x equipos,
        # solo se debe verificar que ambos equipos estén y no sean iguales
        if casa in equipos and visita in equipos and casa != visita:
            # se encuentra la posición de la fecha y del juego en esa fecha
            # cuando el ciclo se corta, ya se tienen los índices almacenados
            for i_fecha, fecha in enumerate(juegos):
                try:
                    j_fecha = fecha.index((casa, visita))
                    break
                except:
                    continue
            
            # para la operación de agregar
            # si el resultado del partido ya tiene datos (no es tupla vacía)
            if not modificar and resultados[i_fecha][j_fecha]:
                error("Este juego ya está registrado, no se puede agregar")
                continue

            # para la de modificar
            # si más bien no tiene datos
            elif modificar and not resultados[i_fecha][j_fecha]:
                error("Este juego no está registrado, no se puede modificar")
            
        else:
            error("Este juego no está en el calendario, no se puede registrar resultado")
            continue
        
        # línea separadora entre códigos y goles
        print()

        """
        crea y retorna la tupla de goles para un equipo, según su cantidad de goles
        entrada: int (cantidad de goles del equipo)
        salida: tuple (tupla de tuplas con los nombres y minutos de cada gol)

        función local a resultados_agregar()
        """
        def crear_goles(num_goles_equipo: int) -> tuple:
            goles_equipo = ()
            for gol in range(num_goles_equipo):

                print(f"  - Gol {gol + 1}")

                # solicitar el nombre del goleador
                while True:
                    nombre_goleador = input(f"  Nombre del goleador".ljust(30))

                    if len(nombre_goleador) < 2 or len(nombre_goleador) > 40:
                        error("El nombre del goleador debe ser entre 2 y 40 caracteres")
                    else:
                        break
                
                # solicitar el minuto en que ocurrió el gol
                while True:
                    minuto_gol = input(f"  Minuto".ljust(30))

                    # contar válidos "10" y "-10"
                    if not minuto_gol.isnumeric() and not minuto_gol[1:].isnumeric():
                        error("El minuto del gol debe ser un número")
                        continue

                    minuto_gol = int(minuto_gol)

                    
                    if abs(minuto_gol) < 1 or abs(minuto_gol) > 120:
                        error("El minuto del gol debe ser de 1 a 120, o -1 a -120 para autogoles")
                    else:
                        break
                
                # solicitar el minuto de reposición (si los minutos normales son 45 o 90)
                reposición = 0
                while abs(minuto_gol) == 45 or abs(minuto_gol) == 90:
                    reposición = input(f"  Reposición".ljust(30))

                    if not reposición:
                        reposición = 0
                        break
                    
                    # el formato es +n, donde n comprende de 0 a 30
                    if reposición[0] != "+" or not reposición[1:].isnumeric():
                        error("El minuto de reposición debe ser un número empezando con \"+\" (ej: +3)")
                        continue
                    
                    reposición = int(reposición[1:])
                    break
                    

                # formar la tupla y añadirla a los goles del equipo
                tupla_gol = (nombre_goleador, minuto_gol, reposición)
                goles_equipo += (tupla_gol,)

                # separar cada gol con una nueva línea
                print()

            return goles_equipo
            
        # pedir la cantidad de goles de casa, y los goleadores de cada uno
        while True:
            num_goles_casa = input("Goles del equipo casa:".ljust(30))

            if not num_goles_casa.isnumeric() or int(num_goles_casa) < 0:
                error("Los goles deben ser un número positivo")
            else:
                num_goles_casa = int(num_goles_casa)
                break

        goles_casa = crear_goles(num_goles_casa)    


        # pedir la cantidad de goles de visita, y los goleadores de cada uno
        while True:
            num_goles_visita = input("Goles del equipo visita:".ljust(30))

            if not num_goles_visita.isnumeric() or int(num_goles_visita) < 0:
                error("Los goles deben ser un número positivo")
            else:
                num_goles_visita = int(num_goles_visita)
                break

        goles_visita = crear_goles(num_goles_visita)

        # línea separadora entre los goles y la confirmación
        print()
        if confirmar():
            # asignar el resultado y los goleadores a la fecha y partido respectivo
            # como las listas están formadas como tuplas, se debe recrear la tupla
            # en lugar de solo reemplazar elementos

            res_fecha = resultados[i_fecha]
            gols_fecha = goleadores[i_fecha]

            # en la fecha, el nuevo resultado será una tupla (p1, p2)
            # donde p1 y p2 son números de cada equipo
            res_fecha = res_fecha[:j_fecha] + ( (num_goles_casa, num_goles_visita), ) + res_fecha[j_fecha + 1:]

            # en la fecha, los nuevos goleadores serán una tupla ((...), (...))
            # donde (...) son goles (como tuplas) de cada equipo
            gols_fecha = gols_fecha[:j_fecha] + ( ( goles_casa, goles_visita ), ) + gols_fecha[j_fecha + 1:]

            # reemplazar las tuplas en la lista original
            resultados[i_fecha] = res_fecha
            goleadores[i_fecha] = gols_fecha

            # crear aliases (no son copias) de las estadísticas para editarlos
            # estadística -> código: [jg, je, jp, gf, gc]
            estadística_casa = estadísticas[casa]
            estadística_visita = estadísticas[visita]

            # pierde visita
            if num_goles_casa > num_goles_visita:
                estadística_casa[0] += 1
                estadística_visita[2] += 1
            # pierde casa
            elif num_goles_visita > num_goles_casa:
                estadística_casa[2] += 1
                estadística_visita[0] += 1
            # empatan
            else:
                estadística_casa[1] += 1
                estadística_visita[1] += 1
            
            # en todos los casos, añadir los goles a favor y en contra
            estadística_casa[3] += num_goles_casa
            estadística_casa[4] += num_goles_visita
            estadística_visita[3] += num_goles_visita
            estadística_visita[4] += num_goles_casa

"""
funcionalidad 4.2: consultar resultados

pide los códigos de equipos y despliega los datos asociados a ese partido
"""
def resultados_consultar():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR RESULTADOS: CONSULTAR".center(50))
        print()

        while True:
            casa = input("Código del equipo casa:".ljust(30))

            # cancelar con C
            if casa == "C":
                return
            
            visita = input("Código del equipo visita:".ljust(30))

            # como juegos comprende a todos los del producto cartesiano equipos x equipos,
            # solo se debe verificar que ambos equipos estén y no sean iguales
            if casa in equipos and visita in equipos and casa != visita:
                # se encuentra la posición de la fecha y del juego en esa fecha
                # cuando el ciclo se corta, ya se tienen los índices almacenados
                for i_fecha, fecha in enumerate(juegos):
                    try:
                        j_fecha = fecha.index((casa, visita))
                        break
                    except:
                        continue
                
                # si el resultado del partido no tiene datos (es tupla vacía)
                if not resultados[i_fecha][j_fecha]:
                    error("Este juego no está registrado, no se puede consultar")
                else:
                    break
            else:
                error("Este juego no está en el calendario, no se puede consultar resultado")
        
        # línea separadora entre códigos y despliegues
        print()

        resultado = resultados[i_fecha][j_fecha]

        # imprimir el puntaje de cada equipo
        print(casa.center(7) + "-" + visita.center(7))
        print(str(resultado[0]).center(7) + "-" + str(resultado[1]).center(7))
        print()
        
        goles = goleadores[i_fecha][j_fecha]
        # imprimir los goles del equipo casa
        if goles[0]:
            print("Goles de", equipos[casa][0], "(casa):")
            for gol_casa in goles[0]:
                string_gol = f"  {gol_casa[0]} en '{gol_casa[1]}"
                if gol_casa[2]:
                    string_gol += f" +{gol_casa[2]}"

                print(string_gol)
            print()

        if goles[1]:
            print("Goles de", equipos[visita][0], "(visita):")
            for gol_visita in goles[1]:
                string_gol = f"  {gol_visita[0]} en '{gol_visita[1]}"
                if gol_visita[2]:
                    string_gol += f" +{gol_visita[2]}"

                print(string_gol)
            print()

        
        confirmar(solo_aceptar=True)

def resultados_modificar():
    resultados_agregar(modificar=True)

def resultados_eliminar():
    while True:
        limpiar_terminal()

        # título, nueva línea adicional
        print("TORNEOS DE BOLA".center(50))
        print("REGISTRAR RESULTADOS: ELIMINAR".center(50))
        print()

        
        casa = input("Código del equipo casa:".ljust(30))

        # cancelar con C
        if casa == "C":
            return
        
        visita = input("Código del equipo visita:".ljust(30))

        # como juegos comprende a todos los del producto cartesiano equipos x equipos,
        # solo se debe verificar que ambos equipos estén y no sean iguales
        if casa in equipos and visita in equipos and casa != visita:
            # se encuentra la posición de la fecha y del juego en esa fecha
            # cuando el ciclo se corta, ya se tienen los índices almacenados
            for i_fecha, fecha in enumerate(juegos):
                try:
                    j_fecha = fecha.index((casa, visita))
                    break
                except:
                    continue
            
            # si el resultado del partido no tiene datos (es tupla vacía)
            if not resultados[i_fecha][j_fecha]:
                error("Este juego no está registrado, no se puede eliminar")
                continue
        else:
            error("Este juego no está en el calendario, no se puede eliminar resultado")
            continue
        
        # línea separadora entre códigos y despliegues
        print()

        # pedir doble confirmación de eliminación
        if confirmar() and confirmar("CONFIRMA LA ELIMINACIÓN"):
            res_fecha = resultados[i_fecha]
            gols_fecha = goleadores[i_fecha]

            # (1) revertir todos los cambios de las estadísticas

            # crear aliases (no son copias) de las estadísticas para editarlos
            # estadística -> código: [jg, je, jp, gf, gc]
            estadística_casa = estadísticas[casa]
            estadística_visita = estadísticas[visita]
            res_partido = res_fecha[j_fecha]

            # pierde visita
            if res_partido[0] > res_partido[1]:
                estadística_casa[0] -= 1
                estadística_visita[2] -= 1
            # pierde casa
            elif res_partido[1] > res_partido[0]:
                estadística_casa[2] -= 1
                estadística_visita[0] -= 1
            # empatan
            else:
                estadística_casa[1] -= 1
                estadística_visita[1] -= 1
            
            # quitar los goles a favor y en contra
            estadística_casa[3] -= res_partido[0]
            estadística_casa[4] -= res_partido[1]
            estadística_visita[3] -= res_partido[1]
            estadística_visita[4] -= res_partido[0]

            # (2) revertir las listas de resultados y goleadores

            # limpiar el contenido de solo el partido específico de la fecha
            res_fecha = res_fecha[:j_fecha] + ( (), ) + res_fecha[j_fecha + 1:]

            # de igual manera para los goles
            gols_fecha = gols_fecha[:j_fecha] + ( (), ) + gols_fecha[j_fecha + 1:]

            resultados[i_fecha] = res_fecha
            goleadores[i_fecha] = gols_fecha

def menú_tabla_posiciones():
    # tener un diccionario con formato "código: (jg, je, jp, gf, gc)"
    # luego, hacer una lista con (código, (puntos, gc, escalafón))
    # y ordenarla según key = elem[1]

    limpiar_terminal()

    # título, nueva línea adicional
    print("TORNEOS DE BOLA".center(50))
    print("CONSULTAR CALENDARIO DE JUEGOS".center(50))
    print()

    # verificar que el calendario de juegos esté hecho (y subsecuentemente resultados y goleadores)
    if not juegos:
        error("Debe primero crear el calendario de juegos")
        return

    # se hace una lista de tuplas con el formato (código, (puntos, gd, gf, escalafón))
    tuplas_por_ordenar = []
    for equipo in equipos:
        estadística_equipo = estadísticas[equipo]
        puntos = estadística_equipo[0] * puntos_ganado + estadística_equipo[1] * puntos_empatado
        gd = estadística_equipo[3] - estadística_equipo[4]

        tuplas_por_ordenar.append((equipo, (puntos, gd, estadística_equipo[3], equipos[equipo][1])))

    # ahora que se tiene la lista ordenada, se imprimen todas las estadísticas en ese orden

    # un sort con tuplas implica ordenar con el primer elemento
    # y si en ese se empata, ordenar con el segundo, y así sucesivamente
    tuplas_por_ordenar.sort(key=lambda tupla: tupla[1])

    # imprimir los encabezados
    print(nombre_torneo)
    print("Tabla de posiciones")
    print("Equipos que clasifican:", equipos_clasifican)
    print()

    str_encabezado = "Equipo".ljust(20)

    for encabezado in ("JJ", "JG", "JP", "JE", "GF", "GC", "GD", "Puntos"):
        str_encabezado += encabezado.ljust(5)
    
    str_encabezado += "\n" + "─" * (20 + 5 * 8 + 2)

    print(str_encabezado)

    str_equipos = ""

    # estadísticas_resto tiene algunas estadísticas, estadísticas[equipo] tiene más; se desempaquetan ambas
    for equipo, estadísticas_resto in tuplas_por_ordenar:
        jg, je, jf, gf, gc = estadísticas[equipo]

        # _ es el estándar de una variable desusada, y con * agarra todo lo que
        # sobra de estadísticas_resto al final
        puntos, gd, *_ = estadísticas_resto

        str_equipo = equipos[equipo][0].ljust(20)
        
        # añadir los valores de la tabla al string por imprimir
        # añade un + solo con positivos en diferencia de goles
        if gd > 0:
            gd = f"+{gc}"

        for valor in (jg + je + jf, jg, je, jf, gf, gc, gd, puntos):
            str_equipo += str(valor).ljust(5)
        
        print(str_equipo)
        str_equipos += str_equipo + "\n"

    # TODO: enviar correo
    if confirmar("¿Enviar un correo electrónico con la tabla?"):
        while True:
            correo = input("Digite su dirección de correo: ")
            return


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

# configuración del torneo
nombre_torneo = "copa airlines"
equipos_participantes = 6
equipos_clasifican = 2
puntos_ganado = 3
puntos_empatado = 1

# diccionario con los equipos y su información
equipos = {
    "CRC": ("Costa Rica", 1),
    "USA": ("Estados Unidos", 2),
    "MEX": ("México", 3),
    "HND": ("Honduras", 4),
    "SAL": ("El Salvador", 5),
    "PAN": ("Panamá", 6)
}

juegos = [(('CRC', 'PAN'), ('USA', 'SAL'), ('MEX', 'HND')), (('CRC', 'SAL'), ('PAN', 'HND'), ('USA', 'MEX')), (('CRC', 'HND'), ('SAL', 'MEX'), ('PAN', 'USA')), (('CRC', 'MEX'), ('HND', 'USA'), ('SAL', 'PAN')), (('CRC', 'USA'), ('MEX', 'PAN'), ('HND', 'SAL')), [('PAN', 'CRC'), ('SAL', 'USA'), ('HND', 'MEX')], [('SAL', 'CRC'), ('HND', 'PAN'), ('MEX', 'USA')], [('HND', 'CRC'), ('MEX', 'SAL'), ('USA', 'PAN')], [('MEX', 'CRC'), ('USA', 'HND'), ('PAN', 'SAL')], [('USA', 'CRC'), ('PAN', 'MEX'), ('SAL', 'HND')]]
resultados = [((), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), ((2, 1), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), ((), (), ())]
goleadores = [((), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), (((('ovario', 10, 0), ('duende', 45, 3)), (('dickins', 90, 2),)), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), ((), (), ()), ((), (), ())]
estadísticas = {'CRC': [1, 0, 0, 2, 1], 'USA': [0, 0, 1, 1, 2], 'MEX': [0, 0, 0, 0, 0], 'HND': [0, 0, 0, 0, 0], 'SAL': [0, 0, 0, 0, 0], 'PAN': [0, 0, 0, 0, 0]}

########################################
# Función principal ####################
########################################
menú_principal()