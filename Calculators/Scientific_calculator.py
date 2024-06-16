import customtkinter

customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("470x525")
app.resizable(False, False)
app.title("Scientific Calculator")

def button_click(value):
    current_text = output.cget("text")
    if value == "=":
        try:
            result = str(eval(current_text.replace('x', '*').replace('÷', '/')))
            output.configure(text=result)
        except Exception as e:
            output.configure(text="Error")
    elif value == "AC":
        output.configure(text="")
    else:
        new_text = current_text + str(value)
        output.configure(text=new_text)

def clear_display():
    output.configure(text="")

bomb_label = customtkinter.CTkButton(app, text="Shift", font=("Helvetica", 14), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=0, pady=(2, 2), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="Alpha", font=("Helvetica", 14), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=1, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="\u2190", font=("Helvetica", 17), fg_color="#0263eb", height=80, width=55)
bomb_label.grid(row=1, column=2, pady=(4, 4), padx=(4,4), rowspan=3)
bomb_label = customtkinter.CTkButton(app, text="\u2191", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=3, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="\u2192", font=("Helvetica", 17), fg_color="#0263eb", height=80, width=55)
bomb_label.grid(row=1, column=4, pady=(4, 4), padx=(4,4), rowspan=3)
bomb_label = customtkinter.CTkButton(app, text="Setup", font=("Helvetica", 13), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=5, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="ON", font=("Helvetica", 13), fg_color="#0263eb",height=35, width=55)
bomb_label.grid(row=1, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="ABS", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=0, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="xʸ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=1, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="\u2193", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=3, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="x⁻¹", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=5, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="log", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="\u00b3\u221A", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=0, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="\u221A", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=1, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="x\u00b2", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=2, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="log", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=3, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="ln", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=4, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="eˣ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=5, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="10ˣ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="x/y", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=0, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="n!", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=1, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="hyp", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=2, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="sin", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=3, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="cos", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=4, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="tan", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=5, column=5, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="AC", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: clear_display())
bomb_label.grid(row=5, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="RCL", font=("Helvetica", 16), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=0, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="ENG", font=("Helvetica", 16), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=1, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="(", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=2, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text=")", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=3, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="S<->D", font=("Helvetica", 13), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=4, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="M+", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=5, pady=(4, 4), padx=(4,4))
bomb_label = customtkinter.CTkButton(app, text="%", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="1", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(1))
bomb_label.grid(row=7, column=0, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="2", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(2))
bomb_label.grid(row=7, column=2, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="3", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(3))
bomb_label.grid(row=7, column=4, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="+", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click("+"))
bomb_label.grid(row=7, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="4", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(4))
bomb_label.grid(row=8, column=0, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="5", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(5))
bomb_label.grid(row=8, column=2, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="6", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(6))
bomb_label.grid(row=8, column=4, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="-", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('-'))
bomb_label.grid(row=8, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="7", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(7))
bomb_label.grid(row=9, column=0 , pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="8", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(8))
bomb_label.grid(row=9, column=2, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="9", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(9))
bomb_label.grid(row=9, column=4, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="x", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('x'))
bomb_label.grid(row=9, column=6, pady=(4, 4), padx=(4,4))

bomb_label = customtkinter.CTkButton(app, text="+/-", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120)
bomb_label.grid(row=10, column=0 , pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="0", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click(0))
bomb_label.grid(row=10, column=2, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text=".", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=120, command=lambda: button_click('.'))
bomb_label.grid(row=10, column=4, pady=(4, 4), padx=(4,4), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="=", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('='))
bomb_label.grid(row=10, column=6, pady=(4, 4), padx=(4,4))

output = customtkinter.CTkLabel(app, text="", anchor='nw', fg_color="#131313", width=450, height=100, font=("Helvetica", 20), corner_radius=7)
output.grid(row=0, column=0, columnspan=7, padx=(10, 10), pady=15)

app.mainloop()
