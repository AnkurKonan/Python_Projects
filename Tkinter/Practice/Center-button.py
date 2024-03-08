from tkinter import *
root = Tk()
def click():
	label1 = Label(root, text="Button Clicked")
	label1.pack()
button = Button(root, text="Click Me", command=click)
button.pack()
root.mainloop()
