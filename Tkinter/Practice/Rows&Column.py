from tkinter import *

root = Tk()
root.geometry("800x800")

height = 5
width = 5
for i in range(height):
    for j in range(width):
        b = Entry(root, text="")
        b.grid(row=i, column=j)

root.mainloop()
