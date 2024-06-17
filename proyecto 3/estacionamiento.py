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
import tkinter as tk
from tkinter import ttk
from tkinter import font

# facilita registro, validación y cálculos de tiempos
import datetime

# usado en validaciones
import re

# usado para leer y escribir archivos en binario
import pickle

########################################
# Variables principales ################
########################################

# contiene información de cada campo del parqueo
# un campo ocupado se ve así: [placa, fecha_hora_entrada, fecha_hora_salida, monto_pagado]
parqueo = []

# contiene todos los pagos hechos, adiciona información cada vez que un campo se libera
# una entrada se ve así: [placa, número_espacio, fecha_hora_entrada, fecha_hora_pago, monto_pagado, fecha_hora_salida]
historial_parqueo = []

# variable global de la ventana general del programa
ventana = tk.Tk()

# variable del campo de texto
frame = ttk.Frame(ventana)

# fuente global del programa
FUENTE = font.nametofont("TkDefaultFont").name

# formato de fecha y hora utilizado para desplegar objetos datetime
# hh:mm dd/mm/aaaa
FORMATO_HORA = "%H:%M %d/%m/%Y"

# variables de configuración
cantidad_espacios = precio_hora = pago_mínimo = redondeo = minutos_máximos = 0
monedas = []
billetes = []

# denominaciones de moneda con sus cantidades ingresadas y egresadas
cantidades_denominaciones = [{}, {}]

# versión del programa
VERSIÓN = "0.9.1"

########################################
# Funcionalidades base #################
########################################

""" la ventana principal del programa, con todas las opciones """
def menú_principal():
    # crear las opciones principales
    menubar = tk.Menu(ventana)
    menubar.add_command(label="Configuración", command=configuración)

    # crear el submenú del dinero del cajero
    menubar_dinero = tk.Menu(menubar, tearoff=0)
    menubar_dinero.add_command(label="Saldo del cajero", command=saldo_cajero)
    menubar_dinero.add_command(label="Cargar cajero", command=cargar_cajero)
    menubar.add_cascade(label="Dinero del cajero", menu=menubar_dinero)

    menubar.add_command(label="Entrada del vehículo", command=entrada_vehículo)
    menubar.add_command(label="Cajero", command=cajero)
    menubar.add_command(label="Salida del vehículo", command=salida_vehículo)
    menubar.add_command(label="Reporte de ingresos de dinero", command=reporte_ingresos)
    menubar.add_command(label="Ayuda")
    menubar.add_command(label="Acerca de", command=acerca_de)
    menubar.add_command(label="Salir", command=salir)

    ventana.config(menu=menubar)

    # crear un evento de guardar datos al cerrar la ventana con X
    ventana.wm_protocol("WM_DELETE_WINDOW", salir)

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
        primer_cero = len(monedas_local)

        for i, moneda in enumerate(monedas_local):
            if moneda == 0:
                if not hay_ceros:
                    hay_ceros = True
                    primer_cero = i
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

        monedas_local = monedas_local[:primer_cero]

        billetes_local = []

        try:
            billetes_local = [int(datos[8]), int(datos[9]), int(datos[10]), int(datos[11]), int(datos[12])]
        except ValueError:
            error(error_frame, "Billetes deben ser enteros", row=row)
            row += 1
            hay_errores = True

        hay_ceros = False
        primer_cero = len(billetes_local)
        
        for i, billete in enumerate(billetes_local):
            if billete == 0:
                if not hay_ceros:
                    hay_ceros = True
                    primer_cero = i
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
        
        billetes_local = billetes_local[:primer_cero]

        if not monto_posible(datos[1], monedas_local, billetes_local) or not monto_posible(datos[2], monedas_local, billetes_local):
            error(error_frame, f"El pago mínimo o por hora no se puede formar con estas denominaciones", row=row)
            row += 1
            hay_errores = True

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

            crear_cantidades_denominaciones()

            clear_frame()
    
    # ----------- #

    # función principal de configuración: empezar por borrar el desplegado actual
    clear_frame()
    
    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - configuración", justify="left")
    título.grid(column=0, row=0, sticky="w", padx=5, pady=5)
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
    entries.grid(column=0, row=1, sticky="w")

    botones = ttk.Frame(frame)
    botones.grid(column=0, row=2, sticky="w")

    error_frame = ttk.Frame(frame)
    error_frame.grid(column=0, row=3, sticky="w", padx=10, pady=10)

    # validar que el parqueo esté vacío
    for campo in parqueo:
        if campo:
            error(error_frame, "El parqueo debe estar vacío para configurarlo")

            ttk.Button(error_frame, text="ok", command=clear_frame) \
                .grid(column=0, row=1, sticky="w", pady=10, padx=10)

            return

    # poblar los textos y entradas
    for i, texto in enumerate(textos):
        label = ttk.Label(entries, text=texto)
        label.grid(sticky="w", column=0, row=i + 1, padx=10, pady=3)
        label.config(font = (FUENTE, 12))

        if i == 5 or i == 9:
            continue

        entry = ttk.Entry(entries)
        entry.grid(sticky=tk.E, column=1, row=i + 1, padx=50)
        entradas.append(entry)

    # añadir los botones
    ttk.Button(botones, text="ok", command=establecer) \
        .grid(column=0, row=0, sticky="w", pady=10, padx=10)
    ttk.Button(botones, text="cancelar", command=clear_frame) \
        .grid(column=1, row=0, sticky="w", pady=10, padx=10)

""" despliega saldo del cajero en sus diferentes denominaciones """
def saldo_cajero():
    vaciar = tk.BooleanVar()

    """ función interna. cuando se presiona ok, revisa el valor de la casilla de vaciar 
    y si está marcada resetea cantidades_denominaciones """
    def vaciar_o_no():
        global cantidades_denominaciones

        if vaciar.get():
            cantidades_denominaciones = [{}, {}]
            crear_cantidades_denominaciones()
        
        clear_frame()

    clear_frame()
    
    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - saldo del cajero")
    título.grid(pady=10, row=0, column=0, sticky="w")
    título.config(font=(FUENTE, 16))    

    # sección de contenidos que tiene los despliegues de datos
    contents = ttk.Frame(frame)
    contents.grid(pady=10, row=1, column=0, sticky="w")

    ttk.Label(contents, text="Denominación").grid(row=1, column=0, padx=10, sticky="w")
    ttk.Label(contents, text="Entradas").grid(row=0, column=1, columnspan=2, padx=10)
    ttk.Label(contents, text="Salidas").grid(row=0, column=3, columnspan=2, padx=10)
    ttk.Label(contents, text="Saldo").grid(row=0, column=5, columnspan=2, padx=10)

    ttk.Label(contents, text="Cantidad").grid(row=1, column=1, padx=10, sticky="w")
    ttk.Label(contents, text="Cantidad").grid(row=1, column=3, padx=10, sticky="w")
    ttk.Label(contents, text="Cantidad").grid(row=1, column=5, padx=10, sticky="w")

    ttk.Label(contents, text="Total").grid(row=1, column=2, padx=10, sticky="e")
    ttk.Label(contents, text="Total").grid(row=1, column=4, padx=10, sticky="e")
    ttk.Label(contents, text="Total").grid(row=1, column=6, padx=10, sticky="e")

    ttk.Label(contents).grid(row=2, columnspan=6)

    # botones de vaciar, ok, cancelar
    botones = ttk.Frame(frame)
    botones.grid(row=2, column=0, sticky="w")

    i = 3
    cantidad_monedas, cantidad_billetes = cantidades_denominaciones

    # entrada y salida de monedas, entrada y salida de billetes
    totales = [0] * 8
    for denom, (ent, sal) in cantidad_monedas.items():
        ttk.Label(contents, text=f"Monedas de {denom}").grid(row=i, column=0, padx=10, sticky="w")

        ttk.Label(contents, text=str(ent)).grid(row=i, column=1, padx=10)
        ttk.Label(contents, text=str(ent * denom)).grid(row=i, column=2, padx=10)

        ttk.Label(contents, text=str(sal)).grid(row=i, column=3, padx=10)
        ttk.Label(contents, text=str(sal * denom)).grid(row=i, column=4, padx=10)

        ttk.Label(contents, text=str(ent - sal)).grid(row=i, column=5, padx=10)
        ttk.Label(contents, text=str((ent - sal) * denom)).grid(row=i, column=6, padx=10)

        totales[0] += ent
        totales[1] += ent * denom
        totales[2] += sal
        totales[3] += sal * denom

        i += 1

    # totales de monedas
    ttk.Label(contents, text="Total de monedas").grid(row=i, column=0, padx=10, sticky="w")
    ttk.Label(contents, text=str(totales[0])).grid(row=i, column=1, padx=10)
    ttk.Label(contents, text=str(totales[1])).grid(row=i, column=2, padx=10)
    ttk.Label(contents, text=str(totales[2])).grid(row=i, column=3, padx=10)
    ttk.Label(contents, text=str(totales[3])).grid(row=i, column=4, padx=10)
    ttk.Label(contents, text=str(totales[0] - totales[2])).grid(row=i, column=5, padx=10)
    ttk.Label(contents, text=str(totales[1] - totales[3])).grid(row=i, column=6, padx=10)
    i += 1

    ttk.Label(contents).grid(row=i, columnspan=6)
    i += 1

    for denom, (ent, sal) in cantidad_billetes.items():
        ttk.Label(contents, text=f"Billetes de {denom}").grid(row=i, column=0, padx=10, sticky="w")

        ttk.Label(contents, text=str(ent)).grid(row=i, column=1, padx=10)
        ttk.Label(contents, text=str(ent * denom)).grid(row=i, column=2, padx=10)

        ttk.Label(contents, text=str(sal)).grid(row=i, column=3, padx=10)
        ttk.Label(contents, text=str(sal * denom)).grid(row=i, column=4, padx=10)

        ttk.Label(contents, text=str(ent - sal)).grid(row=i, column=5, padx=10)
        ttk.Label(contents, text=str((ent - sal) * denom)).grid(row=i, column=6, padx=10)

        totales[4] += ent
        totales[5] += ent * denom
        totales[6] += sal
        totales[7] += sal * denom

        i += 1

    # totales de billetes
    ttk.Label(contents, text="Total de billetes").grid(row=i, column=0, padx=10, sticky="w")
    ttk.Label(contents, text=str(totales[4])).grid(row=i, column=1, padx=10)
    ttk.Label(contents, text=str(totales[5])).grid(row=i, column=2, padx=10)
    ttk.Label(contents, text=str(totales[6])).grid(row=i, column=3, padx=10)
    ttk.Label(contents, text=str(totales[7])).grid(row=i, column=4, padx=10)
    ttk.Label(contents, text=str(totales[4] - totales[6])).grid(row=i, column=5, padx=10)
    ttk.Label(contents, text=str(totales[5] - totales[7])).grid(row=i, column=6, padx=10)

    ttk.Checkbutton(botones, text="Vaciar cajero", variable=vaciar).grid(row=0, pady=10)
    ttk.Button(botones, text="ok", command=vaciar_o_no).grid(row=1, column=0, padx=10)
    ttk.Button(botones, text="cancelar", command=clear_frame).grid(row=1, column=1, padx=10)

""" despliega saldo del cajero en sus diferentes denominaciones """
def cargar_cajero():
    clear_frame()

    # variable que detecta errores al validar entradas de carga
    errores_en = []

    clear_frame()
    
    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - cargar cajero")
    título.grid(pady=10, row=0, column=0, sticky="w")
    título.config(font=(FUENTE, 16))    

    # sección de contenidos que tiene los despliegues de datos
    contents = ttk.Frame(frame)
    contents.grid(pady=10, row=1, column=0, sticky="w")

    ttk.Label(contents, text="Denominación").grid(row=1, column=0, padx=10, sticky="w")
    ttk.Label(contents, text="Saldo antes de la carga").grid(row=0, column=1, columnspan=2, padx=10)
    ttk.Label(contents, text="Carga").grid(row=0, column=3, columnspan=2, padx=10)
    ttk.Label(contents, text="Saldo").grid(row=0, column=5, columnspan=2, padx=10)

    ttk.Label(contents, text="Cantidad").grid(row=1, column=1, padx=10)
    ttk.Label(contents, text="Cantidad").grid(row=1, column=3, padx=10, sticky="w")
    ttk.Label(contents, text="Cantidad").grid(row=1, column=5, padx=10, sticky="w")

    ttk.Label(contents, text="Total").grid(row=1, column=2, padx=10)
    ttk.Label(contents, text="Total").grid(row=1, column=4, padx=10, sticky="e")
    ttk.Label(contents, text="Total").grid(row=1, column=6, padx=10, sticky="e")

    ttk.Label(contents).grid(row=2, columnspan=6)

    # botones de ok, cancelar
    botones = ttk.Frame(frame)
    botones.grid(row=2, column=0, sticky="w")

    error_frame = ttk.Frame(frame)
    error_frame.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    i = 3
    cantidad_monedas, cantidad_billetes = cantidades_denominaciones

    # se crea un diccionario con los saldos de todas las denominaciones
    # también se creará un diccionario con cambios de la carga 
    saldos = {}
    cambios = {}

    for denom, (ent, sal) in cantidad_monedas.items():
        saldos[denom] = ent - sal

    for denom, (ent, sal) in cantidad_billetes.items():
        saldos[denom] = ent - sal

    # totales de saldo antes de la carga (cant. y tot.), para monedas y billetes
    totales = [0, 0, 0, 0]

    # labels de totales de carga (cant. y tot), labels de totales de saldo final (cant. y tot), para monedas y billetes
    totales_editar = [ttk.Label(contents, text="0"), ttk.Label(contents, text="0"), ttk.Label(contents), ttk.Label(contents),
        ttk.Label(contents, text="0"), ttk.Label(contents, text="0"), ttk.Label(contents), ttk.Label(contents)]

    """ función interna para manejar auto-refresque de los campos """
    def editar(name, index, mode, variables_extra, es_monedas):
        denom, carga, carga_total, saldo_final_cant, saldo_final_total = variables_extra

        nonlocal errores_en

        saldo = saldos[denom]
        try:
            string = carga.get()
            
            if not string:
                if denom in cambios:
                    del cambios[denom]

                if denom in errores_en:
                    errores_en.remove(denom)

                carga_total.config(text="0")
                saldo_final_cant.config(text=saldos[denom])
                saldo_final_total.config(text=saldos[denom] * denom)
            else:
                cambio = int(carga.get())
                if cambio < 0:
                    raise ValueError
                
                cambios[denom] = cambio

                if denom in errores_en:
                    errores_en.remove(denom)  
                      
                nuevo_saldo = saldo + cambios[denom]
                carga_total.config(text=str(cambios[denom] * denom))
                saldo_final_cant.config(text=str(nuevo_saldo))
                saldo_final_total.config(text=str(nuevo_saldo * denom))
            
        except ValueError:
            if denom not in errores_en:
                errores_en.append(denom)

            if denom in cambios:
                del cambios[denom]
                carga_total.config(text="-")
                saldo_final_cant.config(text="-")
                saldo_final_total.config(text="-")

        if errores_en:
            if es_monedas:
                totales_editar[0].config(text="-")
                totales_editar[1].config(text="-")
                totales_editar[2].config(text="-")
                totales_editar[3].config(text="-")
            else:
                totales_editar[4].config(text="-")
                totales_editar[5].config(text="-")
                totales_editar[6].config(text="-")
                totales_editar[7].config(text="-")
        else:
            if es_monedas:
                # obtener suma de los nuevos saldos con los que ya se tienen
                # cambios se preasume ya tener estructura {int: int}
                total_nuevas_cant = total_nuevas_tot = 0
                for denom in cambios:
                    if denom not in monedas:
                        continue

                    total_nuevas_cant += cambios[denom]
                    total_nuevas_tot += cambios[denom] * denom
                
                totales_editar[0].config(text=str(total_nuevas_cant))
                totales_editar[1].config(text=str(total_nuevas_tot))
                totales_editar[2].config(text=str(total_nuevas_cant + totales[0]))
                totales_editar[3].config(text=str(total_nuevas_tot + totales[1]))
            else:
                total_nuevas_cant = total_nuevas_tot = 0
                for denom in cambios:
                    if denom not in billetes:
                        continue

                    total_nuevas_cant += cambios[denom]
                    total_nuevas_tot += cambios[denom] * denom
                
                totales_editar[4].config(text=str(total_nuevas_cant))
                totales_editar[5].config(text=str(total_nuevas_tot))
                totales_editar[6].config(text=str(total_nuevas_cant + totales[2]))
                totales_editar[7].config(text=str(total_nuevas_tot + totales[3]))

    def establecer():
        if errores_en:
            error(error_frame, "Las cargas deben ser enteros positivos o estar vacías")
        else:
            for denom in cambios:
                if denom in monedas:
                    tipo = 0
                else:
                    tipo = 1

                cantidades_denominaciones[tipo][denom][0] += cambios[denom]
            
            clear_frame()

    # desplegar todos los datos y cajas de monedas
    for denom in monedas:
        if denom == 0:
            break

        saldo = saldos[denom]

        ttk.Label(contents, text=f"Monedas de {denom}").grid(row=i, column=0, padx=10, sticky="w")

        # saldo actual, cantidad y total
        ttk.Label(contents, text=str(saldo)).grid(row=i, column=1, padx=10)
        ttk.Label(contents, text=str(saldo * denom)).grid(row=i, column=2, padx=10)

        # entrada de carga, cantidad
        carga = tk.StringVar()
        ttk.Entry(contents, textvariable=carga, width=7).grid(row=i, column=3, padx=10)
        # y total
        carga_total = ttk.Label(contents, text="0")
        carga_total.grid(row=i, column=4, padx=10)

        # saldo final, cantidad
        saldo_final_cant = ttk.Label(contents, text=str(saldo))
        saldo_final_cant.grid(row=i, column=5, padx=10)
        # y total
        saldo_final_total = ttk.Label(contents, text=str(saldo * denom))
        saldo_final_total.grid(row=i, column=6, padx=10)

        carga.trace_add(
            "write",
            lambda n, i, m, variables_extra=(denom, carga, carga_total, saldo_final_cant, saldo_final_total), es_monedas=True: editar(n, i, m, variables_extra, es_monedas)
        )

        totales[0] += saldo
        totales[1] += saldo * denom
        i += 1

    i += 1
    # desplegar todos los totales con sus valores iniciales, luego se editarán automáticamente
    ttk.Label(contents, text="Total de monedas").grid(row=i, column=0, padx=10, sticky="w")
    ttk.Label(contents, text=str(totales[0])).grid(row=i, column=1)
    ttk.Label(contents, text=str(totales[1])).grid(row=i, column=2)
    totales_editar[0].grid(row=i, column=3)
    totales_editar[1].grid(row=i, column=4)
    totales_editar[2].config(text=str(totales[0]))
    totales_editar[2].grid(row=i, column=5)
    totales_editar[3].config(text=str(totales[1]))
    totales_editar[3].grid(row=i, column=6)

    ttk.Label(contents).grid(row=i + 1)
    i += 2

    for denom in billetes:
        if denom == 0:
            break

        saldo = saldos[denom]

        ttk.Label(contents, text=f"Billetes de {denom}").grid(row=i, column=0, padx=10, sticky="w")

        ttk.Label(contents, text=str(saldo)).grid(row=i, column=1, padx=10)
        ttk.Label(contents, text=str(saldo * denom)).grid(row=i, column=2, padx=10)

        carga = tk.StringVar()
        ttk.Entry(contents, textvariable=carga, width=7).grid(row=i, column=3, padx=10)
        
        carga_total = ttk.Label(contents, text=str(sal * denom))
        carga_total.grid(row=i, column=4, padx=10)

        saldo_final_cant = ttk.Label(contents, text=str(saldo))
        saldo_final_cant.grid(row=i, column=5, padx=10)

        saldo_final_total = ttk.Label(contents, text=str(saldo * denom))
        saldo_final_total.grid(row=i, column=6, padx=10)

        carga.trace_add(
            "write",
            lambda n, i, m, variables_extra=(denom, carga, carga_total, saldo_final_cant, saldo_final_total), es_monedas=False: editar(n, i, m, variables_extra, es_monedas)
        )

        totales[2] += saldo
        totales[3] += saldo * denom
        i += 1

    # desplegar todos los totales con sus valores iniciales, luego se editarán automáticamente
    ttk.Label(contents, text="Total de billetes").grid(row=i, column=0, padx=10, sticky="w")
    ttk.Label(contents, text=str(totales[2])).grid(row=i, column=1)
    ttk.Label(contents, text=str(totales[3])).grid(row=i, column=2)
    totales_editar[4].grid(row=i, column=3)
    totales_editar[5].grid(row=i, column=4)
    totales_editar[6].config(text=str(totales[2]))
    totales_editar[6].grid(row=i, column=5)
    totales_editar[7].config(text=str(totales[3]))
    totales_editar[7].grid(row=i, column=6)

    ttk.Button(botones, text="ok", command=establecer).grid(row=1, column=0, padx=10)
    ttk.Button(botones, text="cancelar", command=clear_frame).grid(row=1, column=1, padx=10)

""" registra la entrada de un vehículo, si el parqueo tiene campos disponibles """
def entrada_vehículo():
    clear_frame()

    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - entrada de vehículo")
    título.grid(pady=10, row=0, column=0, sticky="w")
    título.config(font=(FUENTE, 16))

    # frames principales
    contents = ttk.Frame(frame)
    contents.grid(pady=10, row=1, column=0, sticky="w")

    botones = ttk.Frame(frame)
    botones.grid(pady=10, row=2, column=0, sticky="w")

    error_frame = ttk.Frame(frame)
    error_frame.grid(pady=10, row=3, column=0, sticky="w")

    # validar que el parqueo haya sido configurado (es decir, tenga elementos, aunque sean listas vacías)
    if not parqueo:
        error(error_frame, "El parqueo debe configurarse para acceder a esta funcionalidad")

        ttk.Button(error_frame, text="ok", command=clear_frame) \
            .grid(column=0, row=1, sticky="w", pady=10, padx=10)

        return

    # la fecha y hora de hoy
    hora_entrada = datetime.datetime.today()
    índice_nuevo_vehículo = -1
    campos_ocupados = []
    placa = tk.StringVar()
    placa_entry = ttk.Entry()
    
    
    """ función interna para crear todo* (excepto botones) """
    def crear_campos():
        nonlocal placa, placa_entry, hora_entrada, índice_nuevo_vehículo, campos_ocupados
        clear_frame(contents)
        clear_frame(error_frame)

        # calcular el espacio en el que va a estar el nuevo vehículo
        índice_nuevo_vehículo = búsqueda_espaciada(parqueo)
        campos_ocupados = [campo for campo in parqueo if campo]

        # calcular la cantidad de espacios disponibles
        espacios_disponibles = len(parqueo) - len(campos_ocupados)

        # desplegar datos
        ttk.Label(contents, text="Espacios disponibles").grid(row=0, column=0, pady=10, sticky="w")

        # validar que hayan espacios
        if índice_nuevo_vehículo == -1:
            error(contents, "NO HAY ESPACIO", row=0, col=1)

            ttk.Button(error_frame, text="ok :(", command=crear_campos) \
                .grid(column=0, row=1, sticky="w", pady=10, padx=10)

            return

        # de otra manera, mostrar los demás campos
        ttk.Label(contents, text=str(espacios_disponibles)).grid(row=0, column=1, pady=10, sticky="e")

        ttk.Label(contents, text="Su placa").grid(row=1, column=0, sticky="w")

        placa_entry = ttk.Entry(contents, textvariable=placa, width=10, justify="right")
        placa_entry.delete(0, "end")
        placa_entry.grid(row=1, column=1, pady=10, sticky="e")

        ttk.Label(contents, text="Campo asignado").grid(row=2, column=0, pady=10, sticky="w")
        ttk.Label(contents, text=str(índice_nuevo_vehículo + 1), font=(FUENTE, 16)).grid(row=2, column=1, pady=10, sticky="e")

        ttk.Label(contents, text="Hora de entrada").grid(row=3, column=0, pady=10, sticky="w")
        ttk.Label(contents, text=hora_entrada.strftime(FORMATO_HORA)).grid(row=3, column=1, pady=10, sticky="e")

        ttk.Label(contents, text="Precio por hora").grid(row=4, column=0, pady=10, sticky="w")
        ttk.Label(contents, text=str(precio_hora)).grid(row=4, column=1, pady=10, sticky="e")

        ttk.Label(contents, text="Pago mínimo").grid(row=5, column=0, pady=10, sticky="w")
        ttk.Label(contents, text=str(pago_mínimo)).grid(row=5, column=1, pady=10, sticky="e")        

    """ función interna para colocar la información del nuevo vehículo en el campo respectivo """
    def parquear():
        placa_str = placa.get()

        if not placa_str or len(placa_str) > 8:
            clear_frame(error_frame)
            error(error_frame, "El campo de placa debe ser entre 1 y 8 caracteres")
            return

        for campo in campos_ocupados:
            if campo[0] == placa_str:
                clear_frame(error_frame)
                error(error_frame, f"La placa {placa_str} ya está en el parqueo")
                placa_entry.delete(0, "end")
                return

        parqueo[índice_nuevo_vehículo] = [placa_str, hora_entrada]

        # reinicia el proceso recreando los campos
        crear_campos()

    # crear botones de ok y cancelar
    crear_campos()
    ttk.Button(botones, text="ok", command=parquear).grid(row=0, column=0, sticky="w")
    ttk.Button(botones, text="cancelar", command=crear_campos).grid(row=0, column=1, padx=10, sticky="e")

""" en 3 pasos:
1. pide la placa del vehículo y muestra su monto a pagar
2. muestra botones para pagar con las denominaciones permitidas, o con tarjeta
3. muestra el cambio si el pago fue en efectivo """
def cajero():
    clear_frame()

    hora_salida = datetime.datetime.today()
    pagado = 0
    i_campo = 0

    # crear encabezado
    headings = ttk.Frame(frame)
    headings.grid(row=0)
    ttk.Label(headings, text="Cajero", font=(FUENTE, 20, "bold")).grid(row=0, column=0)
    ttk.Label(headings, text=f"{precio_hora:.2f} por hora").grid(row=0, column=1, padx=10)

    paso1 = ttk.Frame(frame)
    paso1.grid(row=1, column=0, sticky="w", pady=10)

    paso2 = ttk.Frame(frame)
    paso2.grid(row=2, column=0, sticky="w", pady=20)

    paso3 = ttk.Frame(frame)
    paso3.grid(row=3, column=0, sticky="w")

    pago_exitoso = ttk.Label(frame, text="Pago exitoso. Presione \"Finalizar\".")

    anular = ttk.Button(frame, text="anular pago")

    error_frame = ttk.Frame(frame)
    error_frame.grid(row=6, column=0, sticky="w", pady=20)

    # --- paso 1 --- #
    ttk.Label(paso1, text="Paso 1: su placa").grid(row=0, column=0, pady=20)

    placa_str = tk.StringVar()
    placa = ttk.Entry(paso1, width=10, textvariable=placa_str)
    placa.grid(row=0, column=1, padx=20, sticky="w")    
    
    # entradas de dinero que aumentan conforme se presionan los botones de monedas
    entradas_denoms = {}
    def añadir(denom, pago_cnv, pago_id, cambio_cnv, cambio_id, tarjeta_entry, pago, botones_frame):
        # args = (m, pago_cnv, pago_id, cambio_cnv, cambio_id, tarjeta_entry)
        nonlocal pagado

        tarjeta_entry.config(state="disabled")
        pagado += denom
        pago_cnv.itemconfig(pago_id, text=str(pagado))

        if denom in entradas_denoms:
            entradas_denoms[denom] += 1
        else:
            entradas_denoms[denom] = 1

        if pagado >= pago:
            for botón in botones_frame.winfo_children():
                botón.config(state="disabled")
                
            pasar_al_paso3(pago, pagado, cambio_cnv, cambio_id)

    def tarjetazo(botones_frame, tarjeta_var, tarjeta_entry, pago, pago_cnv, pago_id, cambio_cnv, cambio_id):
        for botón in botones_frame.winfo_children():
                botón.config(state="disabled")

        tarjeta = tarjeta_var.get()
        if len(tarjeta) == 10:
            tarjeta_entry.configure(state="disabled")
            pago_cnv.itemconfigure(pago_id, text=str(pago))
            cambio_cnv.itemconfigure(cambio_id, text="N/A")

            # actualizar el campo del parqueo con la fecha hora de salida y el monto cancelado
            parqueo[i_campo].append(hora_salida)
            parqueo[i_campo].append(pago)

            pago_exitoso.grid(row=4, column=0, sticky="w")
            anular.configure(text="finalizar")

    def pasar_al_paso2(*args):
        nonlocal i_campo

        placa_str_str = placa_str.get()

        campo = None
        for i, c in enumerate(parqueo):
            if c and c[0] == placa_str_str:
                campo = c
                i_campo = i
                break
        
        if campo:
            placa.config(state="disabled")

            if len(campo) > 2:
                error(error_frame, f"El vehículo con placa {placa_str_str} ya está pagado")
                anular.config(text="finalizar")
                anular.grid(row=5, column=0, sticky="w")
                return

            # obtener el tiempo redondeado y el pago correspondiente a ese tiempo
            d, h, m = redondear_tiempo(hora_salida - campo[1])
            pago = calcular_pago(d, h, m)

            ttk.Label(paso1, text="Hora de entrada").grid(row=1, column=0, sticky="w")
            ttk.Label(paso1, text=campo[1].strftime(FORMATO_HORA)).grid(row=1, column=1, padx=20, sticky="w")
            ttk.Label(paso1, text="Hora de salida").grid(row=2, column=0, sticky="w")
            ttk.Label(paso1, text=hora_salida.strftime(FORMATO_HORA)).grid(row=2, column=1, padx=20, sticky="w")
            ttk.Label(paso1, text="Tiempo cobrado").grid(row=3, column=0, sticky="w", pady=7)
            ttk.Label(paso1, text=f"{h:02}h {m:02}m          {d}d").grid(row=3, column=1, padx=20, pady=7, sticky="w")

            ttk.Label(paso1, text="A pagar").grid(row=0, column=2, padx=30)
            a_pagar = tk.Canvas(paso1, width=100, height=60, background="#DC143C")
            a_pagar.grid(row=1, column=2, rowspan=2, padx=30)
            a_pagar.create_text(50, 30, text=str(pago), anchor="center", font=(FUENTE, 16))
            
            ttk.Label(paso1, text="Pago").grid(row=1, column=3, padx=10, sticky="w")
            pago_cnv = tk.Canvas(paso1, width=100, height=30, background="#2E8B57")
            pago_cnv.grid(row=1, column=4)
            pago_id = pago_cnv.create_text(50, 15, text="xxxxxx", anchor="center", font=(FUENTE, 16))

            ttk.Label(paso1, text="Cambio").grid(row=2, column=3, padx=10, sticky="w")
            cambio_cnv = tk.Canvas(paso1, width=100, height=30, background="#2E8B57")
            cambio_cnv.grid(row=2, column=4)
            cambio_id = cambio_cnv.create_text(50, 15, text="xxxxxx", anchor="center", font=(FUENTE, 16))            

            # --- paso 2 --- #
            ttk.Label(paso2, text="Paso 2: su pago en").grid(row=0, column=0)
            ttk.Label(paso2, text="Monedas").grid(row=0, column=1, padx=20)
            ttk.Label(paso2, text="Billetes").grid(row=0, column=2, padx=50)
            ttk.Label(paso2, text="Tarjeta de crédito").grid(row=0, column=3, padx=20)

            botones_frame = ttk.Frame(paso2)
            botones_frame.grid(row=1, column=1, columnspan=2, rowspan=5, sticky="w")

            # entrada de la tarjeta
            tarjeta = tk.StringVar()
            tarjeta_entry = ttk.Entry(paso2, textvariable=tarjeta)
            tarjeta_entry.grid(row=1, column=3, padx=20)
            args = (botones_frame, tarjeta, tarjeta_entry, pago, pago_cnv, pago_id, cambio_cnv, cambio_id)
            tarjeta.trace_add("write", lambda i, n, m, args=args: tarjetazo(*args))
            

            for i, m in enumerate(monedas):
                args = (m, pago_cnv, pago_id, cambio_cnv, cambio_id, tarjeta_entry, pago, botones_frame)
                # deconstruir la tupla de argumentos en la llamada de la función, tal que
                # f(*(a, b, c)) -> f(a, b, c)
                ttk.Button(botones_frame, text=str(m), command=lambda args=args: añadir(*args), width=3).grid(row=i, column=0, padx=45)

            for i, b in enumerate(billetes):
                args = (b, pago_cnv, pago_id, cambio_cnv, cambio_id, tarjeta_entry, pago, botones_frame)
                ttk.Button(botones_frame, text=str(b), command=lambda args=args: añadir(*args)).grid(row=i, column=1, padx=50)      

            anular.grid(row=5, column=0, sticky="w")

    # --- paso 3 --- #
    def pasar_al_paso3(por_pagar, pagado, cambio_cnv, cambio_id):
        cambio = pagado - por_pagar
        cambio_cnv.itemconfigure(cambio_id, text=str(cambio))
        
        # paso 1: añadir las monedas insertadas a la máquina al registro total de denominaciones (entradas)
        for denom in entradas_denoms:
            if denom in cantidades_denominaciones[0]:
                cantidades_denominaciones[0][denom][0] += entradas_denoms[denom]
            else:
                cantidades_denominaciones[1][denom][0] += entradas_denoms[denom]


        # paso 2: obtener y desplegar el cambio
        # además, añadir la distribución de denominaciones usadas para el cambio como salidas
        distribución = monto_posible_realista(cambio, cantidades_denominaciones)

        if distribución == -1:
            error(error_frame, "No se puede dar el cambio, por favor solicite que carguen el cajero o pague con tarjeta")
        else:
            ttk.Label(paso3, text="Su cambio en:").grid(row=0, column=0)
            ttk.Label(paso3, text="Monedas").grid(row=0, column=1, padx=20)
            ttk.Label(paso3, text="Billetes").grid(row=0, column=2, padx=20)

            for i, moneda in enumerate(monedas):
                cantidad = 0
                if moneda in distribución:
                    cantidad = distribución[moneda]
                
                ttk.Label(paso3, text=f"{cantidad} de {moneda}").grid(row=i + 1, column=1, padx=20)
                cantidades_denominaciones[0][moneda][1] += cantidad
            
            for i, billete in enumerate(billetes):
                cantidad = 0
                if billete in distribución:
                    cantidad = distribución[billete]
                
                ttk.Label(paso3, text=f"{cantidad} de {billete}").grid(row=i + 1, column=2, padx=20)
                cantidades_denominaciones[1][billete][1] += cantidad
        
            pago_exitoso.grid(row=4, column=0, sticky="w")
            anular.configure(text="Finalizar")

        # paso 3: actualizar el campo del parqueo con la fecha hora de salida y el monto cancelado
        parqueo[i_campo].append(hora_salida)
        parqueo[i_campo].append(por_pagar)

    def reset():
        nonlocal hora_salida, pagado, placa
        hora_salida = datetime.datetime.today()
        pagado = 0

        clear_frame(paso1)
        clear_frame(paso2)
        clear_frame(paso3)
        clear_frame(error_frame)

        ttk.Label(paso1, text="Paso 1: su placa").grid(row=0, column=0, pady=20)
        
        placa = ttk.Entry(paso1, width=10, textvariable=placa_str)
        placa.delete(0, "end")
        placa.grid(row=0, column=1, padx=20, sticky="w")

        anular.configure(text="Anular pago")
        anular.grid_forget()
        pago_exitoso.grid_forget()


    anular.configure(command=reset)
    placa_str.trace_add("write", pasar_al_paso2)

""" desocupa el campo del vehículo que estaba en él, si es que ya pagó y salió a tiempo """
def salida_vehículo():
    clear_frame()

    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - salida de vehículo")
    título.grid(pady=10, row=0, column=0, sticky="w")
    título.config(font=(FUENTE, 16))

    contents = ttk.Frame(frame)
    contents.grid(row=1, column=0, sticky="w", pady=10)

    ttk.Label(contents, text="Su placa").grid(row=0, column=0, sticky="w")
    placa_str = tk.StringVar()
    placa = ttk.Entry(contents, textvariable=placa_str, width=10)
    placa.grid(row=0, column=1, padx=10)

    error_frame = ttk.Frame(frame)
    error_frame.grid(row=3, column=0, sticky="w")

    i_campo = 0
    tiempo_salida = 0

    def salida():
        nonlocal i_campo, tiempo_salida

        tiempo_salida = datetime.datetime.today()
        placa_str_str = placa_str.get()

        campo = None
        for i, c in enumerate(parqueo):
            if c and c[0] == placa_str_str:
                campo = c
                i_campo = i
                break
        
        if campo:
            if len(campo) < 4:
                reset()
                error(error_frame, "Debe pagar en el cajero antes de salir")
            else:
                tiempo_transcurrido = tiempo_salida - campo[2]
                tiempo_transcurrido = tiempo_transcurrido.days * 24 * 60 + tiempo_transcurrido.seconds // 60

                error_exceso = f"""No puede salir porque excedió el tiempo el tiempo permitido para ello.
Tiempo máximo para salir del parqueo: {minutos_máximos} minutos
Tiempo que usted ha tardado: {tiempo_transcurrido} minutos
Debe regresar al cajero a pagar la diferencia."""

                # si se pasó del tiempo permitido para salir, hace una nueva entrada con la fecha de pago
                reset()
                if tiempo_transcurrido > minutos_máximos:
                    error(error_frame, error_exceso)
                    pasar_a_historial(campo)
                    parqueo[i_campo] = [campo[0], campo[2]]
                else:
                    pasar_a_historial(campo)
        else:
            reset()
            error(error_frame, f"La placa {placa_str_str} no está en el parqueo")

    def reset():
        clear_frame(error_frame)
        placa.delete(0, "end")

    def pasar_a_historial(campo):
        historial_parqueo.append([campo[0], i_campo + 1, campo[1], campo[2], campo[3], tiempo_salida])
        parqueo[i_campo] = []

    botones = ttk.Frame(frame)
    botones.grid(row=2, column=0, sticky="w", pady=20)

    ttk.Button(botones, text="ok", command=salida).grid(row=2, column=0, sticky="w")
    ttk.Button(botones, text="cancelar", command=reset).grid(row=2, column=1, padx=10)

def reporte_ingresos():
    clear_frame()

    # crear el encabezado
    título = ttk.Label(frame, text="Estacionamiento - reporte de ingresos de dinero")
    título.grid(pady=10, row=0, column=0, columnspan=5, sticky="w")
    título.config(font=(FUENTE, 16))

    reporte_frame = ttk.Frame(frame)
    reporte_frame.grid(row=1, column=0, sticky="w")

    ttk.Label(reporte_frame, text="Ingresos desde el día").grid(row=0, column=0, sticky="w")
    desde = tk.StringVar()
    ttk.Entry(reporte_frame, textvariable=desde, width=10).grid(row=0, column=1, sticky="w", padx=20)

    ttk.Label(reporte_frame, text="Hasta el día").grid(row=1, column=0, sticky="w")
    hasta = tk.StringVar()
    ttk.Entry(reporte_frame, textvariable=hasta, width=10).grid(row=1, column=1, sticky="w", padx=20)

    cálculos_reporte_frame = ttk.Frame(frame)

    ttk.Label(cálculos_reporte_frame, text="Total de ingresos").grid(row=2, column=0, sticky="w", pady=20)
    total_ingresos = ttk.Label(cálculos_reporte_frame)
    total_ingresos.grid(row=2, column=1, sticky="w", padx=45)
    
    
    ttk.Label(frame, text="Para hacer una estimación de ingresos digite la fecha y hora hasta la cual ocupa la estimación:") \
        .grid(row=3, column=0, sticky="w", pady=(30, 10))

    estimación_frame = ttk.Frame(frame)
    estimación_frame.grid(row=4, column=0, sticky="w")

    ttk.Label(estimación_frame, text="Fecha para la estimación").grid(row=0, column=0, sticky="w")
    fecha_estim = tk.StringVar()
    ttk.Entry(estimación_frame, textvariable=fecha_estim, width=10).grid(row=0, column=1, columnspan=10, sticky="w", padx=20)

    ttk.Label(estimación_frame, text="Hora para la estimación").grid(row=1, column=0, sticky="w")
    hora_estim = tk.StringVar()
    minuto_estim = tk.StringVar()
    ttk.Entry(estimación_frame, textvariable=hora_estim, width=2).grid(row=1, column=1, sticky="w", padx=(20, 0))
    ttk.Label(estimación_frame, text=":").grid(row=1, column=2, sticky="w")
    ttk.Entry(estimación_frame, textvariable=minuto_estim, width=2).grid(row=1, column=3, sticky="w")

    cálculos_estimación_frame = ttk.Frame(frame)
    ttk.Label(cálculos_estimación_frame, text="Estimado de ingresos por recibir").grid(row=0, column=0, pady=20)
    total_estimación = ttk.Label(cálculos_estimación_frame)
    total_estimación.grid(row=0, column=1, padx=20)

    error_frame = ttk.Frame(frame)
    error_frame.grid(row=7, column=0, sticky="w")

    def calcular():
        # paso 1: calcular los ingresos de x a y día
        try:
            clear_frame(error_frame)
            delta = datetime.timedelta(days=1)
            fecha_inicio = datetime.datetime.strptime(desde.get(), "%d/%m/%Y")
            fecha_fin = datetime.datetime.strptime(hasta.get(), "%d/%m/%Y") + delta

            total = 0
            for campo in historial_parqueo:
                # [placa, número_espacio, fecha_hora_entrada, fecha_hora_pago, monto_pagado, fecha_hora_salida]
                if campo[3] >= fecha_inicio and campo[3] < fecha_fin:
                    total += campo[4]

            total_ingresos.config(text=str(total))
            cálculos_reporte_frame.grid(row=2, column=0, sticky="w")
            
        except ValueError:
            error(error_frame, "Debe proveer una fecha de inicio y final correcta")
            
        # paso 2: opcionalmente calcular la proyección de ingresos, suponiendo que todos los autos pagan al tiempo de la llamada
        if fecha_estim.get():
            try:
                fecha_hora = datetime.datetime.strptime(
                    f"{fecha_estim.get()} {hora_estim.get()} {minuto_estim.get()}",
                    "%d/%m/%Y %H %M"
                )

                total = 0
                for campo in parqueo:
                    # solo considerar aquellos pagos que sí estén antes de la fecha solicitada,
                    # para no incurrir en tiempos negativos
                    if campo and campo[1] <= fecha_hora:
                        # redondear_tiempo retorna un tuple que se deconstruye como los parámetros de calcular_pago
                        total += calcular_pago(*redondear_tiempo(fecha_hora - campo[1]))

                total_estimación.config(text=total)
                cálculos_estimación_frame.grid(row=5, column=0, sticky="w")
            except Exception as e:
                print(e)
                error(error_frame, "Debe proveer una fecha y hora de estimación correcta")

    botones = ttk.Frame(frame)
    botones.grid(row=6, column=0, sticky="w")
    ttk.Button(botones, text="ok", command=calcular).grid(row=2, column=0, sticky="w")
    ttk.Button(botones, text="cancelar", command=clear_frame).grid(row=2, column=1, padx=10)

""" despliega información sobre el programa en la ventana """
def acerca_de():
    clear_frame()

    textos = [
        "Administrador de estacionamiento de vehículos",
        f"Versión {VERSIÓN}",
        "Fecha de creación: 2024/05/24",
        "Autor: Fernando González Robles",
        "Programa 3 - IC1803 Taller de Programación"
    ]

    for i, texto in enumerate(textos):
        label = ttk.Label(frame, text=texto, font=(FUENTE, 16))
        label.grid(sticky="w", column=0, row=i)

def salir():
    guardar_datos()
    ventana.destroy()

########################################
# Funciones auxiliares #################
########################################

"""
borra todos los elementos de un frame existente
entrada: Frame (el frame cuyos elementos se borrarán)
"""
def clear_frame(f=frame):
    for widget in f.winfo_children():
        widget.destroy()

"""
crea un texto de error en el frame
entradas: Frame (frame donde se coloca el error), str (mensaje), int (tamaño de fuente),
    int (fila donde se coloca el error), int (columna del error)
"""
def error(frame, mensaje, tamaño=14, row=0, col=0):
    ttk.Label(frame, text="[Error] " + mensaje, foreground="red", font=(FUENTE, tamaño), anchor="w") \
        .grid(column=col, row=row, sticky="w")

""" guardar todos los datos en sus archivos respectivos al salir del programa """
def guardar_datos():
    # datos de configuración
    f_config = open("configuración.dat", "w")

    f_config.write(f"{cantidad_espacios}\n")
    f_config.write(f"{precio_hora}\n")
    f_config.write(f"{pago_mínimo}\n")
    f_config.write(f"{redondeo}\n")
    f_config.write(f"{minutos_máximos}\n")
    f_config.write(f"{monedas}\n")
    f_config.write(f"{billetes}\n")

    f_config.close()

    f_parqueo = open("parqueo.dat", "wb")
    pickle.dump(parqueo, f_parqueo)
    f_parqueo.close()

    f_historial = open("historial_parqueo.dat", "wb")
    pickle.dump(historial_parqueo, f_historial)
    f_historial.close()

    f_cajero = open("cajero.dat", "wb")
    pickle.dump(cantidades_denominaciones, f_cajero)
    f_cajero.close()

""" el tándem de guardar datos, lee los archivos guardados cuando inicia el programa """
def leer_datos():
    global cantidad_espacios, precio_hora, pago_mínimo, redondeo, minutos_máximos, \
        monedas, billetes, cantidades_denominaciones, parqueo, historial_parqueo

    try:
        f_config = open("configuración.dat", "r")

        cantidad_espacios = int(f_config.readline()[:-1])
        precio_hora = float(f_config.readline()[:-1])
        pago_mínimo = int(f_config.readline()[:-1])
        redondeo = int(f_config.readline()[:-1])
        minutos_máximos = int(f_config.readline()[:-1])
        monedas = eval(f_config.readline()[:-1])
        billetes = eval(f_config.readline()[:-1])
        f_config.close()

        f_parqueo = open("parqueo.dat", "rb")
        parqueo = pickle.load(f_parqueo)
        f_parqueo.close()

        f_historial = open("historial_parqueo.dat", "rb")
        historial_parqueo = pickle.load(f_historial)
        f_historial.close()

        f_parqueo = open("cajero.dat", "rb")
        cantidades_denominaciones = pickle.load(f_parqueo)
        f_parqueo.close()
    except:
        return


""" crea el diccionario de denominaciones asociadas a sus cantidades de entrada y salida """
def crear_cantidades_denominaciones():
    for moneda in monedas:
        if moneda != 0:
            # ingresados, egresados
            cantidades_denominaciones[0][moneda] = [0, 0]

    for billete in billetes:
        if billete != 0:
            cantidades_denominaciones[1][billete] = [0, 0]

"""
retorna el índice donde se debe colocar un nuevo elemento (o -1 si la lista está llena),
de tal manera que esta sea la más espaciada posible
se asume que la lista está compuesta de sublistas (vacías o con elementos)

entrada: list (lista para encontrar el índice)
salida: int (índice con mayor espaciamiento)
"""
def búsqueda_espaciada(lista: list) -> int:
    # encontrar los campos llenos
    i_campos_llenos = []
    for i, campo in enumerate(lista):
        if campo:
            i_campos_llenos.append(i)

    if len(i_campos_llenos) == len(lista):
        return -1

    # si el inicio o el final no están llenos, escoger esos
    if not i_campos_llenos or i_campos_llenos[0] != 0:
        return 0
    
    if i_campos_llenos[-1] != len(lista) - 1:
        return len(lista) - 1

    # si no, buscar la diferencia más grande, y calcular el medio en ese espacio
    max_diferencia = -1
    nuevo_campo = -1
    
    for j in range(1, len(i_campos_llenos)):
        dif_actual = i_campos_llenos[j] - i_campos_llenos[j - 1]

        if dif_actual > max_diferencia:
            max_diferencia = dif_actual
            nuevo_campo = (i_campos_llenos[j] - i_campos_llenos[j - 1]) // 2 + i_campos_llenos[j - 1]

    return nuevo_campo

"""
retorna si es posible generar un monto con los billetes y monedas actuales,
considerando de que exista una cantidad infinita de las denominaciones

entradas: int (monto por analizar), list (monedas), list (billetes)
"""
def monto_posible(monto: int, monedas: list, billetes: list) -> bool:
    i = 0;
    denoms = billetes + monedas
    denoms.sort(reverse=True)

    for denom in denoms:
        if monto // denom:
            monto %= denom
    
    return monto == 0

"""
retorna la distribución de denominaciones usadas para alcanzar cierto modo, con base en las
cantidades de cada denominación. si no es posible cubrirlo, se retorna un -1

entradas: int (monto), dict (cantidades de cada denominación (entrada y salida))
salidas: dict (distribución) o -1
"""
def monto_posible_realista(monto: int, cantidades_denominaciones: list) -> dict|int:
    denoms = []
    saldos = {}
    distribución = {}

    for denom, (ent, sal) in (cantidades_denominaciones[0] | cantidades_denominaciones[1]).items():
        denoms.append(denom)
        saldos[denom] = ent - sal
    
    denoms.sort(reverse=True)
    
    for denom in denoms:
        if saldos[denom] != 0:
            uso_posible = min(saldos[denom], monto // denom)
            distribución[denom] = uso_posible
            monto -= denom * uso_posible

    if monto != 0:
        return -1
    else:
        return distribución

"""
redondear el tiempo según la cantidad de minutos de redondeo especificada en la configuración 
si los minutos es menor al redondeo, se coloca todo en 0 (indicador de que se debería priorizar el pago mínimo)

entrada: datetime.timedelta (tiempo transcurrido entre dos puntos datetime.datetime)
salida: tupla (días, horas, minutos)
"""
def redondear_tiempo(tiempo: datetime.timedelta):
    segundos = tiempo.days * 86400 + tiempo.seconds
    minutos = segundos // 60

    if not redondeo or (minutos < redondeo and pago_mínimo):
        return (0, 0, 0)

    # obtener cuántos "ciclos" de redondeo caben en los minutos,
    # sumarle 1 (techo) y volver a convertir en minutos
    minutos = (minutos // redondeo + 1) * redondeo

    horas, minutos = divmod(minutos, 60)
    días, horas = divmod(horas, 24)

    return días, horas, minutos

"""
según los días, horas y minutos redondeados con redondear_tiempo, calcular el pago

entradas: int (días), int (horas), int (minutos)
salidas: int (pago total)
"""
def calcular_pago(días: int, horas: int, minutos: int) -> int:
    # según redondear tiempo, (0, 0, 0) indicaría priorizar el pago mínimo
    if not (días or horas or minutos):
        return pago_mínimo

    minutos_totales = días * 1440 + horas * 60 + minutos

    # obtener las horas, multiplicarlas por el precio por hora, y retornar un int para mantener consistencia
    return int(minutos_totales / 60 * precio_hora)


########################################
# Pruebas ##############################
########################################

########################################
# Función principal ####################
########################################
ventana.title("Estacionamiento")
ventana.geometry("950x600")
ventana.grid_columnconfigure(0, weight=1)

frame.grid(padx=10, pady=10)

leer_datos()
menú_principal()