number = int(input("Enter the number: "))
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print(f"The factorial of {number} is {factorial}")

#Patterns
n = 4
for i in range(9):
    print("*" * (1+i))

for i in range(9):
    print("*" * (2*i+1))

n = 6
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))
