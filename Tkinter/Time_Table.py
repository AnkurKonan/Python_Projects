import customtkinter
import random

customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Time Table")
        self.geometry("800x400")
        self.resizable(False, False)
        self.rowconfigure(9, weight=1)
        self.columnconfigure(9, weight=1)

        self.main_frame = customtkinter.CTkFrame(self, fg_color="white")
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_columnconfigure(10)
        self.main_frame2 = customtkinter.CTkFrame(self.main_frame, fg_color="white", width=700)
        self.main_frame2.grid(row=1, padx=0, pady=0, columnspan=9)
        self.Tabview = customtkinter.CTkTabview(self.main_frame, height=300, fg_color="white", width=700)
        self.Tabview.grid(row=2, padx=0, pady=0, columnspan=9)
        self.Tabview.add("Day")
        self.Tabview.add("Night")
        self.Tabview.tab("Day").grid_columnconfigure(25)
        self.Tabview.tab("Night").grid_columnconfigure(25)
        self.Task = customtkinter.CTkLabel(self.main_frame, text="Task:", font=("Helvetica", 16))
        self.Task.grid(row=0, column=0, padx=(5, 0), pady=(10, 10))
        self.Task1 = customtkinter.CTkEntry(self.main_frame, width=200)
        self.Task1.grid(row=0, column=1, padx=(0, 5), pady=(10, 10))
        self.welcome = customtkinter.CTkLabel(self.main_frame, text="From:", font=("Helvetica", 16))
        self.welcome.grid(row=0, column=2, padx=(0, 0))
        self.From = customtkinter.CTkEntry(self.main_frame, width=100)
        self.From.grid(row=0, column=3, padx=(0, 5), pady=(10, 10))
        self.welcome = customtkinter.CTkLabel(self.main_frame, text="To:", font=("Helvetica", 16))
        self.welcome.grid(row=0, column=4, padx=(0, 0))
        self.To = customtkinter.CTkEntry(self.main_frame, width=100)
        self.To.grid(row=0, column=5, padx=(0, 5), pady=(10, 10))
        self.welcome = customtkinter.CTkButton(self.main_frame, text="Add", command=self.add, width=40, font=("Helvetica", 16))
        self.welcome.grid(row=0, column=6, padx=(0, 5))
        self.radio_buttons = customtkinter.CTkCheckBox(self.main_frame, text="Night")
        self.radio_buttons.grid(row=0, column=7, pady=10, padx=(10, 0), sticky="nw")
        self.radio_buttons = customtkinter.CTkCheckBox(self.main_frame, text="Day")
        self.radio_buttons.grid(row=0, column=8, pady=10, padx=(0, 0), sticky="nw")

        self.radio_buttons = {}
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "All"]
        for i, day in enumerate(days):
            self.radio_buttons[day] = customtkinter.CTkCheckBox(self.main_frame2, text=day)
            self.radio_buttons[day].grid(row=1, column=i, pady=10, padx=(0, 0), sticky="nw")
            if i == 0:
                self.radio_buttons[day] = customtkinter.CTkCheckBox(self.main_frame2, text=day)
                self.radio_buttons[day].grid(row=1, column=0, pady=10, padx=(10, 0), sticky="nw")

        time_labels = ["1:00PM", "2:00PM", "3:00PM", "4:00PM", "5:00PM", "6:00PM", "7:00PM", "8:00PM", "9:00PM", "10:00PM",  "11:00PM",  "12:00PM"]
        for i, time in enumerate(time_labels):
            customtkinter.CTkLabel(self.Tabview.tab("Day"), text=time, font=("Helvetica", 13)).grid(row=0, column=i + 1, padx=(0, 12))

        for i, day in enumerate(days):
            customtkinter.CTkLabel(self.Tabview.tab("Day"), text=day, font=("Helvetica", 16)).grid(row=i + 1, column=0, padx=(5, 5), pady=(0, 0), sticky="w")

        for i, time in enumerate(time_labels):
            customtkinter.CTkLabel(self.Tabview.tab("Night"), text=time, font=("Helvetica", 13)).grid(row=0, column=i + 1, padx=(0, 12))

        for i, day in enumerate(days):
            customtkinter.CTkLabel(self.Tabview.tab("Night"), text=day, font=("Helvetica", 16)).grid(row=i + 1, column=0, padx=(5, 5), pady=(0, 0), sticky="w")

    def add(self):
        task_name = self.Task1.get()
        start_time = self.From.get()
        end_time = self.To.get()

        time_to_col = {
            "1:00PM": 1, "2:00PM": 2, "3:00PM": 3, "4:00PM": 4,
            "5:00PM": 5, "6:00PM": 6, "7:00PM": 7, "8:00PM": 8,
            "9:00PM": 9, "10:00PM": 10, "11:00PM": 11, "12:00PM": 12
        }

        start_col = time_to_col.get(start_time)
        end_col = time_to_col.get(end_time)

        if start_col is None or end_col is None or start_col >= end_col:
            print("Invalid time range")
            return

        colspan = end_col - start_col

        colors = ["red", "blue", "green", "orange", "pink"]
        color = random.choice(colors)

        for i, day in enumerate(self.radio_buttons):
            if self.radio_buttons[day].get() == 1:
                task_block = customtkinter.CTkButton(
                    self.Tabview.tab("Day"),
                    text=task_name,
                    fg_color=color,
                    width=colspan * 60,
                    height=20
                )
                task_block.grid(
                    row=i + 1,
                    column=start_col,
                    columnspan=colspan,
                    padx=(5, 5),
                    pady=(0, 6),
                    sticky="we"
                )

        # Clear the entry boxes
        self.Task1.delete(0, 'end')
        self.From.set('')
        self.To.set('')

        for day in self.radio_buttons:
            self.radio_buttons[day].set(0)

if __name__ == "__main__":
    app = App()
    app.mainloop()
