from tkinter import *
import time
from random import *
import threading

root = Tk()
root.title("Randome&Time")
root.geometry("500x400")
root["bg"] = "yellow"

def seven_seconds():
	time.sleep(5)
	my_label.config(text="7 Seconds Is Up!")

def rando():
	random_label.config(text=f'Random Number: {randint(1,100)}')

my_label = Label(root, text="You have only 7 seconds")
my_label.pack(pady=20)

my_button1 = Button(root, text="7 Seconds", command=threading.Thread(target=seven_seconds).start())
my_button1.pack(pady=20)

my_button2 = Button(root, text="Pick Random Number", font=("Apple", 25), command=rando)
my_button2.pack(pady=20)

random_label = Label(root, text='')
random_label.pack(pady=20)

threading.Thread(target=seven_seconds).start()
root.mainloop()
