"""
Estacionamiento

Fernando Andrés González Robles
Carné 2024201276
IC1803 Taller de programación
Prof. William Mata
Grupo 4
"""

########################################
# Módulos ##############################
########################################

# módulo de interfaz gráfica
from tkinter import *
from tkinter import ttk
from tkinter import font

# facilita registro, validación y cálculos de tiempos
import time

# usado en validaciones
import re

########################################
# Variables principales ################
########################################

# contiene información de cada campo del parqueo
# un campo ocupado se ve así: [placa, fecha_hora_entrada, fecha_hora_salida, monto_pagado]
parqueo = []

# contiene todos los pagos hechos, adiciona información cada vez que un campo se libera
# una entrada se ve así: [placa, número_espacio, fecha_hora_entrada, fecha_hora_salida, monto_pagado]
historial_parqueo = []

# variable global de la ventana general del programa
ventana = Tk()
ventana.title("Estacionamiento")
ventana.geometry("950x600")

# variable del campo de texto
frame = ttk.Frame(ventana, padding=10)
frame.grid()

# fuente global del programa
FUENTE = font.nametofont("TkDefaultFont").name

# variables de configuración
cantidad_espacios = precio_hora = pago_mínimo = redondeo = minutos_máximos = 0
monedas = []
billetes = []

# denominaciones de moneda con sus cantidades ingresadas y egresadas
cantidades_denominaciones = [{}, {}]


########################################
# Funcionalidades base #################
########################################

""" la ventana principal del programa, con todas las opciones """
def menú_principal():
    # crear las opciones principales
    menubar = Menu(ventana)
    menubar.add_command(label="Configuración", command=configuración)

    # crear el submenú del dinero del cajero
    menubar_dinero = Menu(menubar, tearoff=0)
    menubar_dinero.add_command(label="Saldo del cajero", command=saldo_cajero)
    menubar_dinero.add_command(label="Cargar cajero")
    menubar.add_cascade(label="Dinero del cajero", menu=menubar_dinero)

    menubar.add_command(label="Entrada del vehículo")
    menubar.add_command(label="Cajero")
    menubar.add_command(label="Salida del vehículo")
    menubar.add_command(label="Reporte de ingresos de dinero")
    menubar.add_command(label="Ayuda")
    menubar.add_command(label="Acerca de", command=acerca_de)
    menubar.add_command(label="Salir", command=ventana.destroy)

    ventana.config(menu=menubar)

    # una vez configurado todo el aspecto gráfico, mostrar la ventana
    ventana.mainloop()


""" configuración del programa """
def configuración():
    # lista de entradas de texto
    entradas = []

    # función interna para validar y establecer los datos cuando todo esté correcto
    def establecer():
        global cantidad_espacios, precio_hora, pago_mínimo, redondeo, minutos_máximos, monedas, billetes, parqueo

        clear_frame(error_frame)

        # obtener datos de los valores actuales en las entradas
        datos = [x.get() for x in entradas]

        hay_errores = False
        row = 0

        # cantidad de espacios
        if not datos[0].isnumeric() or int(datos[0]) < 1:
            error(error_frame, "Cantidad de espacios debe ser un entero >= 1", row=row)
            row += 1
            hay_errores = True
        else:
            datos[0] = int(datos[0])
        
        # precio por hora
        try:
            p = float(datos[1])

            if p < 0 or datos[1][::-1].find(".") > 2:
                error(error_frame, "El precio por hora debe ser un flotante de máximo 2 decimales", row=row)
                row += 1
                hay_errores = True
            else:
                datos[1] = p
        except ValueError:
            error(error_frame, "El precio por hora debe ser un flotante de máximo 2 decimales", row=row)
            row += 1
            hay_errores = True

        # pago mínimo
        if not datos[2].isnumeric() or int(datos[2]) < 0:
            error(error_frame, "El pago mínimo debe ser un entero >= 0", row=row)
            row += 1
            hay_errores = True
        else:
            datos[2] = int(datos[2])
        
        # redondear el tiempo al próximo minuto
        if not datos[3].isnumeric() or int(datos[3]) < 0 or int(datos[3]) > 60:
            error(error_frame, "El tiempo para redondear debe ser un entero entre 0 y 60", row=row)
            row += 1
            hay_errores = True
        else:
            datos[3] = int(datos[3])

        # minutos máximos para salir 
        if not datos[4].isnumeric() or int(datos[4]) < 0:
            error(error_frame, "Minutos máximos para salir debe ser un entero >= 0", row=row)
            row += 1
            hay_errores = True
        else:
            datos[4] = int(datos[4])

        # monedas
        monedas_local = []

        try:
            monedas_local = [int(datos[5]), int(datos[6]), int(datos[7])]
        except ValueError:
            error(error_frame, "Monedas deben ser enteros", row=row)
            row += 1
            hay_errores = True
        
        hay_ceros = False
        for i, moneda in enumerate(monedas_local):
            if moneda == 0:
                hay_ceros = True
            else:
                # si hay ceros y la moneda no es 0, está mal
                if hay_ceros:
                    error(error_frame, "Si una moneda es 0, las siguientes deben serlo también", row=row)
                    row += 1
                    hay_errores = True
                    break
                else:
                    if i == 0:
                        if moneda < 0:
                            error(error_frame, "Moneda 1 debe ser >= 0", row=row)
                            row += 1
                            hay_errores = True
                            break
                    else:        
                        if moneda < monedas_local[i - 1]:
                            error(error_frame, f"Moneda {i + 1} debe ser >= 0 y mayor que la anterior", row=row)
                            row += 1
                            hay_errores = True
                            break

        billetes_local = []

        try:
            billetes_local = [int(datos[8]), int(datos[9]), int(datos[10])]
        except ValueError:
            error(error_frame, "Billetes deben ser enteros", row=row)
            row += 1
            hay_errores = True

        hay_ceros = False
        for i, billete in enumerate(billetes_local):
            if billete == 0:
                hay_ceros = True
            else:
                # si hay ceros y la moneda no es 0, está mal
                if hay_ceros:
                    error(error_frame, "Si un billete es 0, las siguientes deben serlo también", row=row)
                    row += 1
                    hay_errores = True
                    break
                else:
                    if i == 0:
                        if billete < 0:
                            error(error_frame, "Billete 1 debe ser >= 0", row=row)
                            row += 1
                            hay_errores = True
                            break
                    else:        
                        if billete < billetes_local[i - 1]:
                            error(error_frame, f"Billete {i + 1} debe ser >= 0 y mayor que la anterior", row=row)
                            row += 1
                            hay_errores = True
                            break
            
        if not hay_errores:
            cantidad_espacios = datos[0]
            precio_hora = datos[1]
            pago_mínimo = datos[2]
            redondeo = datos[3]
            minutos_máximos = datos[4]
            monedas = monedas_local
            billetes = billetes_local

            # una lista de información vacía por cada espacio del parqueo
            parqueo = [[] for i in range(cantidad_espacios)]

            for moneda in monedas:
                if moneda != 0:
                    # ingresados, egresados
                    cantidades_denominaciones[0][moneda] = [0, 0]

            for billete in billetes:
                if billete != 0:
                    cantidades_denominaciones[1][billete] = [0, 0]

            clear_frame()

    # función principal de configuración: empezar por borrar el desplegado actual
    clear_frame()
    
    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - configuración", justify="left", padding=5)
    título.grid(column=0, row=0, sticky=W)
    título.config(font=(FUENTE, 16))

    textos = [
        "Cantidad de espacios en el parqueo",
        "Precio por hora",
        "Pago mínimo",
        "Redondear el tiempo cobrado al próximo minuto",
        "Minutos máximos para salir después del pago",
        "Tipos de moneda",
        "    Moneda 1, la de menor denominación",
        "    Moneda 2, denominación siguiente a la anterior",
        "    Moneda 3, denominación siguiente a la anterior",
        "Tipos de billetes",
        "    Billete 1, el de menor denominación",
        "    Billete 2, denominación siguiente a la anterior",
        "    Billete 3, denominación siguiente a la anterior",
        "    Billete 4, denominación siguiente a la anterior",
        "    Billete 5, denominación siguiente a la anterior"
    ]

    # crear tres frames: texto y entradas, botones, errores
    entries = ttk.Frame(frame)
    entries.grid(column=0, row=1, sticky=W)

    botones = ttk.Frame(frame)
    botones.grid(column=0, row=2, sticky=W)

    error_frame = ttk.Frame(frame, padding=10)
    error_frame.grid(column=0, row=3, sticky=W)

    # poblar los textos y entradas
    for i, texto in enumerate(textos):
        label = ttk.Label(entries, text=texto)
        label.grid(sticky=W, column=0, row=i + 1, padx=10, pady=3)
        label.config(font = (FUENTE, 12))

        if i == 5 or i == 9:
            continue

        entry = ttk.Entry(entries)
        entry.grid(sticky=E, column=1, row=i + 1, padx=50)
        entradas.append(entry)

    # añadir los botones
    ttk.Button(botones, text="ok", command=establecer) \
        .grid(column=0, row=0, sticky=W, pady=10, padx=10)
    ttk.Button(botones, text="cancelar", command=clear_frame) \
        .grid(column=1, row=0, sticky=W, pady=10, padx=10)

""" despliega saldo del cajero en sus diferentes denominaciones """
def saldo_cajero():
    clear_frame()

    # crear el encabezado
    headings = ttk.Frame(frame)
    headings.grid(row=0, sticky=W)

    título = ttk.Label(headings, text="Estacionamiento - saldo del cajero", justify="left", padding=5)
    título.grid(column=0, row=0, sticky=W)
    título.config(font=(FUENTE, 16))

    contents = ttk.Frame(frame)
    contents.grid(row=1)
    # crear las secciones principales
    denominaciones = ttk.Frame(contents)
    denominaciones.grid(column=0, row=1, padx=30, pady=10)

    entradas = ttk.Frame(contents)
    entradas.grid(column=1, row=1, padx=30, pady=10)

    entradas_cantidad = ttk.Frame(entradas)
    entradas_cantidad.grid(column=0, row=1, padx=30, pady=10)

    entradas_total = ttk.Frame(entradas)
    entradas_total.grid(column=1, row=1, padx=30, pady=10)

    salidas = ttk.Frame(contents)
    salidas.grid(column=2, row=1, padx=30, pady=10)

    salidas_cantidad = ttk.Frame(salidas)
    salidas_cantidad.grid(column=0, row=1, padx=30, pady=10)

    salidas_total = ttk.Frame(salidas)
    salidas_total.grid(column=1, row=1, padx=30, pady=10)

    saldo = ttk.Frame(contents)
    saldo.grid(column=3, row=1, padx=30, pady=10)

    saldo_cantidad = ttk.Frame(saldo)
    saldo_cantidad.grid(column=0, row=1, padx=30, pady=10)

    saldo_total = ttk.Frame(saldo)
    saldo_total.grid(column=1, row=1, padx=30, pady=10)

    botones = ttk.Frame(frame)
    botones.grid(column=0, row=4)

    ttk.Label(denominaciones).grid(row=0)
    ttk.Label(denominaciones, text="Denominaciones").grid(row=1)

    ttk.Label(entradas, text="Entradas").grid(row=0)
    ttk.Label(entradas_cantidad, text="Cantidad").grid(row=0)
    ttk.Label(entradas_total, text="Total").grid(row=0)

    ttk.Label(salidas, text="Salidas").grid(row=0)
    ttk.Label(salidas_cantidad, text="Cantidad").grid(row=0)
    ttk.Label(salidas_total, text="Total").grid(row=0)

    ttk.Label(saldo, text="Saldo").grid(row=0)
    ttk.Label(saldo_cantidad, text="Cantidad").grid(row=0)
    ttk.Label(saldo_total, text="Total").grid(row=0)

    # TODO: todos los ttk -> tk

    i = 1
    cantidad_monedas, cantidad_billetes = cantidades_denominaciones

    # entrada y salida de monedas, entrada y salida de billetes
    totales = [0, 0, 0, 0]
    for denom, (ent, sal) in cantidad_monedas.items():
        ttk.Label(denominaciones, text=f"Monedas de {denom}").grid(row=i)

        ttk.Label(entradas_cantidad, text=str(ent)).grid(row=i)
        ttk.Label(entradas_total, text=str(ent * denom)).grid(row=i)

        ttk.Label(salidas_cantidad, text=str(sal)).grid(row=i)
        ttk.Label(salidas_total, text=str(sal * denom)).grid(row=i)

        ttk.Label(saldo_cantidad, text=str(ent - sal)).grid(row=i)
        ttk.Label(saldo_total, text=str((ent - sal) * denom)).grid(row=i)

        totales[0] += ent
        totales[1] += sal

        i += 1


""" despliega información sobre el programa en la ventana """
def acerca_de():
    clear_frame()

    textos = ["Administrador de estacionamiento de vehículos", "Fecha de creación: 2024/05/24",
        "Autor: Fernando González Robles", "Programa 3 - IC1803 Taller de Programación"]

    for i, texto in enumerate(textos):
        label = ttk.Label(frame, text=texto, justify="left", anchor="w")
        label.grid(sticky=W, column=0, row=i)
        label.config(font = (FUENTE, 16))


########################################
# Funciones auxiliares #################
########################################

""" borra todos los elementos de un frame existente """
def clear_frame(f=frame):
    for widget in f.winfo_children():
        widget.destroy()

""" crea un texto de error en el frame """
def error(frame, mensaje, tamaño=14, row=0, col=0):
    ttk.Label(frame, text="[Error] " + mensaje, foreground="red", font=(FUENTE, tamaño), anchor="w") \
        .grid(column=col, row=row, sticky=W)

def guardar_datos():
    # datos de configuración
    f_config = open("configuración.dat", "w")
    str_write = f"{cantidad_espacios}\n"
    str_write += f"{precio_hora}\n"
    str_write += f"{pago_mínimo}\n"
    str_write += f"{redondeo}\n"
    str_write += f"{minutos_máximos}\n"
    f_config.write()
    f_config.write()
    f_config.write()
    f_config.write()
    f_con

    # TODO: seguir

########################################
# Pruebas ##############################
########################################



########################################
# Función principal ####################
########################################
menú_principal()