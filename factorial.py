#Find Factorial value of the given Integer
n = int(input("enter the number which factorial you want"))
factorial = 1
for i in range(2, n+1, 1):
    factorial *= i
print(factorial)