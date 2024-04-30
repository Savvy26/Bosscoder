'''
Given a square matrix mat, 
return the sum of the matrix diagonals. 
Only include the sum of all the elements on the primary 
diagonal and all the elements on the secondary diagonal 
that are not part of the primary diagonal.

Input 1: mat = [[1,2,3], [4,5,6], [7,8,9]]
Output 1: 25
Explanation 1: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25. Notice that element mat[1][1] = 5 is counted only once.
'''

def diagonal_sum():
    n = int(input("enter the dimension for your n*n matrix"))
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            x = int(input(f"enter a value for {i}{j} postion"))
            row.append(x)
        arr.append(row)

    sum = 0
    for i in range(0,n):
        for j in range(0,n):
            if (i == j or i+j == n-1):
                sum += arr[i][j]

    return sum
            
print(diagonal_sum())