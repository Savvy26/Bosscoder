#Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
#To flip an image horizontally means that each row of the image is reversed.
#For example, flipping [1,1,0] horizontally results in [0,1,1]. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].
def flip():
    n = int(input("Dimension of  n X n matrix "))
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            x = int(input(f"enter binary number for {i}{j} postion"))
            row.append(x)
        arr.append(row)


    ans = []
    s = len(arr)
    for i in range(0,s):
        row = []
        for j in range(0,s):
            row.append(1 - arr[i][n-j-1])
        ans.append(row)
    return ans

print(flip())