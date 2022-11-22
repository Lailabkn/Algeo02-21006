import numpy as np

def Normalize(matrix):
    matrix = np.square(matrix)
    matrix = np.sum(matrix)
    matrix = np.sqrt(matrix)
    return matrix