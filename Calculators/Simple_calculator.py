import customtkinter

# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("320x445")
app.title("Calculator")
app.resizable(False, False)

def bracket():
    current_text = output.cget("text")
    if not current_text or current_text[-1] in "+-x÷(":
        new_text = current_text + "("
    else:
        new_text = current_text + ")"
    output.configure(text=new_text)

def button_click(value):
    current_text = output.cget("text")
    if value == "=":
        try:
            result = str(eval(current_text.replace('x', '*').replace('÷', '/')))
            output.configure(text=result)
        except Exception as e:
            output.configure(text="Error")
    elif value == "C":
        output.configure(text="")
    else:
        new_text = current_text + str(value)
        output.configure(text=new_text)

def clear_display():
    output.configure(text="")

bomb_label = customtkinter.CTkButton(app, text="C", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: clear_display())
bomb_label.grid(row=1, column=0, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="()", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60)
bomb_label.grid(row=1, column=1, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="%", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60)
bomb_label.grid(row=1, column=2, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="÷", font=("Helvetica", 25), fg_color="#02c238", height=60, width=60)
bomb_label.grid(row=1, column=3, pady=(0, 8), padx=(2,2))

bomb_label = customtkinter.CTkButton(app, text="1", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(1))
bomb_label.grid(row=2, column=0 , pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="2", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(2))
bomb_label.grid(row=2, column=1, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="3", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(3))
bomb_label.grid(row=2, column=2, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="+", font=("Helvetica", 25), fg_color="#02c238", height=60, width=60, command=lambda: button_click('+'))
bomb_label.grid(row=2, column=3, pady=(0, 8), padx=(2,2))

bomb_label = customtkinter.CTkButton(app, text="4", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(4))
bomb_label.grid(row=3, column=0 , pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="5", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(5))
bomb_label.grid(row=3, column=1, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="6", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(6))
bomb_label.grid(row=3, column=2, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="-", font=("Helvetica", 25), fg_color="#02c238", height=60, width=60, command=lambda: button_click('-'))
bomb_label.grid(row=3, column=3, pady=(0, 8), padx=(2,2))

bomb_label = customtkinter.CTkButton(app, text="7", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(7))
bomb_label.grid(row=4, column=0 , pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="8", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(8))
bomb_label.grid(row=4, column=1, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="9", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(9))
bomb_label.grid(row=4, column=2, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="x", font=("Helvetica", 25), fg_color="#02c238", height=60, width=60, command=lambda: button_click('x'))
bomb_label.grid(row=4, column=3, pady=(0, 8), padx=(2,2))

bomb_label = customtkinter.CTkButton(app, text="+/-", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60)
bomb_label.grid(row=5, column=0 , pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="0", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click(0))
bomb_label.grid(row=5, column=1, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text=".", font=("Helvetica", 25), fg_color="#0598ed", height=60, width=60, command=lambda: button_click('.'))
bomb_label.grid(row=5, column=2, pady=(0, 8), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="=", font=("Helvetica", 25), fg_color="#02c238", height=60, width=60, command=lambda: button_click('='))
bomb_label.grid(row=5, column=3, pady=(0, 8), padx=(2,2))

output = customtkinter.CTkLabel(app, text="", anchor='nw', font=("Helvetica", 25), fg_color="#131313", width=300, height=70, corner_radius=7)
output.grid(row=0, column=0, columnspan=4, padx=(10, 10), pady=15)
app.mainloop()
