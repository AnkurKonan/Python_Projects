import customtkinter
from PIL import Image, ImageOps
from area import SecondInterface
from length import ThirdInterface
from Temp import FourthInterface
from volume import FifthInterface
from mass import SixthInterface
from data import SeventhInterface
from time1 import EigthInterface
from power import NinthInterface
from energy import TenthInterface
from speed import EleventhInterface
from pressure import TewelthInterface
from angle import ThirteenInterface
from Force import SixteenInterface
from base import SeventeenInterface

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Unit_Convertor")
        self.geometry("450x522")
        self.resizable(False, False)

        self.frames = {}
        self.frames["Main"] = customtkinter.CTkFrame(self)
        self.frames["Second"] = SecondInterface(self)
        self.frames["Third"] = ThirdInterface(self)
        self.frames["Fourth"] = FourthInterface(self)
        self.frames["Fifth"] = FifthInterface(self)
        self.frames["Sixth"] = SixthInterface(self)
        self.frames["Seventh"] = SeventhInterface(self)
        self.frames["Eigth"] = EigthInterface(self)
        self.frames["Ninth"] = NinthInterface(self)
        self.frames["Tenth"] = TenthInterface(self)
        self.frames["Eleventh"] = EleventhInterface(self)
        self.frames["Tewelth"] = TewelthInterface(self)
        self.frames["Thirteen"] = ThirteenInterface(self)
        self.frames["Sixteen"] = SixteenInterface(self)
        self.frames["Seventeen"] = SeventeenInterface(self)
        self.frames["Main"].pack(fill="both", expand=True)
        self.frames["Main"].grid_columnconfigure(2, weight=1)
        self.frames["Main"].grid_rowconfigure(10, weight=1)

        self.create_main_interface()

    def create_main_interface(self):
        original_image = Image.open("right_arrow.png")
        mirrored_image = ImageOps.mirror(original_image)
        self.button_image_mirrored = customtkinter.CTkImage(mirrored_image, size=(20, 20))
        self.button_image = customtkinter.CTkImage(original_image, size=(20, 20))

        self.sidebar_frame = customtkinter.CTkFrame(self.frames["Main"], width=900, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, columnspan=3, sticky="nwe", padx=(0, 0), pady=(0, 0))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#f20578", height=40, width=40,
                                               image=self.button_image_mirrored, compound="right")
        self.welcome.grid(row=0, column=0, padx=(16, 10), pady=(16, 16))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#f20578", height=40, width=40,
                                               image=self.button_image, compound="right")
        self.welcome.grid(row=0, column=1, padx=(5, 0), pady=(16, 16))

        # self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, width=95, anchor="sw",
        #                                                                fg_color="#f20578",
        #                                                                values=["Light", "Dark", "System"],
        #                                                                command=self.apperance)
        # self.appearance_mode_optionemenu.grid(row=11, column=0, padx=10, pady=(10, 10), columnspan=2)

        self.welcome_label = customtkinter.CTkLabel(self.frames["Main"], text="Welcome to Unit Convertor",
                                                    font=("Helvetica", 34))
        self.welcome_label.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), columnspan=2)

        self.subtitle_label = customtkinter.CTkLabel(self.frames["Main"], text="All Tools & conversions in one place",
                                                     font=("Helvetica", 19))
        self.subtitle_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), columnspan=2)

        self.stocks_button = customtkinter.CTkButton(self.frames["Main"], text="Area",
                                                     font=("Helvetica", 16), width=200, height=30, fg_color="#f20578",
                                                     command=lambda: self.show_frame("Second"))
        self.stocks_button.grid(row=4, column=0, padx=(10, 10), pady=(10, 10))

        self.mortgage_button = customtkinter.CTkButton(self.frames["Main"], text="Length",
                                                       font=("Helvetica", 16), width=200, height=30,
                                                       fg_color="#f20578", command=lambda: self.show_frame("Third"))
        self.mortgage_button.grid(row=5, column=0, padx=(10, 10), pady=(10, 10))

        self.business_button = customtkinter.CTkButton(self.frames["Main"], text="Temperature", font=("Helvetica", 16), width=200, height=30, fg_color="#f20578", command=lambda: self.show_frame("Fourth"))
        self.business_button.grid(row=6, column=0, padx=(10, 10), pady=(10, 10))

        self.investments_button = customtkinter.CTkButton(self.frames["Main"], text="Volume", font=("Helvetica", 16), width=200, height=30, fg_color="#f20578", command=lambda: self.show_frame("Fifth"))
        self.investments_button.grid(row=7, column=0, padx=(10, 10), pady=(10, 10))

        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Mass", font=("Helvetica", 16), width=200, height=30, fg_color="#f20578", command=lambda: self.show_frame("Sixth"))
        self.other_button.grid(row=8, column=0, padx=(10, 10), pady=(10, 10))
        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Angle", font=("Helvetica", 16), width=200,
                                                    height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Thirteen"))
        self.other_button.grid(row=9, column=0, padx=(10, 10), pady=(10, 10))
        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Force", font=("Helvetica", 16),
                                                    width=200,
                                                    height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Sixteen"))
        self.other_button.grid(row=10, column=0, padx=(10, 10), pady=(10, 10))


        self.business_button = customtkinter.CTkButton(self.frames["Main"], text="Data",
                                                       font=("Helvetica", 16), width=200, height=30, fg_color="#f20578",
                                                       command=lambda: self.show_frame("Seventh"))
        self.business_button.grid(row=4, column=1, padx=(0, 10), pady=(10, 10))

        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Speed", font=("Helvetica", 16),
                                                    width=200, height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Eleventh"))
        self.other_button.grid(row=5, column=1, padx=(0, 10), pady=(10, 10))

        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Time", font=("Helvetica", 16),
                                                    width=200, height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Eigth"))
        self.other_button.grid(row=6, column=1, padx=(0, 10), pady=(10, 10))
        self.business_button = customtkinter.CTkButton(self.frames["Main"], text="Energy",
                                                       font=("Helvetica", 16), width=200, height=30, fg_color="#f20578",
                                                       command=lambda: self.show_frame("Tenth"))
        self.business_button.grid(row=7, column=1, padx=(0, 10), pady=(10, 10))

        self.investments_button = customtkinter.CTkButton(self.frames["Main"], text="Power",
                                                          font=("Helvetica", 16), width=200, height=30,
                                                          fg_color="#f20578", command=lambda: self.show_frame("Ninth"))
        self.investments_button.grid(row=8, column=1, padx=(0, 10), pady=(10, 10))
        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Pressure", font=("Helvetica", 16),
                                                    width=200,
                                                    height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Tewelth"))
        self.other_button.grid(row=9, column=1, padx=(0, 10), pady=(10, 10))
        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Base", font=("Helvetica", 16),
                                                    width=200,
                                                    height=30, fg_color="#f20578",
                                                    command=lambda: self.show_frame("Seventeen"))
        self.other_button.grid(row=10, column=1, padx=(0, 10), pady=(10, 10))

    def apperance(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
