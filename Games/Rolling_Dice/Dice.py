import customtkinter
import random

app = customtkinter.CTk()
app.title("Dice")
app.geometry("200, 250")
app.resizable(False, False)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(2, weight=1)

b1 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=105, width=105)
b1.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
b2 = customtkinter.CTkButton(app, text="", font=("Helvetica", 60), fg_color="#171717", height=105, width=105)
b2.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))

b2 = customtkinter.CTkButton(app, text="Roll the Dice", font=("Helvetica", 20), fg_color="#171717", height=50, width=215)
b2.grid(row=1, column=0, columnspan=2, pady=(0, 5), padx=(5, 5))

app.mainloop()
