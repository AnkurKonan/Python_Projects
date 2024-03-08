from tkinter import *

root = Tk()
root.title('Window-Info')
root.geometry("800x800+-1900+100")

def info():
	dimension_label = Label(root, text=root.winfo_geometry())
	dimension_label.pack(pady=20)

	height_label = Label(root, text=f"Height: {root.winfo_height()}")
	height_label.pack(pady=20)
	width_label = Label(root, text=f"Width: {root.winfo_width()}")
	width_label.pack()

	x_label = Label(root, text="X: " + str(root.winfo_x()))
	x_label.pack(pady=20)
	y_label = Label(root, text="Y: " + str(root.winfo_y()))
	y_label.pack()

my_button = Button(root, text="Show Info", command=info)
my_button.pack(pady=20)

root.mainloop()
