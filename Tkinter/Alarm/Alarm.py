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
        self.popmenuminutes = customtkinter.CTkOptionMenu(self, fg_color="#0598ed", width=80, dynamic_resizing=False, values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29','30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'])

        self.popmenuminutes.grid(row=0, column=1, padx=2, pady=(4,2))
        self.popmenuAMPM = customtkinter.CTkOptionMenu(self, fg_color="#0598ed", width=80, dynamic_resizing=False,
                                                        values=["AM", "PM"])
        self.popmenuAMPM.grid(row=0, column=2, padx=(2,4), pady=(4, 2))
        button = customtkinter.CTkButton(self, text="Set", fg_color="#0598ed", width=80, command=self.set)
        button.grid(row=1, column=0, padx=(4,2), pady=(2,4))
        button = customtkinter.CTkButton(self, text="Cancel", fg_color="#0598ed", width=80, command=self.cancel)
        button.grid(row=1, column=1, padx=2, pady=(2,4))
        button = customtkinter.CTkButton(self, text="Stop", fg_color="#0598ed", width=80, command=self.stop)
        button.grid(row=1, column=2, padx=(2,4), pady=(2,4))

    def set(self):
        hour = int(self.popmenuhours.get())
        minute = int(self.popmenuminutes.get())
        period = self.popmenuAMPM.get()

        if period == "PM" and hour != 12:
            hour += 12
        if period == "AM" and hour == 12:
            hour = 0

        now = datetime.datetime.now()
        self.alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if self.alarm_time < now:
            self.alarm_time = self.alarm_time.replace(day=now.day + 1)

        self.alarm_active = True
        self.alarm_thread = threading.Thread(target=self.check_alarm)
        self.alarm_thread.start()

    def cancel(self):
        self.alarm_active = False
        self.alarm_time = None

    def stop(self):
        pygame.mixer.stop()

    def check_alarm(self):
        while self.alarm_active:
            if datetime.datetime.now() >= self.alarm_time:
                music.play()
                self.alarm_active = False
            time.sleep(1)

if __name__ == "__main__":
    app = Alarm()
    app.mainloop()
