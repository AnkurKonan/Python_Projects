import customtkinter
from tkintermapview import TkinterMapView
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Explosives Management System")
app.geometry("2000x4000")
app.resizable(True, True)

entry_fields = []
switches = []

try:
    original_image = Image.open("red_dot.png")
    resized_image = original_image.resize((20, 20), Image.Resampling.LANCZOS)
    red_dot_image = ImageTk.PhotoImage(resized_image)
except Exception as e:
    print(f"Error loading image: {e}")

def show_on_output():
    for widget in output_frame.winfo_children():
        widget.destroy()

    for index, ((key_entry, type_entry), switch) in enumerate(zip(entry_fields, switches), start=1):
        key_value = key_entry.get().strip()
        type_value = type_entry.get().strip()
        if key_value or type_value:
            if switch.get() == 1:
                text = f"Bomb {index}: Key: {key_value}, Type: {type_value}, Bomb Blasted"
                color = "#ed0231"
            else:
                text = f"Bomb {index}: Key: {key_value}, Type: {type_value}, Nothing Happened"
                color = "white"
            label = customtkinter.CTkLabel(output_frame, text=text, font=("Helvetica", 15, "normal"))
            label.pack(anchor="w")
            label.configure(text_color=color)

title_label = customtkinter.CTkLabel(app, text="Explosives", font=("Helvetica", 20, "bold"))
title_label.grid(row=0, column=0, pady=(15, 10), padx=10)
key_label = customtkinter.CTkLabel(app, text="Key", font=("Helvetica", 20, "bold"))
key_label.grid(row=0, column=1, pady=(15, 10), padx=10)
type_label = customtkinter.CTkLabel(app, text="Type", font=("Helvetica", 20, "bold"))
type_label.grid(row=0, column=2, pady=(15, 10), padx=10)
switch_label = customtkinter.CTkLabel(app, text="Detonate", font=("Helvetica", 20, "bold"))
switch_label.grid(row=0, column=3, pady=(15, 10), padx=10)
map_label = customtkinter.CTkLabel(app, text="Map of Buildings", font=("Helvetica", 20, "bold"))
map_label.grid(row=0, column=4, columnspan=2, padx=10, pady=(15, 10))

for i in range(1, 13):
    bomb_label = customtkinter.CTkLabel(app, text=f"Bomb {i}", font=("Helvetica", 16))
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
password_entry = customtkinter.CTkEntry(app, width=30)
password_entry.grid(row=13, column=1, columnspan=2, pady=(0, 10), padx=10)

show_button = customtkinter.CTkButton(app, text="Show", font=("Helvetica", 15,), command=show_on_output)
show_button.grid(row=14, column=1, pady=(0, 10), padx=10)

# Map settings
map_view = TkinterMapView(app, corner_radius=10, width=850, height=500)
map_view.grid(row=1, column=4, columnspan=10, rowspan=14, padx=(10, 10), pady=(0,0))
map_view.set_position(40.7128, -74.0059)
map_view.set_marker(40.7128, -74.0059, text="New York City")
map_view.set_path([(40.7128, -74.0059), (40.7078, -74.0059)])
red_dot_position = [40.7128, -74.0059]
red_dot_marker = map_view.set_marker(red_dot_position[0], red_dot_position[1], text="", image=red_dot_image)

def update_red_dot():
    global red_dot_marker
    red_dot_marker.delete()
    red_dot_marker = map_view.set_marker(red_dot_position[0], red_dot_position[1], text="", image=red_dot_image)

def move_up():
    red_dot_position[0] += 0.0001
    update_red_dot()

def move_down():
    red_dot_position[0] -= 0.0001
    update_red_dot()

def move_left():
    red_dot_position[1] -= 0.0001
    update_red_dot()

def move_right():
    red_dot_position[1] += 0.0001
    update_red_dot()

def draw_circle():
    global red_dot_position
    x, y = map_view.get_position()
    radius = 50  # Adjust this value to change the radius
    map_view.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="red", width=2, fill="red")
    red_dot_position = [x, y]

# Adding frames for output and controls
big_box_frame2 = customtkinter.CTkFrame(app, fg_color="#131313", corner_radius=7, width=850, height=260)
big_box_frame2.grid(row=15, column=4, columnspan=10, rowspan=14, pady=(10, 10), padx=10)

output_frame = customtkinter.CTkFrame(app, fg_color="#131313", width=500, height=260, corner_radius=7)
output_frame.grid(row=15, column=0, columnspan=4, rowspan=4, padx=(0, 10), pady=15)
output_frame.pack_propagate(False)

controls_label = customtkinter.CTkLabel(app, text="Controls", width=100, height=50, corner_radius=7, font=("Helvetica", 18, "bold"))
controls_label.grid(row=15, column=5, padx=(10, 10), pady=(20, 10))
control_a = customtkinter.CTkButton(app, text="A", width=100, height=50, corner_radius=7, font=("Helvetica", 15, "normal"))
control_a.grid(row=15, column=6, padx=(10, 10), pady=(20, 10))
control_b = customtkinter.CTkButton(app, text="B", width=100, height=50, corner_radius=7, font=("Helvetica", 15, "normal"))
control_b.grid(row=15, column=7, padx=(10, 10), pady=(20, 10))
control_c = customtkinter.CTkButton(app, text="C", width=100, height=50, corner_radius=7, font=("Helvetica", 15, "normal"))
control_c.grid(row=15, column=8, padx=(10, 10), pady=(20, 10))
place_button = customtkinter.CTkButton(app, text="Place", width=100, height=50, corner_radius=7, font=("Helvetica", 15, "normal"), command=draw_circle)
place_button.grid(row=15, column=9, padx=(10, 10), pady=(20, 10))

move_label = customtkinter.CTkLabel(app, text="Move", width=100, height=50, corner_radius=7, font=("Helvetica", 18, "bold"))
move_label.grid(row=16, column=5, padx=(10, 10), pady=0)
move_left_button = customtkinter.CTkButton(app, text="\u2190", width=100, height=50, corner_radius=7, font=("Helvetica", 20, "normal"), command=move_left)
move_left_button.grid(row=16, column=6, padx=(10, 10), pady=0)
move_right_button = customtkinter.CTkButton(app, text="\u2192", width=100, height=50, corner_radius=7, font=("Helvetica", 20, "normal"), command=move_right)
move_right_button.grid(row=16, column=7, padx=(10, 10), pady=0)
move_up_button = customtkinter.CTkButton(app, text="\u2191", width=100, height=50, corner_radius=7, font=("Helvetica", 20, "normal"), command=move_up)
move_up_button.grid(row=16, column=8, padx=(10, 10), pady=0)
move_down_button = customtkinter.CTkButton(app, text="\u2193", width=100, height=50, corner_radius=7, font=("Helvetica", 20, "normal"), command=move_down)
move_down_button.grid(row=16, column=9, padx=(10, 10), pady=0)

app.mainloop()
