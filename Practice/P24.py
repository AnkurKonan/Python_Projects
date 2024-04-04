for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("GAS GAS GAS!!")

for i in range(10):
    if i == 5:
        continue
    print(i)

number = int(input("Enter the number: \n"))
for i in range(1,11):
    print(str(number) + "X" + str(i) + "=" + str(i*number))

Friends = {"Ankur", "Shubham", "Sahil", "Bhavesh"}
for name in Friends:
    if name.startswith('S'):
        print("Hello " + name)
