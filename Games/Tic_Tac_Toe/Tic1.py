import customtkinter

app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("305x425")
app.resizable(False, False)
app.grid_columnconfigure(3, weight=1)
app.grid_rowconfigure(5, weight=1)

count = 0

def change_color(button_id):
    global count

    button = eval(button_id)

    if button.cget("text") == "":
        if count % 2 == 0:
            button.configure(text="X", fg_color="#f20292")
        else:
            button.configure(text="O", fg_color="#0598ed")
        count += 1
        winner()

def winner():
    three = [
        [b1, b2, b3],
        [b4, b5, b6],
        [b7, b8, b9],
        [b1, b4, b7],
        [b2, b5, b8],
        [b3, b6, b9],
        [b1, b5, b9],
        [b3, b5, b7]
    ]

    for combination in three:
        if combination[0].cget("text") != "" and combination[0].cget("text") == combination[1].cget("text") == \
                combination[2].cget("text"):
            winner_player = combination[0].cget("text")
            if winner_player == "X":
                frame2.configure(text="Player 1 Wins!", corner_radius=5, font=("Helvetica", 20), fg_color="#f20292")
            else:
                frame2.configure(text="Player 2 Wins!", corner_radius=5,font=("Helvetica", 20), fg_color="#0598ed")
            return

def play_again():
    b1.configure(text="", fg_color="#171717", state="normal")
    b2.configure(text="", fg_color="#171717", state="normal")
    b3.configure(text="", fg_color="#171717", state="normal")
    b4.configure(text="", fg_color="#171717", state="normal")
    b5.configure(text="", fg_color="#171717", state="normal")
    b6.configure(text="", fg_color="#171717", state="normal")
    b7.configure(text="", fg_color="#171717", state="normal")
    b8.configure(text="", fg_color="#171717", state="normal")
    b9.configure(text="", fg_color="#171717", state="normal")
    frame2.configure(text="", fg_color="#171717")

b1 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b1'))
b1.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
b2 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b2'))
b2.grid(row=1, column=0, pady=(0, 5), padx=(5, 5))
b3 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b3'))
b3.grid(row=2, column=0, pady=(0, 5), padx=(5, 5))

b4 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b4'))
b4.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))
b5 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b5'))
b5.grid(row=1, column=1, pady=(0, 5), padx=(0, 5))
b6 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b6'))
b6.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))

b7 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b7'))
b7.grid(row=0, column=2, pady=(5, 5), padx=(0, 5))
b8 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b8'))
b8.grid(row=1, column=2, pady=(0, 5), padx=(0, 5))
b9 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95,
                             command=lambda: change_color('b9'))
b9.grid(row=2, column=2, pady=(0, 5), padx=(0, 5))

frame1 = customtkinter.CTkFrame(app, fg_color="#171717", height=70, width=95)
frame1.grid(row=3, column=0, pady=(0, 5), padx=(5, 5))

frame2 = customtkinter.CTkLabel(app, text="", font=("Helvetica", 20), fg_color="#171717", height=75, width=195)
frame2.grid(row=3, column=1, pady=(0, 5), padx=(0, 5), columnspan=2)

button = customtkinter.CTkButton(app, text="Play Again", font=("Helvetica", 15), fg_color="#af02d1",
                                            height=35, width=295, command=play_again)
button.grid(row=4, column=0, columnspan=3, pady=(0, 5), padx=(5, 5))

button = customtkinter.CTkButton(frame1, text="", fg_color="#f20292", height=30, width=30)
button.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
button = customtkinter.CTkButton(frame1, text="", fg_color="#0598ed", height=30, width=30)
button.grid(row=1, column=0, pady=(0, 5), padx=(5, 5))

button = customtkinter.CTkLabel(frame1, text="Player 1", height=20, width=20)
button.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))
button = customtkinter.CTkLabel(frame1, text="Player 2", height=20, width=20)
button.grid(row=1, column=1, pady=(0, 5), padx=(0, 5))

app.mainloop()

