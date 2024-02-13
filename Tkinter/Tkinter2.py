from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Ankur Konan")

label1 = Label(root, text="Name:")
label2 = Label(root, text="Password:")
label1.grid(row=1, column=1, pady=10, padx=15)
label2.grid(row=2, column=1, pady=10, padx=15)
entry1 = Entry(root)
entry2 = Entry(root)
entry1.grid(row=1, column=2, pady=10)
entry2.grid(row=2, column=2, pady=10)
# pady & padx are basically padding at x & y axis
# column & rows you already know
# grid basically sets rows & column inside GUI
submit = Button(root, text="Submit")
submit.grid(column=2, row=3, pady=10)
root.mainloop()
