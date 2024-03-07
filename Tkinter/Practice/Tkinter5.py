import tkinter as tk
from tkinter import *
import tkinter.font as TkFont

root = tk.Tk()
root.title("Form")
root.geometry("250x250")


font1 = TkFont.Font(family="apple", size=15, weight="bold")
font2 = TkFont.Font(family="Symbol", size=12, weight="bold")
font3 = TkFont.Font(family="apple", size=15, weight="bold")
font4 = TkFont.Font(family="arial", size=20, weight="bold")
font5 = TkFont.Font(family="Symbol", size=25, weight="bold")


l1 = Label(root, text="1st Font", font=font1, bg="red")
l1.pack()

l2 = Label(root, text="2nd Font", font=font2, fg="red")
l2.pack()

l3 = Label(root, text="3rd Font", font=font3)
l3.pack()

l4 = Label(root, text="4th Font", font=font4, fg="cyan")
l4.pack()

l5 = Label(root, text="5th Font", font=font5, fg="white", bg="black")
l5.pack()

l6 = Label(root, text="6th Font", font=("comic", 16, "bold"))
l6.pack()


root.mainloop()
