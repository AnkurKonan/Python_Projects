import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Tic Tac Toe")
        self.geometry("305x420")
        self.resizable(False, False)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(5, weight=1)

        bomb_label = customtkinter.CTkButton(self, text="X", font=("Helvetica", 60), fg_color="#f20292", height=95, width=95)
        bomb_label.grid(row=0, column=0, pady=(5, 5), padx=(5, 5))
        bomb_label = customtkinter.CTkButton(self, text="O", font=("Helvetica", 60), fg_color="#f20292", height=95, width=95)
        bomb_label.grid(row=1, column=0, pady=(0, 5), padx=(5, 5))
        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95, width=95)
        bomb_label.grid(row=2, column=0, pady=(0, 5), padx=(5, 5))

        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=0, column=1, pady=(5, 5), padx=(0, 5))
        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=1, column=1, pady=(0, 5), padx=(0, 5))
        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=2, column=1, pady=(0, 5), padx=(0, 5))

        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=0, column=2, pady=(5, 5), padx=(0, 5))
        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=1, column=2, pady=(0, 5), padx=(0, 5))
        bomb_label = customtkinter.CTkButton(self, text="", font=("Helvetica", 60), fg_color="#f20292", height=95,
                                             width=95)
        bomb_label.grid(row=2, column=2, pady=(0, 5), padx=(0, 5))

        frame1 = customtkinter.CTkFrame(self, fg_color="#1c1c1c", height=70, width=195)
        frame1.grid(row=3, column=0, pady=(0, 5), padx=(5, 5), columnspan=2)

        bomb_label = customtkinter.CTkFrame(self, fg_color="#1c1c1c", height=70,
                                            width=95)
        bomb_label.grid(row=3, column=2, pady=(0, 5), padx=(0, 5), columnspan=2)

        bomb_label = customtkinter.CTkButton(frame1, text="", font=("Helvetica", 60), fg_color="#f20292", height=35,
                                             width=295)
        bomb_label.grid(row=4, column=0, columnspan=3, pady=(0, 5), padx=(5, 5))



if __name__ == "__main__":
    app = App()
    app.mainloop()


# fg_color="#0598ed"
