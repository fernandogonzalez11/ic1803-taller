from tkinter import *
from tkinter import ttk

root = Tk()
root.title("holi")

def donothing():
    pass

# File menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

# Extra button
menubar.add_command(label="Extra", command=donothing)

# Main
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World").grid(column=0, row=0, padx=10)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

root.config(menu=menubar)

root.mainloop()