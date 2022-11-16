from eigen import *
import numpy as np

def EigenVector(matriks):
    Q, R = QRDecomposition(matriks)
    for i in range(0, 1, 1):
        Q, R = QRDecomposition(np.dot(R, Q))
    return (Q)

def EigenVectorList(L):
    hasil = []
    for i in range(0, len(L), 1):
        hasil.append(EigenVector(L[i]))
    return (hasil)