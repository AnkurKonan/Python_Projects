from tkinter import *

root = Tk()
root.title('Center button')
root.geometry("500x500")
button_1 = Button(root, text="Button 1", font=("Helvetica", 20))
button_2 = Button(root, text="Button 2", font=("Helvetica", 20))
button_1.grid(column=0, row=0)
button_2.grid(column=1, row=0)
my_button = Button(root, text="Click Me", font=("Helvetica, 20"))
my_button.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
