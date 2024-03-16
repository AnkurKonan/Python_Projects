#Annotation
def increment(n: int) -> int:
    return n + 1
count: int = 0

#Exception
try:
    result = 2/0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    result = 1
print(result)

try:
    raise Exception("An error")
except Exception as error:
    print(error)
