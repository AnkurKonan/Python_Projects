#polymorphism
class Dog:
    def eat(self):
        print('Eating dog food')
class Cat:
    def eat(self):
        print('Eating cat food')
animal1 = Dog()
animal2 = Cat()
animal1.eat()
animal2.eat()

#operator overloading
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
ankur = Human('Ankur', 19)
yash = Human('Yash', 19)
print(ankur > yash)
