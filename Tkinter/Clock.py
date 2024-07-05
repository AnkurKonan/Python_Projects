from tkinter import *
import time

root = Tk()
root.title("Clock")
root["bg"] = "black"
root.geometry("200x100")
root.resizable(False, False)
def clock():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    my_label1.config(text=hour + ":" + minute + ":" + second)
    my_label1.after(1000, clock)

my_label1 = Label(root, text="", font=("apple", 45), fg="#ffffff", bg="black")
my_label1.pack(pady=20)
clock()
root.mainloop()
