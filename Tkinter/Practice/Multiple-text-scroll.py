from tkinter import *

root = Tk()
root.title('Multiple Text Scrolls')
root.geometry("400x500")

def multiple_yview(*args):
	my_text1.yview(*args)
	my_text2.yview(*args)
	print(*args)

my_frame = Frame(root)
my_frame.pack(pady=20)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

my_text1 = Text(my_frame, width=20, height=25, highlightbackground="blue", highlightthickness=5, font=("Helvetica", 16), yscrollcommand=text_scroll.set, wrap="none")
my_text1.pack(side=RIGHT, padx=10)
my_text2 = Text(my_frame, width=20, height=25, highlightbackground="blue", highlightthickness=5, font=("Helvetica", 16), yscrollcommand=text_scroll.set, wrap="none")
my_text2.pack(side=LEFT)

text_scroll.config(command=multiple_yview)
root.mainloop()
