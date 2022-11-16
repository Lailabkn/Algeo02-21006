import numpy as np

def selisih(listofmatrix, matrix):
    hasil = []
    for i in range(0, len(listofmatrix), 1):
        hasil.append(abs(listofmatrix[i] - matrix))
    return (hasil)

def covarian(listofmatrix):
    hasil = []
    for i in range(0, len(listofmatrix), 1):
        hasil.append(np.cov(listofmatrix[i]))
    return (hasil)

def mean(listofmatrix):
    hasil = []
    for i in range(0, len(listofmatrix), 1):
        hasil.append(np.mean(listofmatrix[i], axis=0))
    return (hasil)