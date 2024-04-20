"""
Pattern 1
------------
N = 5

* * * * *
* * * * *
* * * * *
* * * * *
* * * * * 
"""
def pattern1(n):
    for i in range(1,n+1,1):
        for j in range(1,n+1,1):
            print("* " , end = "")
        print()

n = int(input("Enter the value of n"))
pattern1(n)