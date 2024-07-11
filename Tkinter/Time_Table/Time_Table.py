import customtkinter
import random
from openpyxl import Workbook

customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Time Table")
        self.geometry("920x630")
        self.resizable(False, False)
        self.rowconfigure(11, weight=1)
        self.columnconfigure(9, weight=1)

        self.main_frame = customtkinter.CTkFrame(self, fg_color="#f0f0f0", corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.main_frame2 = customtkinter.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        self.main_frame2.grid(row=0, column=0, padx=10, pady=10, sticky="we")

        self.Task = customtkinter.CTkLabel(self.main_frame2, text="Task:", font=("Helvetica", 16))
        self.Task.grid(row=0, column=0, padx=(10, 5), pady=(10, 10))
        self.Task1 = customtkinter.CTkEntry(self.main_frame2, width=200)
        self.Task1.grid(row=0, column=1, padx=(5, 10), pady=(10, 10))
        self.FromLabel = customtkinter.CTkLabel(self.main_frame2, text="From:", font=("Helvetica", 16))
        self.FromLabel.grid(row=0, column=2, padx=(5, 5))
        self.From = customtkinter.CTkEntry(self.main_frame2, width=100)
        self.From.grid(row=0, column=3, padx=(5, 10), pady=(10, 10))
        self.ToLabel = customtkinter.CTkLabel(self.main_frame2, text="To:", font=("Helvetica", 16))
        self.ToLabel.grid(row=0, column=4, padx=(5, 5))
        self.To = customtkinter.CTkEntry(self.main_frame2, width=100)
        self.To.grid(row=0, column=5, padx=(5, 10), pady=(10, 10))
        self.AddButton = customtkinter.CTkButton(self.main_frame2, text="Add", command=self.add, width=40, font=("Helvetica", 16))
        self.AddButton.grid(row=0, column=6, padx=(5, 10))

        self.checkbox_frame = customtkinter.CTkFrame(self.main_frame2, fg_color="white")
        self.checkbox_frame.grid(row=0, column=7, padx=(10, 10), pady=(10, 10))
        self.DayCheckbox = customtkinter.CTkCheckBox(self.checkbox_frame, text="Day")
        self.DayCheckbox.grid(row=0, column=0, pady=10, padx=(0, 10))
        self.NightCheckbox = customtkinter.CTkCheckBox(self.checkbox_frame, text="Night")
        self.NightCheckbox.grid(row=0, column=1, pady=10, padx=(10, 0))

        self.SaveButton = customtkinter.CTkButton(self.main_frame, text="Save to Excel", command=self.save_to_excel, font=("Helvetica", 16))
        self.SaveButton.grid(row=3, column=0, padx=10, pady=10, sticky="we")

        self.main_frame3 = customtkinter.CTkFrame(self.main_frame, fg_color="white", corner_radius=10)
        self.main_frame3.grid(row=1, column=0, padx=10, pady=10, sticky="we")
        self.days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        self.checkbox = {}
        for i, day in enumerate(self.days):
            self.checkbox[day] = customtkinter.CTkCheckBox(self.main_frame3, text=day)
            if day == "Mon":
                self.checkbox[day].grid(row=1, column=i, pady=10, padx=(100, 0), sticky="nw")
            else:
                self.checkbox[day].grid(row=1, column=i, pady=10, padx=(0, 0), sticky="nw")

        self.Tabview = customtkinter.CTkTabview(self.main_frame, height=400, fg_color="white", width=760, corner_radius=10)
        self.Tabview.grid(row=2, column=0, padx=10, pady=10)
        self.Tabview.add("Day")
        self.Tabview.add("Night")

        time_labels = ["1:00PM", "2:00PM", "3:00PM", "4:00PM", "5:00PM", "6:00PM", "7:00PM", "8:00PM", "9:00PM", "10:00PM", "11:00PM", "12:00PM"]
        time_labels2 = ["1:00AM", "2:00AM", "3:00AM", "4:00AM", "5:00AM", "6:00AM", "7:00AM", "8:00AM", "9:00AM", "10:00AM", "11:00AM", "12:00AM"]
        for i, time in enumerate(time_labels):
            customtkinter.CTkLabel(self.Tabview.tab("Day"), text=time, font=("Helvetica", 13)).grid(row=0, column=i + 1, padx=(0, 12))
        for i, day in enumerate(self.days):
            customtkinter.CTkLabel(self.Tabview.tab("Day"), text=day, font=("Helvetica", 16)).grid(row=i + 1, column=0, padx=(5, 5), pady=(0, 10), sticky="w")
        for i, time in enumerate(time_labels2):
            customtkinter.CTkLabel(self.Tabview.tab("Night"), text=time, font=("Helvetica", 13)).grid(row=0, column=i + 1, padx=(0, 12))
        for i, day in enumerate(self.days):
            customtkinter.CTkLabel(self.Tabview.tab("Night"), text=day, font=("Helvetica", 16)).grid(row=i + 1, column=0, padx=(5, 5), pady=(0, 10), sticky="w")

        self.timetable_data = []

    def add(self):
            task = self.Task1.get()
            start_time = int(self.From.get())
            end_time = int(self.To.get())

            time = {
                1: 1, 2: 2, 3: 3, 4: 4,
                5: 5, 6: 6, 7: 7, 8: 8,
                9: 9, 10: 10, 11: 11, 12: 12
            }

            start_time = time.get(start_time)
            end_time = time.get(end_time)

            if start_time is None or end_time is None or start_time >= end_time:
                print("Invalid time range")
                return

            colspan = end_time - start_time

            colors = ["#04c939", "#f24ef2", "#9133f5", "#3391f5", "#fa2d5d"]
            color = random.choice(colors)

            for i, day in enumerate(self.checkbox):
                if self.checkbox[day].get() == 1:
                    task_block = customtkinter.CTkButton(self.Tabview.tab("Day"), text=task, fg_color=color,
                                                         width=colspan * 60, height=30, corner_radius=5)
                    task_block.grid(row=i + 1, column=start_time, columnspan=colspan, padx=(5, 5), pady=(5, 5),
                                    sticky="we")
                    # Save to timetable data
                    self.timetable_data.append([day, task, f"{start_time}:00", f"{end_time}:00"])

            self.Task1.delete(0, 'end')
            self.From.delete(0, 'end')
            self.To.delete(0, 'end')

            for day in self.checkbox:
                self.checkbox[day].deselect()

    def save_to_excel(self):
        wb = Workbook()
        ws = wb.active
        ws.title = "Time Table"
        headers = ["Day", "Task", "From", "To"]
        ws.append(headers)
        for row in self.timetable_data:
            ws.append(row)
        wb.save("timetable.xlsx")
        print("Timetable saved to timetable.xlsx")

if __name__ == "__main__":
    app = App()
    app.mainloop()
