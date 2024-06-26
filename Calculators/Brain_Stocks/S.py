import customtkinter
from PIL import Image, ImageOps
from S2 import SecondInterface
from S3 import ThirdInterface
from S4 import FourthInterface
from S5 import FifthInterface
from S6 import SixthInterface

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Brain Stocks")
        self.geometry("1100x580")
        self.resizable(False, False)

        self.frames = {}
        self.frames["Main"] = customtkinter.CTkFrame(self)
        self.frames["Second"] = SecondInterface(self)
        self.frames["Third"] = ThirdInterface(self)
        self.frames["Fourth"] = FourthInterface(self)
        self.frames["Fifth"] = FifthInterface(self)
        self.frames["Sixth"] = SixthInterface(self)
        self.frames["Main"].pack(fill="both", expand=True)
        self.frames["Main"].grid_columnconfigure(6, weight=1)
        self.frames["Main"].grid_rowconfigure(6, weight=1)

        self.create_main_interface()

    def create_main_interface(self):
        original_image = Image.open("right_arrow.png")
        mirrored_image = ImageOps.mirror(original_image)
        self.button_image_mirrored = customtkinter.CTkImage(mirrored_image, size=(20, 20))
        self.button_image = customtkinter.CTkImage(original_image, size=(20, 20))

        self.sidebar_frame = customtkinter.CTkFrame(self.frames["Main"], width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsw", padx=(0, 10), pady=(0, 0))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40,
                                               image=self.button_image_mirrored, compound="right")
        self.welcome.grid(row=0, column=0, padx=(15, 10), pady=(20, 10))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40,
                                               image=self.button_image, compound="right")
        self.welcome.grid(row=0, column=1, padx=(5, 15), pady=(20, 10))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, width=95, anchor="sw",
                                                                       fg_color="#0598ed",
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.apperance)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=10, pady=(10, 10), columnspan=2)

        self.welcome_label = customtkinter.CTkLabel(self.frames["Main"], text="Welcome to Brain Stocks",
                                                    font=("Helvetica", 45))
        self.welcome_label.grid(row=0, column=2, padx=(20, 20), pady=(20, 10), columnspan=3)

        self.subtitle_label = customtkinter.CTkLabel(self.frames["Main"], text="All Tools & Calculators in one place",
                                                     font=("Helvetica", 25))
        self.subtitle_label.grid(row=1, column=2, padx=(10, 10), pady=(0, 50), columnspan=3)

        self.stocks_button = customtkinter.CTkButton(self.frames["Main"], text="Stocks &\n Bonds",
                                                     font=("Helvetica", 18), width=150, height=100, fg_color="#0598ed",
                                                     command=lambda: self.show_frame("Second"))
        self.stocks_button.grid(row=4, column=1, padx=(20, 20), pady=(20, 20))

        self.mortgage_button = customtkinter.CTkButton(self.frames["Main"], text="Mortgage\n Loans",
                                                       font=("Helvetica", 18), width=150, height=100,
                                                       fg_color="#0598ed", command=lambda: self.show_frame("Fourth"))
        self.mortgage_button.grid(row=4, column=2, padx=(20, 20), pady=(20, 20))

        self.business_button = customtkinter.CTkButton(self.frames["Main"], text="Business\n Accounting",
                                                       font=("Helvetica", 18), width=150, height=100,
                                                       fg_color="#0598ed", command=lambda: self.show_frame("Third"))
        self.business_button.grid(row=4, column=3, padx=(20, 20), pady=(20, 20))

        self.investments_button = customtkinter.CTkButton(self.frames["Main"], text="Investments\n Real estate",
                                                          font=("Helvetica", 18), width=150, height=100,
                                                          fg_color="#0598ed", command=lambda: self.show_frame("Fifth"))
        self.investments_button.grid(row=4, column=4, padx=(20, 20), pady=(20, 20))

        self.other_button = customtkinter.CTkButton(self.frames["Main"], text="Other", font=("Helvetica", 18),
                                                    width=150, height=100, fg_color="#0598ed", command=lambda: self.show_frame("Sixth"))
        self.other_button.grid(row=4, column=5, padx=(20, 20), pady=(20, 20))

    def apperance(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
