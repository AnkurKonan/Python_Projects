import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

calculation = ""
def add(symbol):
    global calculation
    calculation += str(symbol)
    result_area.delete(1.0, "end")
    pass
def clear(symbol):
    pass
def evaluate(symbol):
    pass

result_area = tk.Text(root, height = 2, width=15, font=("Apple", 24))
result_area.grid(columnspan=5)
root.mainloop()
