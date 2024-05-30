import tkinter as tk

root = tk.Tk()
# root.geometry("900x650")
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, width=200, height=100, highlightbackground="red", highlightthickness=2)
frame.grid(padx=10, pady=10, sticky="NWSE")
frame.columnconfigure((0, 1), weight=1)

entradas = tk.Frame(frame)
entradas.grid(row=0, column=0)
entradas.columnconfigure((0, 1), weight=1)
tk.Label(entradas, text="Entradas").grid(row=0, columnspan=2)
tk.Label(entradas, text="Cantidad").grid(row=1, column=0, ipadx=10, sticky="W")
tk.Label(entradas, text="Total").grid(row=1, column=1, ipadx=10, sticky="E")


entradas2 = tk.Frame(frame)
entradas2.grid(row=0, column=1)
entradas2.columnconfigure((0, 1), weight=1)
tk.Label(entradas2, text="Saldo").grid(row=0, columnspan=2, padx=40)
tk.Label(entradas2, text="Cantidad").grid(row=1, column=0, sticky="W")
tk.Label(entradas2, text="Total").grid(row=1, column=1, sticky="E")


menubar = tk.Menu(root)
menubar.add_command(label="algo")
root.config(menu=menubar)

root.mainloop()