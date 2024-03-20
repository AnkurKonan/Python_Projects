import tkinter as tk

root = tk.Tk()
root.geometry("300x400")

calculation = ""
def add(symbol):
    global calculation
    calculation += str(symbol)
    result_area.delete(1.0, "end")
    result_area.insert(1.0, calculation)
def clear(symbol):
    global calculation
    calculation = ""
    result_area.delete(1.0, "end")
def evaluate(symbol):
    global calculation
    try:
        calculation = str(eval(calculation))
        result_area.delete(1.0, "end")
        result_area.insert(1.0, calculation)
    except:
        clear()
        result_area.insert(1.0, "Error")
def clear_field():
    global calculation
    calculation = ""
    result_area.delete(1.0, "end")

result_area = tk.Text(root, height = 2, width=15, font=("Apple", 24))
result_area.grid(columnspan=5)
btn1 = tk.Button(root, text='1', command=lambda: add(1), width=5, font=('Apple', 14))
btn1.grid(rows = 2, column = 1)
btn2 = tk.Button(root, text='2', command=lambda: add(1), width=5, font=('Apple', 14))
btn2.grid(rows = 2, column = 2)
btn3 = tk.Button(root, text='2', command=lambda: add(1), width=5, font=('Apple', 14))
btn3.grid(rows = 2, column = 3)
btn3 = tk.Button(root, text='3', command=lambda: add(1), width=5, font=('Apple', 14))
btn3.grid(rows = 3, column = 1)
btn4 = tk.Button(root, text='4', command=lambda: add(1), width=5, font=('Apple', 14))
btn4.grid(rows = 3, column = 2)
btn5 = tk.Button(root, text='5', command=lambda: add(1), width=5, font=('Apple', 14))
btn5.grid(rows = 3, column = 3)
btn6 = tk.Button(root, text='6', command=lambda: add(1), width=5, font=('Apple', 14))
btn6.grid(rows = 4, column = 1)
btn7 = tk.Button(root, text='7', command=lambda: add(1), width=5, font=('Apple', 14))
btn7.grid(rows = 4, column = 2)
btn8 = tk.Button(root, text='8', command=lambda: add(1), width=5, font=('Apple', 14))
btn8.grid(rows = 4, column = 3)
btn9 = tk.Button(root, text='9', command=lambda: add(1), width=5, font=('Apple', 14))
btn9.grid(rows = 2, column = 2)
btn0 = tk.Button(root, text='0', command=lambda: add(1), width=5, font=('Apple', 14))
btn0.grid(rows = 2, column = 3)
root.mainloop()


