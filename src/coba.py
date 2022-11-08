#PROGRAM LibraryMatriks
#Spesifikasi :

#FUNGSI DAN PROSEDUR
#Membuat dan Menampilkan Matriks
def createMatrix (nRows, nCols):
    m = [[0 for j in range(nCols)] for i in range(nRows)]
    return (m)

def displayMatrix (m):
    row = len(m)
    col = len(m[0])
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            if (j == col-1):
                print(m[i][j])
            else:
                print(m[i][j],end=' ')
    print("\n")

#Membuat dan Menampilkan List Matriks
def createListMatrix (N, nRows, nCols):
    L = [[[0 for j in range(nCols)] for i in range(nRows)] for k in range(N)]
    return (L)

def displayListMatrix (L):
    N = len(L)
    for k in range(0, N, 1):
        displayMatrix(L[k])

#Operasi Terhadap Matriks
def addMatrix (matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = matrix1[i][j] + matrix2[i][j]
    return (result)

def minusMatrix (matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = matrix1[i][j] - matrix2[i][j]
    return (result)

def multiplyMatrix (matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix2[0])
    result = createMatrix(row, col);
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            for k in range(0, len(matrix1[0]), 1):
                result[i][j] = result[i][j] + (matrix1[i][k] * matrix2[k][j])
    return (result)

def matrixDivide (m, k):
    row = len(m)
    col = len(m[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = m[i][j]/k
    return (result)

def transposeMatrix (m):
    row = len(m)
    col = len(m[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = m[j][i]
    return (result)

def copyMatrix (m):
    row = len(m)
    col = len(m[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = m[i][j]
    return (result)

#Operasi Terhadap List Matriks
def meanElements (L):
    N = len(L)
    row = len(L[0])
    col = len(L[0][0])
    result = createMatrix(row, col)
    i = 0
    while (i < N):
        result = addMatrix(result, L[i])
        i = i + 1
    result = matrixDivide(result, N)
    return (result)

def listMatrixMinus (L, m):
    N = len(L)
    row = len(L[0])
    col = len(L[0][0])
    result = createListMatrix(N, row, col)
    i = 0
    while (i < N):
        result[i] = minusMatrix(L[i], m)
        i = i + 1
    return (result)


#PROGRAM UTAMA
L = createListMatrix (3,3,3)
L[0] = [[3,5,8],[0,1,6],[10,20,9]]
L[1] = [[4,3,2],[3,1,6],[8,0,1]]
L[2] = [[2,4,2],[0,1,3],[0,4,2]]

a = copyMatrix(L[0])
displayMatrix(a)
