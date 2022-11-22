import numpy as np

def Normalize(matrix): # normalize matrix
    matrix = np.square(matrix) # square matrix
    matrix = np.sum(matrix) # sum matrix
    matrix = np.sqrt(matrix) # square root matrix
    return matrix