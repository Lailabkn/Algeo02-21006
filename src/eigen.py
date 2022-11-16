import numpy as np

def QRDecomposition(matriks):
    Q = np.zeros((len(matriks), len(matriks)))
    R = np.zeros((len(matriks), len(matriks)))
    for i in range(0, len(matriks), 1):
        R[i][i] = np.linalg.norm(matriks[:, i])
        Q[:, i] = matriks[:, i] / R[i][i]
        for j in range(i + 1, len(matriks), 1):
            R[i][j] = np.dot(Q[:, i], matriks[:, j])
            matriks[:, j] = matriks[:, j] - R[i][j] * Q[:, i]
    return (Q, R)

def EigenVal(matriks):
    Q, R = QRDecomposition(matriks)
    for i in range(0, 100, 1):
        Q, R = QRDecomposition(np.dot(R, Q))
    return (np.diag(R))

def EigenValList(L):
    hasil = []
    for i in range(0, len(L), 1):
        hasil.append(EigenVal(L[i]))
    return (hasil)