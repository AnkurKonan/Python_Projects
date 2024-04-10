import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Time Table for Coders")
root.geometry("650x400")

tabControl = ttk.Notebook(root)

t1 = ttk.Frame(tabControl)
t2 = ttk.Frame(tabControl)
t3 = ttk.Frame(tabControl)
t4 = ttk.Frame(tabControl)
t5 = ttk.Frame(tabControl)
t6 = ttk.Frame(tabControl)

tabControl.add(t1, text='9:30pm-1:30am')
tabControl.add(t2, text='2:30pm-5:00pm')
tabControl.add(t3, text='5:00pm-6:00pm')
tabControl.add(t4, text='6:00pm-9:00pm')
tabControl.add(t5, text='9:30pm-2:30am')
tabControl.pack(expand=1, fill="both")

ttk.Label(t1,
          text="Attending Lectures & Enjoying College Life", font=("",20)).grid(column=0,
                     row=0,
                     padx=30,
                     pady=30)
ttk.Label(t2,
          text="Watching FreeCodeCamp Tutorials & Making Bullet Point Notes", font=("",20)).grid(column=0,
                          row=0,
                          padx=30,
                          pady=30)
ttk.Label(t3, text="Excersise & Taking Bath" ,font=("",20)).grid(column=0,
                     row=0,
                     padx=30,
                     pady=30)
ttk.Label(t4, text="Coding & Coding", font=("",20)).grid(column=0,
                     row=0,
                     padx=30,
                     pady=30)
ttk.Label(t5, text="Again Coding Till I Fall Asleep", font=("",20)).grid(column=0,
                     row=0,
                     padx=30,
                     pady=30)
root.mainloop()
