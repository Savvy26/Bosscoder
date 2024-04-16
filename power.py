#Take 2 numbers from the user, x & n. Find xn (Calculate this without using the inbuilt function).

x = int(input(" enter the number :"))
n = int(input(" enter the power :"))

def pow(x, n):
    return x ** n

print(pow(x,n))