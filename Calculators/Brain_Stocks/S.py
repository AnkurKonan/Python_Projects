import customtkinter
from PIL import Image, ImageOps
from S2 import SecondInterface

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Brain Stocks")
        self.geometry("1100x580")
        self.resizable(False, False)
        self.grid_columnconfigure(6, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.frames = {}
        self.frames["App"] = self
        self.frames["SecondInterface"] = SecondInterface(self)
        self.current_frame = "App"
        self.show_frame(self.current_frame)

        original_image = Image.open("right_arrow.png")
        mirrored_image = ImageOps.mirror(original_image)
        self.button_image_mirrored = customtkinter.CTkImage(mirrored_image, size=(20, 20))
        self.button_image = customtkinter.CTkImage(Image.open("right_arrow.png"), size=(20, 20))
        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=7, sticky="nsew", padx=(0, 10), pady=(0, 0))
        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40, image=self.button_image_mirrored, compound="right", command=lambda: self.show_frame("App"))
        self.welcome.grid(row=0, column=0, padx=(15, 10), pady=(20, 10))
        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40, image=self.button_image, compound="right", command=lambda: self.show_frame("SecondInterface"))
        self.welcome.grid(row=0, column=1, padx=(5, 15), pady=(20, 10))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, width=95, anchor="sw",
                                                                      fg_color="#0598ed",
                                                                      values=["Light", "Dark", "System"],
                                                                      command=self.apperance)
        self.appearance_mode_optionemenu.grid(row=11, column=0, padx=10, pady=(10, 10), columnspan=2)
        self.welcome = customtkinter.CTkLabel(self, text="Welcome to Brain Stocks", font=("Helvetica", 45))
        self.welcome.grid(row=0, column=2, padx=(20, 20), pady=(20, 10), columnspan=3)
        self.welcome = customtkinter.CTkLabel(self, text="All Tools & Calculators in one place", font=("Helvetica", 25))
        self.welcome.grid(row=1, column=2, padx=(10, 10), pady=(0, 50), columnspan=3)

        self.welcome = customtkinter.CTkButton(self, text="Stocks &\n Bonds", font=("Helvetica",18), width=150, height=100, fg_color="#0598ed")
        self.welcome.grid(row=4, column=1, padx=(20, 20), pady=(20, 20))
        self.welcome = customtkinter.CTkButton(self, text="Mortgage\n Loans", font=("Helvetica",18), width=150, height=100, fg_color="#0598ed")
        self.welcome.grid(row=4, column=2, padx=(20, 20), pady=(20, 20))
        self.welcome = customtkinter.CTkButton(self, text="Business\n Accounting", font=("Helvetica", 18), width=150, height=100, fg_color="#0598ed")
        self.welcome.grid(row=4, column=3, padx=(20, 20), pady=(20, 20))
        self.welcome = customtkinter.CTkButton(self, text="Investments\n Real estate", font=("Helvetica", 18), width=150, height=100, fg_color="#0598ed")
        self.welcome.grid(row=4, column=4, padx=(20, 20), pady=(20, 20))
        self.welcome = customtkinter.CTkButton(self, text="Business\n Accounting", font=("Helvetica", 18), width=150,height=100, fg_color="#0598ed")
        self.welcome.grid(row=4, column=5, padx=(20, 20), pady=(20, 20))

    def show_frame(self, frame_name):
        for frame in self.frames.values():
            frame.grid_remove()
        self.frames[frame_name].grid(row=0, column=1, rowspan=7, columnspan=5, sticky="nsew")
        self.current_frame = frame_name

    def apperance(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
