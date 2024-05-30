from tkinter import *
from tkinter import ttk

root = Tk()
root.title("holi")

def donothing():
    pass

def leng(self):
    print(self.get())
    return len(self) < 20

#root.register(leng)

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
frame.register(leng)
h = ttk.Label(frame, text="Hello World")
h.grid(column=0, row=0, padx=10)

ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)


def hacer():
    for i in range(4):
        var = StringVar()
        e = ttk.Entry(frame, textvariable=var)

        def cambio(name, index, mode, var=var):
            try:
                int(var.get())
            except ValueError:
                h.config(text="kys")

        e.grid()
        var.trace_add("write", cambio)

ttk.Button(frame, text="hacer", command=hacer).grid(column=2, row=0)

root.config(menu=menubar)

root.mainloop()