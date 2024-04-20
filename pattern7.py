"""
    *
   ***
  *****
 *******
*********

"""
def pattern7(n):
    for i in range(1,n+1):
        for j in range(1, n - i +1): # printingspace
            print(" ",end="")
        for j in range(1,2 * i): # printing stars
            print("*",end="")
        print()

n = int(input("enter a number"))
pattern7(n)