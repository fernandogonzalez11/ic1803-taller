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
    menubar_dinero.add_command(label="Saldo del cajero")
    menubar_dinero.add_command(label="Cargar cajero")
    menubar.add_cascade(label="Dinero del cajero")

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
    clear_frame()

    título = ttk.Label(frame, text="Estacionamiento - configuración", justify="left", anchor="w", padding=5)
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

    entradas = []

    for i, texto in enumerate(textos):
        label = ttk.Label(frame, text=texto, justify="left", anchor="w", padding=5)
        label.grid(sticky=W, column=0, row=i + 1)
        label.config(font = (FUENTE, 12))

        if i == 5 or i == 9:
            continue

        entry = ttk.Entry(frame)
        entry.grid(sticky=W, column=1, row=i + 1)
        entradas.append(entry)

    def establecer():
        global cantidad_espacios, precio_hora, pago_mínimo, redondeo, minutos_máximos, monedas, billetes

        # TODO: validaciones

        cantidad_espacios = int(entradas[0].get())
        precio_hora = int(entradas[1].get())
        pago_mínimo = int(entradas[2].get())
        redondeo = int(entradas[3].get())
        minutos_máximos = int(entradas[4].get())

        monedas.append(int(entradas[5].get()))
        if entradas[6].get():
            monedas.append(int(entradas[6].get()))
        if entradas[7].get():
            monedas.append(int(entradas[7].get()))

        billetes.append(int(entradas[8].get()))
        for i in range(9, 13):
            if entradas[i].get():
                billetes.append(int(entradas[i].get()))            

        clear_frame()

    botones = ttk.Frame(frame)
    botones.grid(column=0, row=16,  sticky=W)
    ttk.Button(botones, text="ok", command=establecer).grid(column=0, row=0, sticky=W, pady=10, padx=10)
    ttk.Button(botones, text="cancelar", command=clear_frame).grid(column=1, row=0, sticky=W, pady=10, padx=10)

    

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
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


########################################
# Pruebas ##############################
########################################



########################################
# Función principal ####################
########################################
menú_principal()