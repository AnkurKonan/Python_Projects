import customtkinter
from PIL import Image, ImageOps

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class SixthInterface(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid_rowconfigure(11, weight=1)

        original_image = Image.open("right_arrow.png")
        mirrored_image = ImageOps.mirror(original_image)
        self.button_image_mirrored = customtkinter.CTkImage(mirrored_image, size=(20, 20))
        self.button_image = customtkinter.CTkImage(original_image, size=(20, 20))

        self.sidebar_frame = customtkinter.CTkFrame(self, width=900, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, columnspan=3, sticky="nwe", padx=(0, 0), pady=(0, 0))
        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#f20578", height=40, width=40,
                                               image=self.button_image_mirrored, compound="right", command=self.go_back)
        self.welcome.grid(row=0, column=0, padx=(16, 10), pady=(16, 16))
        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#f20578", height=40, width=40,
                                               image=self.button_image, compound="right")
        self.welcome.grid(row=0, column=1, padx=(5, 0), pady=(16, 16))

        self.b1 = customtkinter.CTkEntry(self, width=200)
        self.b1.grid(row=1, column=0, pady=(20, 10), padx=(10,10))
        self.b1 = customtkinter.CTkEntry(self, width=200)
        self.b1.grid(row=1, column=1, pady=(20, 10), padx=(10, 10))

        radio_button_1 = customtkinter.CTkRadioButton(self, text="tons (t)", value=0)
        radio_button_1.grid(row=2, column=0, pady=10, padx=(20,10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="UK tons (t)", value=0)
        radio_button_1.grid(row=3, column=0, pady=10, padx=(20,10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="US tons (t)", value=0)
        radio_button_1.grid(row=4, column=0, pady=10, padx=(20,10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Pounds (lb)", value=0)
        radio_button_1.grid(row=5, column=0, pady=10, padx=(20,10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Ounces (oz)", value=0)
        radio_button_1.grid(row=6, column=0, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Kilogrammes (kg)", value=0)
        radio_button_1.grid(row=7, column=0, pady=10, padx=(20, 10), sticky="nw")

        radio_button_1 = customtkinter.CTkRadioButton(self, text="tons (t)", value=0)
        radio_button_1.grid(row=2, column=1, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="UK tons (t)", value=0)
        radio_button_1.grid(row=3, column=1, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="US tons (t)", value=0)
        radio_button_1.grid(row=4, column=1, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Pounds (lb)", value=0)
        radio_button_1.grid(row=5, column=1, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Ounces (oz)", value=0)
        radio_button_1.grid(row=6, column=1, pady=10, padx=(20, 10), sticky="nw")
        radio_button_1 = customtkinter.CTkRadioButton(self, text="Kilogrammes (kg)", value=0)
        radio_button_1.grid(row=7, column=1, pady=10, padx=(20, 10), sticky="nw")


    def go_back(self):
        self.parent.show_frame("Main")


