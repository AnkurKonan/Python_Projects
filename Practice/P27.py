def maximum(n1, n2,n3):
    if (n1 > n2 & n1 > n3):
        return n1
    elif(n2 > n3 & n2 > 1):
        return n2
    else:
        return n3
print(maximum(3423,5634,7556))

def maximum1(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3
m = maximum1(13343, 5534, 234)
print("The value of the maximum is " + str(m))


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Entre 4th number: "))
if a > b and a > c and a > d:
  print('the largest number' + str(a))
elif a < b and a < c and a < d:
  print('the smallest number' + str(a))
elif b > a and b > c and b > d:
  print('the largest number' + str(b))
elif b < a and b < c and b < d:
  print('the smallest number is' + str(b))
elif d > a and d > b and d > c:
  print('the biggest number is' + str(d))
elif d < a and d < b and d < c:
  print('the smallest number is'+ str(d))
  
print("I", end=" ")
print("am", end=" ")
print("a", end=" ")
print("software engineer", end=" ")

n = 10
for i in range(10):
    print("*" * (n-i))

