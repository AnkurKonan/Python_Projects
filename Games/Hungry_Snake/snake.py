import customtkinter
import random

def grids(canvas, width, height, cellsize):
    for i in range(0, width, cellsize):
        for j in range(0, height, cellsize):
            canvas.createrectangle(i, j, i + cellsize, j + cellsize, fill="#1c1c1c", outline="#000000")

def makerandomcellred(canvas, width, height, cellsize):
    randomx = random.randint(0, (width // cellsize) - 1) * cellsize
    randomy = random.randint(0, (height // cellsize) - 1) * cellsize
    canvas.createrectangle(randomx, randomy, randomx + cellsize, randomy + cellsize, fill="red", outline="#000000")

def drawsnake(canvas, startx, starty, cellsize):
    snakelength = 3
    for i in range(snakelength):
        x = startx + i * cellsize
        y = starty
        canvas.createrectangle(x, y, x + cellsize, y + cellsize, fill="#05ed28", outline="#000000")

app = customtkinter.CTk()
app.title("Hungry Snake")
app.geometry("520x620")
app.resizable(False, False)

canvas = customtkinter.CTkCanvas(app, width=520, height=520)
canvas.pack()

grids(canvas, 520, 520, 12)
makerandomcellred(canvas, 520, 520, 12)
drawsnake(canvas, 520, 520, 12)
startx = random.randint(0, (520 // 12) - 3) * 12
starty = random.randint(0, (520 // 12) - 1) * 12
drawsnake(canvas, startx, starty, 12)

frame1 = customtkinter.CTkFrame(app, width=200, height=100)
frame1.pack(padx=(4, 2), pady=(1,1), side="left")
frame1.grid_rowconfigure(2, weight=2)
frame1.grid_columnconfigure(3, weight=2)
frame1.pack_propagate(False)

frame2 = customtkinter.CTkFrame(app, width=100, height=100)
frame2.pack(padx=(2, 2), pady=(1,1), side="left")
frame2.grid_rowconfigure(2, weight=2)
frame2.grid_columnconfigure(3, weight=2)
frame2.pack_propagate(False)

frame3 = customtkinter.CTkFrame(app, width=100, height=100)
frame3.pack(padx=(2, 2), pady=(1,1), side="left")
frame3.grid_rowconfigure(2, weight=2)
frame2.grid_columnconfigure(2, weight=2)
frame3.pack_propagate(False)

b1 = customtkinter.CTkButton(frame1, text="\u2191", font=("Helvetica", 16), fg_color="#1c1c1c", height=38, width=40)
b1.grid(row=0, column=1, padx=4, pady=(1,2))
b1 = customtkinter.CTkButton(frame1, text="\u2190", font=("Helvetica", 16), fg_color="#1c1c1c", height=83, width=40)
b1.grid(row=0, column=0, padx=2, pady=1, rowspan=2)
b1 = customtkinter.CTkButton(frame1, text="\u2193", font=("Helvetica", 16), fg_color="#1c1c1c", height=38, width=40)
b1.grid(row=1, column=1, padx=2, pady=(2,1))
b1 = customtkinter.CTkButton(frame1, text="\u2192", font=("Helvetica", 16), fg_color="#1c1c1c", height=83, width=40)
b1.grid(row=0, column=2, rowspan=2, padx=2, pady=1)

b1 = customtkinter.CTkButton(frame2, text="Play \nAgain", font=("Helvetica", 17), fg_color="#1c1c1c", height=83, width=80)
b1.grid(row=0, column=0, padx=0, pady=1)

b1 = customtkinter.CTkLabel(frame3, corner_radius=5, text="Current score", font=("Helvetica", 15),  height=38, width=100)
b1.grid(row=0, column=0, padx=2, pady=(1,2))
b1 = customtkinter.CTkLabel(frame3, corner_radius=5, text="", font=("Helvetica", 15), bg_color="#131313", height=35, width=200)
b1.grid(row=0, column=1, padx=4, pady=(1,2))
b1 = customtkinter.CTkLabel(frame3, corner_radius=5, text="High score", font=("Helvetica", 15), height=37, width=100)
b1.grid(row=1, column=0, padx=2, pady=(3,1))
b1 = customtkinter.CTkLabel(frame3, corner_radius=5, text="", font=("Helvetica", 15), bg_color="#131313", height=38, width=200)
b1.grid(row=1, column=1, padx=4, pady=(3,1))

app.mainloop()


