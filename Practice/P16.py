from functools import reduce
expense = [('Ankur', 60), ('Rahul', 80)]
sum = reduce(lambda a, b: a[1] + b[1], expense)
print(sum)
