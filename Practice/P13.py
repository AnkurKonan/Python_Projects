#Classes
class Animal:
    def walk(self):
        print("walking")
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print("bhaaao!")
pitbull = Dog("bhaaao!", 7)
print(type(pitbull))
print(pitbull.name)
print(pitbull.age)
print(pitbull.bark)
print(pitbull.walk)
print(pitbull.bark())
