import numpy as np
from Normalize import *

# QR Decomposition
def QR_Decomposition(matrix):
    n, m = matrix.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = matrix[:, 0]
    Q[:, 0] = u[:, 0] / Normalize(u[:, 0])

    for i in range(1, n):
        u[:, i] = matrix[:, i]
        for j in range(i):
            u[:, i] -= (matrix[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

        Q[:, i] = u[:, i] / Normalize(u[:, i]) # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = matrix[:, j] @ Q[:, i]

    return Q, R

# mengeluarkan eigen value
def eigVal(matrix):
    pQ = np.eye(matrix.shape[0]) # initialize matrix Q
    X = np.copy(matrix) # copy matrix
    for i in range(10): # loop 10x
        Q, R = QR_Decomposition(X) # get Q and R from QR Decomposition
        pQ = pQ @ Q
        X = R @ Q
    return np.diag(X) # return eigen value

# mengeluarkan eigen vector
def eigVec(matrix):
    pQ = np.eye(matrix.shape[0]) # initialize matrix Q
    X = np.copy(matrix) # copy matrix
    for i in range(10): # loop 10x
        Q, R = QR_Decomposition(X) # get Q and R from QR Decomposition
        pQ = pQ @ Q
        X = R @ Q
    return pQ # return eigen vector