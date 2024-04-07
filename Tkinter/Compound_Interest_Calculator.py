import customtkinter
from customtkinter import CTk
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry('430x300')
app.title('Compound Interest Calculator')

title = customtkinter.CTkLabel(app, text="Compound Interest Calculator", font=("bold", 15))
title.grid(row=0, column=0, pady=(0, 20), padx=20)

principal_amount = customtkinter.CTkLabel(app, text="Principal amount:")
principal_amount.grid(row=1, column=0, sticky="w", pady=(0, 10), padx=20)
principal_amount = customtkinter.CTkEntry(app)
principal_amount.grid(row=1, column=1, pady=(0, 10))

Tenure = customtkinter.CTkLabel(app, text="Tenure:")
Tenure.grid(row=2, column=0, sticky="w", pady=(0, 10), padx=20)
Tenure = customtkinter.CTkEntry(app)
Tenure.grid(row=2, column=1, pady=(0, 10), padx=10)

Rate = customtkinter.CTkLabel(app, text="Rate of Interest:")
Rate.grid(row=3, column=0, sticky="w", pady= (0,10), padx=20)
Rate = customtkinter.CTkEntry(app)
Rate.grid(row=3, column=1, pady=(0, 10), padx=10)

Apply_changes = customtkinter.CTkCheckBox(app, text="Apply_changes")
Apply_changes.grid(row=4, column=1, pady=(0, 10))

Calculate = customtkinter.CTkButton(app, text="Calculate", command=lambda:calculate())
Calculate.grid(row=5, column=1, pady=(0, 20), padx=20, sticky="e")

output = customtkinter.CTkTextbox(app, width=340, height=30)
output.grid(row=6, column=0, columnspan=5, padx=5, pady=5)

def calculate():

    print("Calculate button is pressed")

app.mainloop()
