from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Resize GUI with Sizegrip')
root.geometry("400x300")
root["bg"] = "violet"
root.resizable(True, True)
my_frame1 = Frame(root, highlightbackground="green", highlightthickness=6)
my_frame1.pack(pady=20)
my_frame2 = Frame(root, highlightbackground="blue", highlightthickness=6)
my_frame2.pack(side="bottom", fill=X)

my_label = Label(my_frame1, text="Hello World!",font=("Apple", 32))
my_label.pack(pady=50, padx=20)

my_sizegrip = ttk.Sizegrip(my_frame1)
my_sizegrip.pack(side="right", anchor=SE)

my_sizegrip2 = ttk.Sizegrip(my_frame2)
my_sizegrip2.pack(side="right", anchor=SE)

root.mainloop()
