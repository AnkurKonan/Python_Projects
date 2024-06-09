import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Explosives Management")
app.geometry("2000x4000")
app.resizable(True, True)

entry_fields = []
switches = []

def show_on_output():
    output_text = []
    for index, ((key_entry, type_entry), switch) in enumerate(zip(entry_fields, switches), start=1):
        key_value = key_entry.get().strip()
        type_value = type_entry.get().strip()
        if key_value or type_value:
            output_text.append(f"Bomb-{index}: Key={key_value}, Type={type_value}")
    output.configure(text="\n".join(output_text))

title_label = customtkinter.CTkLabel(app, text="Explosives", font=("Helvetica", 20, "bold"))
title_label.grid(row=0, column=0, pady=(15, 10), padx=10)
key_label = customtkinter.CTkLabel(app, text="Key", font=("Helvetica", 20, "bold"))
key_label.grid(row=0, column=1, pady=(15, 10), padx=10)
type_label = customtkinter.CTkLabel(app, text="Type", font=("Helvetica", 20, "bold"))
type_label.grid(row=0, column=2, pady=(15, 10), padx=10)
switch_label = customtkinter.CTkLabel(app, text="Detonate", font=("Helvetica", 20, "bold"))
switch_label.grid(row=0, column=3, pady=(15, 10), padx=10)

for i in range(1, 13):
    bomb_label = customtkinter.CTkLabel(app, text=f"Bomb-{i}", font=("Helvetica", 16))
    bomb_label.grid(row=i, column=0, sticky="w", pady=(0, 10), padx=20)
    key_entry = customtkinter.CTkEntry(app)
    key_entry.grid(row=i, column=1, pady=(0, 10), padx=10)
    type_entry = customtkinter.CTkEntry(app)
    type_entry.grid(row=i, column=2, pady=(0, 10), padx=10)
    bomb_switch = customtkinter.CTkSwitch(app, text="")
    bomb_switch.grid(row=i, column=3, pady=(0, 10), padx=10)
    entry_fields.append((key_entry, type_entry))
    switches.append(bomb_switch)

password_label = customtkinter.CTkLabel(app, text="Password", font=("Helvetica", 20, "bold"))
password_label.grid(row=13, column=0, pady=(15, 10), padx=10)
password_entry = customtkinter.CTkEntry(app)
password_entry.grid(row=13, column=1, pady=(0, 10), padx=10)

show_button = customtkinter.CTkButton(app, text="Show", command=show_on_output)
show_button.grid(row=14, column=1, pady=(0, 10), padx=10)

big_box_frame = customtkinter.CTkFrame(app, fg_color="white", corner_radius=7)
big_box_frame.grid(row=1, column=4, rowspan=14, sticky="nsew", padx=(10, 20), pady=20)
app.grid_columnconfigure(4, weight=1)
app.grid_rowconfigure(14, weight=1)

big_box_frame2 = customtkinter.CTkFrame(app, fg_color="white", corner_radius=7)
big_box_frame2.grid(row=15, column=4, rowspan=14, sticky="nsew", padx=(10, 20), pady=20)
app.grid_columnconfigure(4, weight=1)
app.grid_rowconfigure(14, weight=1)

map_label = customtkinter.CTkLabel(app, text="Map of buildings", font=("Helvetica", 20,"bold"))
map_label.grid(row=0, column=4, sticky="w", pady=(15, 10), padx=10)

output = customtkinter.CTkLabel(app, text="", fg_color="#131313", width=500, height=260, corner_radius=7)
output.grid(row=15, column=0, columnspan=4, padx=(0, 8), pady=15)

app.mainloop()
