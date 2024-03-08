from tkinter import *
from random import randint

root = Tk()
root.title('')
root.geometry("400x400")

def pick():
	candidates = ["Ankur", "Rahul", "Yash", "Davinder", "John", "David", "Joy"]
	candidates_set = set(candidates)
	unique_entries = list(candidates_set)

	our_number = len(unique_entries) - 1
	rando = randint(0, our_number)

	winnerLabel = Label(root, text=unique_entries[rando], font=("Helvetica", 18))
	winnerLabel.pack(pady=50)

topLabel = Label(root, text="Football", font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = Button(root, text="Picking winners", font=("Helvetica", 24), command=pick)
winButton.pack(pady=20)
root.mainloop()
