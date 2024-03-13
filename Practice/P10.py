#Tuples
names = ("Ankur", "Yash", "Rohit", "Ivy", "Rahul")
print(names[0])
print(names[0:2])
print(names.index("Ankur"))
print(len(names))
print(sorted(names))
print("Ankur" in names)

#Dictonary
Avengers = {"ironman": "armor", "thor": "maljorin"}
Avengers["cap"] = "shield"
Avengers["ironman"] = "blaster"
print(Avengers)
print(Avengers.get("ironman"))
print(Avengers.keys())
print(list(Avengers.keys()))
print(list(Avengers.values()))
print(list(Avengers.items()))
print(len(Avengers))
print(Avengers.pop("thor"))
print(Avengers.popitem())
print("thor" in Avengers)
