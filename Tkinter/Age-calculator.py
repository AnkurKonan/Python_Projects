from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title("Age Calculator")
root.geometry("260x270")
root["bg"] = "white"

def age():
    if my_entry.get():
        current_year = datetime.now().year
        your_age = current_year - int(my_entry.get())
        messagebox.showinfo("Your Age", f"Your Age Is: {your_age}")

    else:
        messagebox.showerror("Please enter your age")


l1 = Label(root, text="                                                                        ",
           fg="white", bg="green")
l1.pack()
my_label = Label(root, text="Enter Year Date of birth", font=("Apple", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Apple", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="Calculate", font=("Apple", 18), command=age)
my_button.pack(pady=20)
l2 = Label(root, text="                                                                       ",
           fg="white", bg="green")
l2.pack()
root.mainloop()


# To run this program -->
# python3 Age-calculator.py
# To terminate the program -->
# press --> control + c
