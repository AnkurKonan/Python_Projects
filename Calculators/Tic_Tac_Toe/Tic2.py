import customtkinter
# #f120292

app = customtkinter.CTk()
app.title("Tic Tac Toe")
app.geometry("305x425")
app.resizable(False, False)
app.grid_columnconfigure(3, weight=1)
app.grid_rowconfigure(5, weight=1)

def change_color(value):
    if value == "b1":
        b1.configure(fg_color="#f20292", text="X", font=("Helvetica", 60))
    elif value == "b2":
        b2.configure(fg_color="#f20292", text="X", font=("Helvetica", 60))
    elif value == "b3":
        b3.configure(fg_color="#f20292", text="X", font=("Helvetica", 60))
def play_again():
    b1.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b2.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b3.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b4.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b5.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b6.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b7.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b8.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    b9.configure(text="", font=("Helvetica", 60), fg_color="#171717")
    frame2.configure(text="", font=("Helvetica", 60), fg_color="#171717")

b1 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95, command=lambda: change_color('b1'))
b1.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
b2 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95, command=lambda: change_color('b2'))
b2.grid(row=1, column=0, pady=(0, 5), padx=(5, 5))
b3 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95, width=95, command=lambda: change_color('b3'))
b3.grid(row=2, column=0, pady=(0, 5), padx=(5, 5))

b4 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b4.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))
b5 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b5.grid(row=1, column=1, pady=(0, 5), padx=(0, 5))
b6 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b6.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))

b7 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b7.grid(row=0, column=2, pady=(5, 5), padx=(0, 5))
b8 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b8.grid(row=1, column=2, pady=(0, 5), padx=(0, 5))
b9 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=95,
                                             width=95)
b9.grid(row=2, column=2, pady=(0, 5), padx=(0, 5))

frame1 = customtkinter.CTkFrame(app, fg_color="#171717", height=70, width=95)
frame1.grid(row=3, column=0, pady=(0, 5), padx=(5, 5))

frame2 = customtkinter.CTkFrame(app, fg_color="#171717", height=75, width=195)
frame2.grid(row=3, column=1, pady=(0, 5), padx=(0, 5), columnspan=2)

bomb_label = customtkinter.CTkButton(app, text="Play Again", font=("Helvetica", 15), fg_color="#af02d1", height=35, width=295, command=lambda: play_again())
bomb_label.grid(row=4, column=0, columnspan=3, pady=(0, 5), padx=(5, 5))

bomb_label = customtkinter.CTkButton(frame1, text="", fg_color="#f20292", height=30,
                                             width=30)
bomb_label.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
bomb_label = customtkinter.CTkButton(frame1, text="", fg_color="#0598ed", height=30,
                                             width=30)
bomb_label.grid(row=1, column=0, pady=(0, 5), padx=(5, 5))

bomb_label = customtkinter.CTkLabel(frame1, text="Player 1", height=20, width=20)
bomb_label.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))
bomb_label = customtkinter.CTkLabel(frame1, text="Player 2", height=20, width=20)
bomb_label.grid(row=1, column=1, pady=(0, 5), padx=(0, 5))

app.mainloop()

# fg_color="#0598ed"
#02d402 green
