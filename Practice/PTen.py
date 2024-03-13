def hello(name, age):
    print("Hello " + name + " you are " + str(age) + " years old")
print("Ankur", 19)

def change(value):
    value = 2
val = 1
change(val)
print(val)

def hello(name):
    if not name:
        return
    print("Hello " + name)
hello(False)
