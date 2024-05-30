import tkinter as tk
from tkinter import ttk
import ttkthemes

root = tk.Tk()

root.style = ttkthemes.ThemedStyle()
    
for i, name in enumerate(sorted(root.style.theme_names())):
    b = ttk.Button(root, text=name, command=lambda name=name:root.style.theme_use(name))
    b.pack(fill='x')

root.mainloop()