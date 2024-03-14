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

age = 19
def test():
    print(age)
print(age)
test()

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)
talk("I am going to buy milk")

def count():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        print(count)
    increment()
count()
