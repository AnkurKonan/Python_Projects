#with
class DogNotException(Exception):
    print("inside")
    pass
try:
    raise DogNotException()
except DogNotException:
    print("Dog not found")

#list compression
numbers = [2,3,5,6,7,8]
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
numbers_power_2 = list(map(lambda n : n**2, numbers))
