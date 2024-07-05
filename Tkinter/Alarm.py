import customtkinter
import pygame
import datetime
import time
import threading

pygame.mixer.init(42050, -16, 2, 2048)
music = pygame.mixer.Sound("sunflower-street-drumloop-85bpm-163900.wav")

class Alarm(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Alarm")
        self.geometry("255x70")
        self.grid_columnconfigure(3)
        self.grid_rowconfigure(2)
        self.resizable(False, False)
        self.popmenuhours = customtkinter.CTkOptionMenu(self, fg_color="#0598ed", width=80, dynamic_resizing=False,
                                                        values=['1','2','3','4','5','6','7','8','9','10','11','12'])
        self.popmenuhours.grid(row=0, column=0, padx=(4,2), pady=(4, 2))
        self.popmenuminutes = customtkinter.CTkOptionMenu(self, fg_color="#0598ed", width=80, dynamic_resizing=False, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'])

        self.popmenuminutes.grid(row=0, column=1, padx=2, pady=(4,2))
        self.popmenuAMPM = customtkinter.CTkOptionMenu(self, fg_color="#0598ed", width=80, dynamic_resizing=False,
                                                        values=["AM", "PM"])
        self.popmenuAMPM.grid(row=0, column=2, padx=(2,4), pady=(4, 2))
        button = customtkinter.CTkButton(self, text="Set", fg_color="#0598ed", width=80)
        button.grid(row=1, column=0, padx=(4,2), pady=(2,4))
        button = customtkinter.CTkButton(self, text="Cancel", fg_color="#0598ed", width=80)
        button.grid(row=1, column=1, padx=2, pady=(2,4))
        button = customtkinter.CTkButton(self, text="Stop", fg_color="#0598ed", width=80)
        button.grid(row=1, column=2, padx=(2,4), pady=(2,4))

if __name__ == "__main__":
    app = Alarm()
    app.mainloop()

