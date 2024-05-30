from tkinter import *

root = Tk()

#Gridding root column-wise
root.grid_columnconfigure(0, weight = 2)
root.grid_columnconfigure(1, weight = 1)

#Gridding root row-wise
root.grid_rowconfigure(0, weight = 1)

frame_left = Frame(root, bg = "blue")
frame_right = Frame(root, bg = "green")

frame_left.grid(row = 0, column = 0, sticky = NSEW)
frame_right.grid(row = 0, column = 1, sticky = NSEW)

root.mainloop()