Students = ["Ankur", "Yash", "Arsh", "Garv", 2,5,90]
Students2 = [12,53,7,63,89,35,56]
Students3 = ["Ankur", "Yash", "Arsh", "Garv"]
Students[6] = 67
Students.append("Rahul")
Students.extend(["Agam", 89])
Students.remove("Arsh")
Students.insert(3, "Rohit")
Students[1:1] = ["Anand", "Roshan"]
StudentsCopy = Students2[:]
Students2.sort()
Students3.sort(key=str.lower)
print(sorted(Students3, key=str.lower))

print("Ankur" in Students)
print(Students[0])
print(Students)
print(Students[-1])
print(Students[2:1])
print(Students[:3])

#Set
Set1 = {"Ankur", 56, "Rajiv"}
Set2 = {"Ankur", 78, "Ganga"}
intersection = Set1 & Set2
mod = Set1 | Set2
# mod = Set1 < Set2
# mod = Set1 > Set2
difference = Set1 - Set2
print(list(Set1))

print(mod)
print(difference)
print(intersection)
