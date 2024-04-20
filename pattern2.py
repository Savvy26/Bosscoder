"""
N = 5

* 
* * 
* * * 
* * * * 
* * * * *

"""

def pattern2(n):
    for i in range(0,n+1,1):
        for j in range(1,i+1):
            print("* ", end = "")
        print()

n = int(input("enter the number"))
pattern2(n)