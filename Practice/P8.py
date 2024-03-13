#Enums
from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(list(State))
print(len(State))

#Inputs
# number1 = int(input("Enter 1st number: "))
# number2 = int(input("Enter 2nd number: "))
# number3 = input("Enter 3rd number: ")
# number4 = input("Enter 4th number: ")

# numbers_concatenated = number3 + number4
# numbers_added = number1 + number2
# print(numbers_added)
# print(numbers_concatenated)
