import customtkinter
import math
import random

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("423x468")
app.resizable(False, False)
app.title("Scientific Calculator")

cursor_visible = True
cursor_position = 0

def update_cursor():
    global cursor_visible
    cursor_visible = not cursor_visible
    current_text = output.cget("text")
    if cursor_visible:
        new_text = current_text[:cursor_position] + '|' + current_text[cursor_position:]
    else:
        new_text = current_text.replace('|', '')
    output.configure(text=new_text)
    app.after(500, update_cursor)

def move_cursor_left(event=None):
    global cursor_position
    if cursor_position > 0:
        cursor_position -= 1

def move_cursor_right(event=None):
    global cursor_position
    current_text = output.cget("text").replace('|', '')
    if cursor_position < len(current_text):
        cursor_position += 1

app.bind('<Left>', move_cursor_left)
app.bind('<Right>', move_cursor_right)

def percentage():
    current_text = output.cget("text")
    try:
        result = str(eval(current_text) / 100)
        output.configure(text=result)
    except Exception as e:
        output.configure(text="Error")

def plus_minus():
    current_text = output.cget("text")
    if current_text.startswith('-'):
        new_text = current_text[1:]
    else:
        new_text = '-' + current_text
    output.configure(text=new_text)

def bracket_left():
    current_text = output.cget("text")
    new_text = current_text + "("
    output.configure(text=new_text)

def bracket_right():
    current_text = output.cget("text")
    if current_text.startswith("sin"):
        new_text = current_text + "°)"
        output.configure(text=new_text)
    else:
        new_text = current_text + ")"
        output.configure(text=new_text)

def button_click(value):
    global cursor_position
    current_text = output.cget("text").replace('|', '')
    if value == "=":
        try:
            if "sin" in current_text or "cos" in current_text or "tan" in current_text:
                current_text = current_text.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
                current_text = current_text.replace("°", "*math.pi/180")
            if "ln" in current_text:
                current_text = current_text.replace("ln", "math.log")
            if "log" in current_text:
                current_text = current_text.replace("log", "math.log10")
            result = str(eval(current_text.replace('^', '**').replace('x', '*').replace('÷', '/')))
            output.configure(text=result)
            cursor_position = len(result)
        except Exception as e:
            output.configure(text="Error")
            cursor_position = len("Error")
    elif value == "AC":
        output.configure(text="")
        cursor_position = 0
    elif value == "rnd":
        random_number = str(random.random())
        new_text = current_text + random_number
        output.configure(text=new_text)
        cursor_position = len(new_text)
    else:
        new_text = current_text[:cursor_position] + str(value) + current_text[cursor_position:]
        output.configure(text=new_text)
        cursor_position += len(str(value))

def clear_display():
    global cursor_position
    output.configure(text="")
    cursor_position = 0

bomb_label = customtkinter.CTkButton(app, text="eˣ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=0, pady=(2, 2), padx=(4,2))
bomb_label = customtkinter.CTkButton(app, text="10ˣ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=1, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="\u2190", font=("Helvetica", 17), fg_color="#0263eb", height=72, width=55)
bomb_label.grid(row=1, column=2, pady=(2,2), padx=(2,2), rowspan=3)
bomb_label = customtkinter.CTkButton(app, text="\u2191", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=3, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="\u2192", font=("Helvetica", 17), fg_color="#0263eb", height=72, width=55)
bomb_label.grid(row=1, column=4, pady=(2,2), padx=(2,2), rowspan=3)
bomb_label = customtkinter.CTkButton(app, text="RND", font=("Helvetica", 13), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=1, column=5, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="EXP", font=("Helvetica", 13), fg_color="#0263eb",height=35, width=55)
bomb_label.grid(row=1, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="e", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('e'))
bomb_label.grid(row=3, column=0, pady=(2,2), padx=(4,2))
bomb_label = customtkinter.CTkButton(app, text="π", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('π'))
bomb_label.grid(row=3, column=1, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="\u2193", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=3, column=3, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="ln", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('ln'))
bomb_label.grid(row=3, column=5, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="log", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('log'))
bomb_label.grid(row=3, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="ʸ√x", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=0, pady=(2,2), padx=(4,2))
bomb_label = customtkinter.CTkButton(app, text="\u00b3√", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=1, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="\u00b2√", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=2, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="n!", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=4, column=3, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="sin\u207B\u00B9", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('sin\u207B\u00B9'))
bomb_label.grid(row=4, column=4, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="cos\u207B\u00B9", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('cos\u207B\u00B9'))
bomb_label.grid(row=4, column=5, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="tan\u207B\u00B9", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('tan\u207B\u00B9'))
bomb_label.grid(row=4, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="xʸ", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('xʸ'))
bomb_label.grid(row=5, column=0, pady=(2,2), padx=(4,2))
bomb_label = customtkinter.CTkButton(app, text="x\u00b3", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('x\u00b3'))
bomb_label.grid(row=5, column=1, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="x\u00b2", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('x\u00b2'))
bomb_label.grid(row=5, column=2, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="1/x", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click(''))
bomb_label.grid(row=5, column=3, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="sin", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('sin'))
bomb_label.grid(row=5, column=4, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="cos", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('cos'))
bomb_label.grid(row=5, column=5, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="tan", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: button_click('tan'))
bomb_label.grid(row=5, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="(", font=("Helvetica", 16), fg_color="#0263eb", height=35, width=55, command=lambda: bracket_left())
bomb_label.grid(row=6, column=0, pady=(2,2), padx=(4,2))
bomb_label = customtkinter.CTkButton(app, text=")", font=("Helvetica", 16), fg_color="#0263eb", height=35, width=55, command=lambda: bracket_right())
bomb_label.grid(row=6, column=1, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="AC", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: clear_display())
bomb_label.grid(row=6, column=2, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="MR", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=3, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="M-", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=4, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="M+", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55)
bomb_label.grid(row=6, column=5, pady=(2,2), padx=(2,2))
bomb_label = customtkinter.CTkButton(app, text="%", font=("Helvetica", 17), fg_color="#0263eb", height=35, width=55, command=lambda: percentage())
bomb_label.grid(row=6, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="1", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(1))
bomb_label.grid(row=7, column=0, pady=(2,2), padx=(4,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="2", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(2))
bomb_label.grid(row=7, column=2, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="3", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(3))
bomb_label.grid(row=7, column=4, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="+", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click("+"))
bomb_label.grid(row=7, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="4", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(4))
bomb_label.grid(row=8, column=0, pady=(2,2), padx=(4,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="5", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(5))
bomb_label.grid(row=8, column=2, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="6", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(6))
bomb_label.grid(row=8, column=4, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="-", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('-'))
bomb_label.grid(row=8, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="7", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(7))
bomb_label.grid(row=9, column=0 , pady=(2,2), padx=(4,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="8", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(8))
bomb_label.grid(row=9, column=2, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="9", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(9))
bomb_label.grid(row=9, column=4, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="x", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('x'))
bomb_label.grid(row=9, column=6, pady=(2,2), padx=(2,4))

bomb_label = customtkinter.CTkButton(app, text="+/-", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: plus_minus())
bomb_label.grid(row=10, column=0 , pady=(2,2), padx=(4,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="0", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click(0))
bomb_label.grid(row=10, column=2, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text=".", font=("Helvetica", 20), fg_color="#0598ed", height=35, width=115, command=lambda: button_click('.'))
bomb_label.grid(row=10, column=4, pady=(2,2), padx=(2,2), columnspan=2)
bomb_label = customtkinter.CTkButton(app, text="=", font=("Helvetica", 24), fg_color="#02c238", height=35, width=55, command=lambda: button_click('='))
bomb_label.grid(row=10, column=6, pady=(2,2), padx=(2,4))

output = customtkinter.CTkLabel(app, text="", anchor='nw', fg_color="#131313", width=415, height=100, font=("Helvetica", 20), corner_radius=7)
output.grid(row=0, column=0, columnspan=7, padx=(4, 4), pady=(7,7))

update_cursor()
app.mainloop()
