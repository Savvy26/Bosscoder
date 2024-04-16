#Average of Three Numbers
a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
c = int(input("enter 3rd number"))

def avg(a,b,c):
    return (a+b+c) // 3

print(avg(a,b,c))