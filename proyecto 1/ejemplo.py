#########################################################################
# LISTA DIGITAL DE CONTACTOS                                                                                #
#########################################################################

#########################################################################
# MÓDULOS                                                                                                                  #
#########################################################################
import os # para usar system("cls") /clear screen

#########################################################################
# FUNCIONES                                                                                                               #
#########################################################################

#########################################################################
# OPCIÓN REGISTRAR ÁREAS                                                                                     #
#########################################################################

# Obtener datos de un area
# Entradas: lista de áreas, código de área
# Salidas: Si área existe en la lista retorna True y la tupla con sus datos, sino existe retorna False y tupla vacía
def obtener_datos_area(areas, area_telefono):
    for elemento in areas:
        if elemento[0] == area_telefono:
            return True, elemento
    return False, tuple()

# Agregar áreas
# Entradas: lista de áreas
# S: lista de áreas actualizada 
def agregar_areas(areas):
        while True:
            os.system("cls")
            print("\n\n\n-------------------------------------------------------------------------------")
            print("                     REGISTRAR ÁREAS\n")
            print("                     AGREGAR ÁREAS\n")
            # leer área
            while True:
                try:
                    area_telefono = input("Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            input("ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR ")
                        else:
                            break
                    else:
                        input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
            # leer nombre del área     
            while True:
                nombre_del_area = input("Nombre del área: ") 
                if len(nombre_del_area) >= 1 and len(nombre_del_area) <= 40:
                    break
                else:
                    input("EL DATO DEBE TENER ENTRE 1 Y 40 CARACTERES ")
            # leer opción
            while True:
                opcion = input("OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    areas.append((area_telefono, nombre_del_area))
                    break
                if opcion == "C":
                    print("Operación cancelada")
                    break
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
            
def consultar_areas(areas):
    pass

def  modificar_areas(areas):
    pass

def eliminar_areas(areas):
    pass
                    
# menú registrar áreas                          
def crud_areas(areas):
    while True:
        os.system("cls")
        print("\n\n\n-------------------------------------------------------------------------------")
        print("                     LISTA DIGITAL DE CONTACTOS\n")
        print("                            REGISTRAR ÁREAS\n")
        print(" 1. Agregar áreas")
        print(" 2. Consultar áreas")
        print(" 3. Modificar áreas")
        print(" 4. Eliminar áreas")
        print(" 0. Fin")
        opcion = input("    OPCIÓN ")              
        match opcion: 
            case "1":
                agregar_areas(areas)
            case "2":
                consultar_areas(areas)
            case "3":
                modificar_areas(areas)
            case "4":
                eliminar_areas(areas)  
            case "0":
                break
            case _: 
                input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
          
#########################################################################
# FUNCIÓN PRINCIPAL                                                                                                 #
#########################################################################

# constante de tipos de teléfono: índices pares tienen código, siguiente índice sus descripciones
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro") 

# inicializar estructuras
areas = [] # lista de áreas de teléfono
contactos = [] # lista con la información de cada contacto
grupos = [] # lista con los nombres de los grupos de contactos
contactos_por_grupos = [] # lista con los contactos asociados a cada grupo de contactos

# datos de configuración
area_por_omision = 0
tipo_telefono_por_omision = ""

#????????????????????
# INICIO DE BLOQUE DE INICIALIZACIÓN DE ESTRUCTURAS PARA PRUEBAS
# OJO: ESTE BLOQUE DE INICIALIZACIÓN NO PERTENECE A LA FUNCIONALIDAD DEL PROGRAMA.
# SE INICIALIZAN LAS ESTRUCTURAS USADAS PARA TENER UNA BASE DE DATOS
# PARA HACER PRUEBAS
areas = [(506, "Costa Rica"), (47, "Noruega")]
# FIN DE BLOQUE DE INICIALIZACIÓN DE ESTRUCTURAS PARA PRUEBAS
#????????????????????

# Menú principal
while True:
    os.system("cls")
    print("\n\n\n-------------------------------------------------------------------------------")
    print("                     LISTA DIGITAL DE CONTACTOS\n")
    print(" 1. Registrar áreas")
    print(" 2. Configuración de lista de contactos")
    print(" 3. Registrar contactos")
    print(" 4. Administrar grupos de contactos")
    print(" 5. Lista de contactos")
    print(" 6. Ayuda")
    print(" 7. Acerca de")
    print(" 0. Fin")
    opcion = input("    OPCIÓN ")              
    match opcion: 
        case "1":
            crud_areas(areas)
        case "2":
            pass            
        case "0":
            break
        case _: # se ejecuta cuando ninguna de las opciones anteriores se ejecutó
            input("OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
            
print("FIN DEL PROGRAMA")
            


