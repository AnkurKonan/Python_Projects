#map, filter, reduce
numbers = [4,6,7,2]
def double(a):
    return a * 2
result = map(double, numbers)
print(list(result))

numbers = [3,4,5,6]
result = map(lambda a : a * 2, numbers)
print(list(result))

numbers = [3,4,5,6,7,8,9,2]
def isEven(n):
    return n % 2 == 0
result = filter(isEven, numbers)
print(list(result))

numbers = [4,5,6,7,8,9]
result = filter(lambda n : n % 2 == 0, numbers)
print(list(result))

from functools import reduce
expense = [('Ankur', 60), ('Rahul', 80)]
sum = reduce(lambda a, b: a[1] + b[1], expense)
print(sum)
