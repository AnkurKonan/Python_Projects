import customtkinter
import math

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry('460x300')
app.title('Compound Interest Calculator')
app.resizable(False,False)

def compound():
    a = float(principal_amount.get()) * float(math.pow((1 + float(Rate.get())/100), float(Tenure.get())))
    output.configure(text=str(a))

title = customtkinter.CTkLabel(app, text="Compound Interest Calculator", font=("bold", 20))
title.grid(row=0, column=0, pady=(15,10),  padx=10)

principal_amount = customtkinter.CTkLabel(app, text="Principal amount:", font=("bold", 15))
principal_amount.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=20)
principal_amount = customtkinter.CTkEntry(app)
principal_amount.grid(row=1, column=1, pady=(0, 10), padx=10)

Tenure = customtkinter.CTkLabel(app, text="Tenure:", font=("bold", 15))
Tenure.grid(row=2, column=0, sticky="w", pady=(0, 10), padx=20)
Tenure = customtkinter.CTkEntry(app)
Tenure.grid(row=2, column=1, pady=(0, 10), padx=10)

Rate = customtkinter.CTkLabel(app, text="Rate of Interest:",font=("bold", 15))
Rate.grid(row=3, column=0, sticky="w", pady= (0,10), padx=20)
Rate = customtkinter.CTkEntry(app)
Rate.grid(row=3, column=1, pady=(0, 10), padx=10)

# Apply_changes = customtkinter.CTkCheckBox(app, text="Apply_changes")
# Apply_changes.grid(row=4, column=1, pady=(0, 10))

Calculate = customtkinter.CTkButton(app, text="Calculate", command=compound)
Calculate.grid(row=5, column=1, pady=(0, 20), padx=20, sticky="e")

output = customtkinter.CTkLabel(app, text="", bg_color="#131313", width=340, height=30)
output.grid(row=6, column=0, columnspan=5, padx=5, pady=5)

app.mainloop()
