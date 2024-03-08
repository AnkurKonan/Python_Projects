from tkinter import *
root = Tk()
root.title("Configuration")
root.geometry("400x400")
def click():
    label1.config(text="New Text", font=("Apple", 40))
    root.config(bg="blue")
    button1.config(text="Configuration happened", state=DISABLED, pady=30)

label1 = Label(root, text="Text", font=("Apple", 20))
label1.pack(pady=10)
button1 = Button(root, text="Click Me", command=click)
button1.pack(pady=10)
root.mainloop()
