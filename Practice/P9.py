Students = ["Ankur", "Yash", "Arsh", "Garv", 2,5,90]
Students[6] = 67
Students.append("Rahul")
Students.extend(["Agam", 89])
Students.remove("Arsh")
Students.insert(3, "Rohit")
Students[1:1] = ["Anand", "Roshan"]
#Sort only works when there are items of same datatype
# Students.sort()

print("Ankur" in Students)
print(Students[0])
print(Students)
print(Students[-1])
print(Students[2:1])
print(Students[:3])
