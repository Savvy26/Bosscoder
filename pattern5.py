"""
* * * * *  
* * * * 
* * * 
* * 
* 
"""

def pattern5(n):
    for i in range(1,n+1):
        for j in range(1,n - i +2):
            print("* ", end= "")
        print()

n = int(input("enter a number:"))
pattern5(n)