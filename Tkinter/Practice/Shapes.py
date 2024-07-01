# Circle
from tkinter import *
app = Tk()
app.geometry("600x400")
c= Canvas(app,width=400, height=400)
c.pack()
c.create_oval(60,60,210,210, fill="red",)
app.mainloop()

# Rectangle
from tkinter import *
app = Tk()
app.geometry("600x600")
c= Canvas(app, width=600, height=600)
c.pack()
c.create_rectangle(230, 10, 290, 60, outline="black", fill="blue", width=2)
app.mainloop()

#Oval
from tkinter import *
app = Tk()
app.geometry("600x600")
c= Canvas(app, width=600, height=600)
c.pack()
c.create_oval(110, 10, 210, 80, outline = "white", fill = "white", width = 2)
app.mainloop()

#Random shape
from tkinter import *
app = Tk()
app.geometry("600x600")
c= Canvas(app, width=600, height=600)
c.pack()
points = [150, 150, 100, 120, 240, 150,
          100, 200, 150, 100, 80, 100]

c.create_polygon(points, outline="white",
                           fill="White", width=2)
c.pack(fill=BOTH, expand=1)
app.mainloop()
