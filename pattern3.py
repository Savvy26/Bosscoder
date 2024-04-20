"""
1
1 2
1 2 3

"""

def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{j} ", end= "")
        print()

n = int(input("enter a number"))
pattern3(n)