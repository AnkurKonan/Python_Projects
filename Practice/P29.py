#Reading
f = open('Gas.txt')
data1 = f.read(43)
data1 = f.readline() #1st line
data1 = f.readline() #2nd line
data1 = f.readline() #3rd line
data1 = f.readline() #4th line
print(data1)
f.close()

#Writing
w = open('Write.txt', 'w')
w.write("Programming can teach you how to think & how to create ideas")
w.close()

#By using with
with open("Gas.txt", 'r') as f:
    a = f.read()
with open("Write.txt", 'w') as f:
    a = f.write("Speed speed boy gasoline burning")
print(a)
