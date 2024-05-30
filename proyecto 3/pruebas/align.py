import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("wow")

estilo_borde = ttk.Style()
estilo_borde.configure("A.TFrame", bordercolor="red", borderwidth=2, relief="solid")
estilo_borde.configure("A.TLabel", bordercolor="red", borderwidth=2, relief="solid")

frame = ttk.Frame(ventana)

frame.grid(padx=10, pady=10)

ttk.Label(frame, text="Estacionamiento - saldo del cajero").grid(pady=10, row=0, column=0, sticky="w")

contents = ttk.Frame(frame, relief="solid", borderwidth=2)
contents.grid(pady=10, row=1, column=0, sticky="w")

# contents
#   0    1    2    3    4    5    6
# 0      [ E  ]    [ Sa ]    [ So ]
# 1 [d] [C]  [T]  [C]  [T]  [C]  [T]
# 2
# 3 d1  e1   t1   s1   t1   o1   t1
# 4 d2  e2   t2   s2   t2   o2   t2
# 5 dn  en   tn   sn   tn   on   tn

ttk.Label(contents, text="Denominaciones").grid(row=1, column=0, padx=10, sticky="w")
ttk.Label(contents, text="Entradas").grid(row=0, column=1, columnspan=2, padx=10)
ttk.Label(contents, text="Salidas").grid(row=0, column=3, columnspan=2, padx=10)
ttk.Label(contents, text="Saldo").grid(row=0, column=5, columnspan=2, padx=10)

ttk.Label(contents, text="Cantidad").grid(row=1, column=1, padx=10, sticky="w")
ttk.Label(contents, text="Cantidad").grid(row=1, column=3, padx=10, sticky="w")
ttk.Label(contents, text="Cantidad").grid(row=1, column=5, padx=10, sticky="w")

ttk.Label(contents, text="Total").grid(row=1, column=2, padx=10, sticky="e")
ttk.Label(contents, text="Total").grid(row=1, column=4, padx=10, sticky="e")
ttk.Label(contents, text="Total").grid(row=1, column=6, padx=10, sticky="e")


buttons = ttk.Frame(frame)
buttons.grid(pady=10)
ttk.Button(buttons, text="oki", command=ventana.destroy).grid()

errors = ttk.Frame(frame)
errors.grid()


""" ttk.Label(salidas, text="Salidas").grid(row=0, column=0, columnspan=2)
ttk.Label(salidas_cantidad, text="Cantidad").grid(row=0)
ttk.Label(salidas_total, text="Total").grid(row=0)

ttk.Label(saldo, text="Saldo").grid(row=0, column=0, columnspan=2)
ttk.Label(saldo_cantidad, text="Cantidad").grid(row=0)
ttk.Label(saldo_total, text="Total").grid(row=0)

# Frame A
frame_a = ttk.Frame(root, padding="10")
frame_a.grid(row=0, column=0, columnspan=2, sticky="ew")
label_a = ttk.Label(frame_a, text="Saldo")
label_a.pack()

# Frame B
frame_b = ttk.Frame(root, padding="10")
frame_b.grid(row=1, column=0, sticky="nsew")
label_b = ttk.Label(frame_b, text="Cantidad", anchor="w")
label_b.pack(fill=tk.X, anchor="w")

# Frame C
frame_c = ttk.Frame(root, padding="10")
frame_c.grid(row=1, column=1, sticky="nsew")
label_c = ttk.Label(frame_c, text="Total", anchor="e")
label_c.pack(fill=tk.X, anchor="e")

# Configure grid weights to distribute space
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
"""
ventana.mainloop()