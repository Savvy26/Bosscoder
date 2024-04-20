"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

def pattern6(n):
    for i in range (1,n+1):
        for j in range(1,n - i + 2):
            print(f"{j} ",end= "")
        print()

n = int(input("enter a number"))
pattern6(n)