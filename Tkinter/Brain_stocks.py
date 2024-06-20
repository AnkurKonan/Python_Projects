import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Brain Stocks")
        self.geometry("1100x600")
        self.resizable(False, False)
        self.grid_rowconfigure(10, weight=1)

        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew", padx=(0,10), pady=(0,0))

        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="", fg_color="#0598ed", height=40, width=40)
        self.welcome.grid(row=0, column=0, padx=(15, 10), pady=(20,10))
        self.welcome = customtkinter.CTkButton(self.sidebar_frame, text="",fg_color="#0598ed", height=40, width= 40)
        self.welcome.grid(row=0, column=1, padx=(5, 15), pady=(20,10))

        self.welcome = customtkinter.CTkLabel(self, text="Choose what you want to calculate", font=("Helvetica", 20))
        self.welcome.grid(row=0, column=1, padx=(10, 10), columnspan=3)

        self.main_frame = customtkinter.CTkFrame(self, width=420, height=460)
        self.main_frame.grid(row=1, column=4, padx=(20, 0), pady=(0, 10), rowspan=9)
        self.main_frame.grid_rowconfigure(9)
        self.frames = {}
        self.create_frames()

        self.welcome = customtkinter.CTkLabel(self, text="Choose what you want to calculate", font=("Helvetica", 20))
        self.welcome.grid(row=0, column=1, padx=(10, 10), pady=(10, 0), columnspan=3)
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15), command=lambda: self.show_frame("Simple Interest"))
        self.welcome.grid(row=1, column=1, padx=(10, 10))
        self.show_frame("Simple Interest")
        self.welcome = customtkinter.CTkButton(self, text="Compound Interest", fg_color="#0598ed", font=("Helvetica", 15), command=lambda: self.show_frame("Compound Interest"))
        self.welcome.grid(row=2, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Profitability", fg_color="#0598ed", font=("Helvetica", 15), command=lambda: self.show_frame("Profitability"))
        self.welcome.grid(row=3, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=4, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=5, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=6, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=7, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=8, column=1, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=9, column=1, padx=(10, 10))

        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=1, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=2, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=3, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=4, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=5, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=6, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=7, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=8, column=2, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=9, column=2, padx=(10, 10))

        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=1, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=2, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=3, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=4, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=5, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=6, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=7, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=8, column=3, padx=(10, 10))
        self.welcome = customtkinter.CTkButton(self, text="Simple Interest", fg_color="#0598ed", font=("Helvetica", 15))
        self.welcome.grid(row=9, column=3, padx=(10, 10))
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Save changes", font=("Helvetica", 15))
        self.checkbox_1.grid(row=10, column=1, pady=(20, 0), padx=20, sticky="n")

        def create_frames(self):
            simple_interest_frame = customtkinter.CTkFrame(self.main_frame)
            self.frames["Simple Interest"] = simple_interest_frame

            self.principal_amount = customtkinter.CTkLabel(simple_interest_frame, text="Principal amount:", font=("bold", 15))
            self.principal_amount.grid(row=1, column=0, sticky="w", pady=(10, 10), padx=20)
            self.principal_amount = customtkinter.CTkEntry(self.main_frame)
            self.principal_amount.grid(row=1, column=1, pady=(10, 10), padx=10)

            self.monthly = customtkinter.CTkLabel(simple_interest_frame, text="Monthly SIP", font=("bold", 15))
            self.monthly.grid(row=2, column=0, sticky="w", pady=(0, 10), padx=20)
            self.monthly = customtkinter.CTkEntry(self.main_frame)
            self.monthly.grid(row=2, column=1, pady=(0, 10), padx=10)

            self.Tenure = customtkinter.CTkLabel(self.main_frame, text="Tenure:", font=("bold", 15))
            self.Tenure.grid(row=3, column=0, sticky="w", pady=(0, 10), padx=20)
            self.Tenure = customtkinter.CTkEntry(self.main_frame)
            self.Tenure.grid(row=3, column=1, pady=(0, 10), padx=10)

            self.Rate = customtkinter.CTkLabel(self.main_frame, text="Rate of Interest:", font=("bold", 15))
            self.Rate.grid(row=4, column=0, sticky="w", pady=(0, 10), padx=20)
            self.Rate = customtkinter.CTkEntry(self.main_frame)
            self.Rate.grid(row=4, column=1, pady=(0, 10), padx=10)

            self.Calculate = customtkinter.CTkButton(self.main_frame, text="Calculate")
            self.Calculate.grid(row=5, column=1, pady=(0, 10), padx=10)

            self.output = customtkinter.CTkLabel(self.main_frame, text="", bg_color="#131313", width=340, height=30)
            self.output.grid(row=10, column=0, columnspan=5, padx=(30,20), pady=(10,20))

            self.slider = customtkinter.CTkLabel(self.main_frame, text="Principal amount:", font=("bold", 15))
            self.slider.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="w")
            self.slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=1, number_of_steps=10000000, fg_color="#0598ed")
            self.slider.grid(row=6, column=1, padx=20, pady=(10, 10), sticky="we")
            self.slider.set(0)

            self.slider = customtkinter.CTkLabel(self.main_frame, text="Monthly amount:", font=("bold", 15))
            self.slider.grid(row=7, column=0, padx=20, pady=(10, 10), sticky="w")
            self.slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=1, number_of_steps=10000000, fg_color="#0598ed")
            self.slider.grid(row=7, column=1, padx=20, pady=(10, 10), sticky="we")
            self.slider.set(0)

            self.slider = customtkinter.CTkLabel(self.main_frame, text="Tenure:", font=("bold", 15))
            self.slider.grid(row=8, column=0, padx=20, pady=(10, 10), sticky="w")
            self.slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=1, number_of_steps=100, fg_color="#0598ed")
            self.slider.grid(row=8, column=1, padx=20, pady=(10, 10), sticky="we")
            self.slider.set(0)

            self.slider = customtkinter.CTkLabel(self.main_frame, text="Rate of Interest:", font=("bold", 15))
            self.slider.grid(row=9, column=0, padx=20, pady=(10, 10), sticky="w")
            self.slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=1, number_of_steps=100, fg_color="#0598ed")
            self.slider.grid(row=9, column=1, padx=20, pady=(10, 10), sticky="we")
            self.slider.set(0)

        def show_frame(self, frame_name):
            frame = self.frames[frame_name]
            frame.grid(row=0, column=0, sticky="nsew")

            for other_frame in self.frames.values():
                if other_frame != frame:
                    other_frame.grid_remove()

if __name__ == "__main__":
    app = App()
    app.mainloop()
