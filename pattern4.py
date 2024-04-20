"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""
def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f"{i} ",end="")
        print()

n = int(input("enter a value:"))
pattern4(n)
