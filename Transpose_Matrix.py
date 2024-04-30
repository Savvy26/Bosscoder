'''
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
'''
def transpose(arr):
    arr = []
    m = len(arr)
    n = len(arr[0])

    trans = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(arr[j][i])
        trans.append(row)
    return trans

