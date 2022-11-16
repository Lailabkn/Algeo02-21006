from eigen import *
import numpy as np

# def EigenVector(matriks):
#     Q, R = QRDecomposition(matriks)
#     for i in range(0, 1, 1):
#         Q, R = QRDecomposition(np.dot(R, Q))
#     return (Q)

def EigenVector(matrix):
    pQ = np.eye(matrix.shape[0])
    temp = np.eye(matrix.shape[0])
    for i in range(0, 1, 1):
        Q, R = QRDecomposition(matrix)
        pQ = np.dot(pQ, Q)
        temp = np.dot(R, Q)
    return (pQ)

def EigenVectorList(L):
    hasil = []
    for i in range(0, len(L), 1):
        hasil.append(EigenVector(L[i]))
    return (hasil)