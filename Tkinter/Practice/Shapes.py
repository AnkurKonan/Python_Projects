# circle
from tkinter import *
app = Tk()
app.geometry("600x400")
c= Canvas(app,width=400, height=400)
c.pack()
c.create_oval(60,60,210,210, fill="red",)
app.mainloop()
