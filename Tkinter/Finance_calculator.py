import tkinter
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Title of GUI
        self.title("Finance Calculator")
        self.geometry("1200x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=0, column=2, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("Compound Interest")
        self.tabview.add("Simple Interest")
        self.tabview.add("SIP Calculator")
        self.tabview.tab("Compound Interest").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Simple Interest").grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=1, column=2, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("ROI Calculator")
        self.tabview.add("CAGR Calculator")
        self.tabview.add("XIR Calculator")
        self.tabview.tab("ROI Calculator").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("CAGR Calculator").grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=0, column=1, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("Bond Calculator")
        self.tabview.add("TVM Calculator")
        self.tabview.add("ARP Calculator")
        self.tabview.tab("Bond Calculator").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("TVM Calculator").grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=1, column=0, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("Credit Card Payment")
        self.tabview.add("Credit Card Minimum payment")
        self.tabview.add("Discount & Tax")
        self.tabview.tab("Credit Card Payment").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Credit Card Minimum payment").grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=0, column=0, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("Percentage Calculator")
        self.tabview.add("Loan Calculator")
        self.tabview.add("Auto Loan Calculator")
        self.tabview.tab("Percentage Calculator").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Loan Calculator").grid_columnconfigure(0, weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=300)
        self.tabview.grid(row=1, column=1, padx=(10), pady=(10), sticky="nsew")
        self.tabview.add("Retirement Calculator")
        self.tabview.add("Tip Calculator")
        self.tabview.add("IRR NPV calculator")
        self.tabview.tab("Retirement Calculator").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tip Calculator").grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()
