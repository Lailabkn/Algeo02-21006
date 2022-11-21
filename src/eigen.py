import numpy as np

# def QRDecomposition(matriks):
#     Q = np.zeros((len(matriks), len(matriks)))
#     R = np.zeros((len(matriks), len(matriks)))
#     for i in range(0, len(matriks), 1):
#         R[i][i] = np.linalg.norm(matriks[:, i])
#         Q[:, i] = matriks[:, i] / R[i][i]
#         for j in range(i + 1, len(matriks), 1):
#             R[i][j] = np.dot(Q[:, i], matriks[:, j])
#             matriks[:, j] = matriks[:, j] - R[i][j] * Q[:, i]
#     return (Q, R)

# def EigenVal(matriks):
#     Q, R = QRDecomposition(matriks)
#     for i in range(0, 1000, 1):
#         Q, R = QRDecomposition(np.dot(R, Q))
#     return (np.diag(R))

# def EigenValList(L):
#     hasil = []
#     for i in range(0, len(L), 1):
#         hasil.append(EigenVal(L[i]))
#     return (hasil)

def QR_Decomposition(matrix):
    n, m = matrix.shape # get the shape of A

    Q = np.empty((n, n)) # initialize matrix Q
    u = np.empty((n, n)) # initialize matrix u

    u[:, 0] = matrix[:, 0]
    Q[:, 0] = u[:, 0] / np.linalg.norm(u[:, 0])

    for i in range(1, n):
        u[:, i] = matrix[:, i]
        for j in range(i):
            u[:, i] -= (matrix[:, i] @ Q[:, j]) * Q[:, j] # get each u vector

        Q[:, i] = u[:, i] / np.linalg.norm(u[:, i]) # compute each e vetor

    R = np.zeros((n, m))
    for i in range(n):
        for j in range(i, m):
            R[i, j] = matrix[:, j] @ Q[:, i]

    return Q, R

def eigVal(matrix):
    pQ = np.eye(matrix.shape[0])
    X = np.copy(matrix)
    for i in range(10):
        Q, R = QR_Decomposition(X)
        pQ = pQ @ Q
        X = R @ Q
    return np.diag(X)

def eigVec(matrix):
    pQ = np.eye(matrix.shape[0])
    X = np.copy(matrix)
    for i in range(10):
        Q, R = QR_Decomposition(X)
        pQ = pQ @ Q
        X = R @ Q
    return pQ



