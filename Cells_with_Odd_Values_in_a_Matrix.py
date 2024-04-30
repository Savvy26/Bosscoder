NOT DONE YET....

'''
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.
'''
indices = []
n = int(input("enter the dimension"))
for i in range(0,n):
    row = []
    for j in range(0,n):
        x = int(input(f"enter the value for {i}{j}"))
        row.append(x)
    indices.append(row)

print(indices)
'''
arr = []
m  = int(input("enter the no of rows"))
n = int(input("enter the coloumn"))
for i in range(0,m):
    row = []
    for j in range(0,n):
        x = 0
        row.append(x)
    arr.append(row)

print(arr)'''

for i in range(0,n):
    for j in range(0,n):
        print(indices[i][j])