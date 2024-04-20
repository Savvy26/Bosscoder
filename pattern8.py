"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
"""
def pattern8(n):
    for i in range(1,2*n):
        star = 0
        if(i <= n):
            star = i+1
        else:
            star = 2*n -i +1
        for j in range(1,star):
            print("* ",end="")
        print()

n = int(input("enter a number"))
pattern8(n)