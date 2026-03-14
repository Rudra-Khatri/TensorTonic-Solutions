import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    row = len(A)
    col = len(A[0])
    mn = np.zeros((col, row))

    for i in range(row):
        for j in range(col):
            mn[j][i] = A[i][j]
    return mn
    
