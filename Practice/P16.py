from functools import reduce
expense = [('Ankur', 60), ('Rahul', 80)]
sum = reduce(lambda a, b: a[1] + b[1], expense)
print(sum)

#Recussion
# def factorial(n):
#     if n == 1: return 1
#     return n * factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

#Decorators
def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper
@logtime
def hello():
    print("hello")
hello()
