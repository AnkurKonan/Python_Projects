from tkinter import *
from tkinter import colorchooser
root = Tk()
root.title("Color Picker")
root.geometry("200x200")
def color():
    color = colorchooser.askcolor()[1]
    label1 = Label(root, text=color).pack(pady=10)
    label2 = Label(root, text="You Picked a color", font=("Apple", 20), bg=color).pack()
button1 = Button(root, text="Pick a Color", command=color).pack()
root.mainloop()
