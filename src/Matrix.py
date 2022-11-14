#PROGRAM LibraryMatriks
#Spesifikasi: Berisi fungsi-fungsi untuk mengoperasikan matriks dan senarai matriks
#Spesifikasi: MATRIX | LIST OF MATRIX

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

def minusMatrixAbs (matrix1, matrix2):
    row = len(matrix1)
    col = len(matrix1[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = abs(matrix1[i][j] - matrix2[i][j])
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

def LambdaIMinA (m, y):
    #'y' adalah representasi lambda
    
    # Inisialisasi Matriks Indentitas #
    row = len(m)
    col = len(m[0])
    I = createMatrix(row, col)
    for i in range(0, row, 1):
        for j in range(0, col, 1):
            if (i == j):
                I[i][j] = y
    # Mengurangi dengan 'A' #
    result = minusMatrix(I, m)
    return(result)

#--------------------------------------------------------------------#
#------------------------KELOMPOK DETERMINAN-------------------------#
#--------------------------------------------------------------------#
# Referensi: https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
def determinant (A):
    total = 0.0
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
     
    # Section 2: when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
 
    # Section 3: define submatrix for focus column and 
    #      call this function
    for fc in indices: # A) for each focus column, ...
        # find the submatrix ...
        As = copyMatrix(A) # B) make a copy, and ...
        As = As[1:] # ... C) remove the first row
        height = len(As) # D) 
 
        for i in range(height): 
            # E) for each remaining row of submatrix ...
            #     remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
 
        sign = (-1) ** (fc % 2) # F) 
        # G) pass submatrix recursively
        sub_det = determinant(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det 
 
    return total

def copyMatrix (m):
    row = len(m)
    col = len(m[0])
    result = createMatrix(row, col)
    for i in range(0, row, 1):
       for j in range(0, col, 1):
           result[i][j] = m[i][j]
    return (result)
#--------------------------------------------------------------------#


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

def listMatrixMinusAbs (L, m):
    N = len(L)
    row = len(L[0])
    col = len(L[0][0])
    result = createListMatrix(N, row, col)
    i = 0
    while (i < N):
        result[i] = minusMatrixAbs(L[i], m)
        i = i + 1
    return (result)

def makeCovarians (L):
    N = len(L)
    row = len(L[0])
    col = len(L[0][0])
    result = createListMatrix(N, row, col)
    i = 0
    while (i < N):
        T = transposeMatrix(L[i])
        result[i] = multiplyMatrix(L[i], T)
        i = i + 1
    return (result)

def typeCasting (L):
    N = len(L)
    row = len(L[0])
    col = len(L[0][0])
    for i in range(0, N, 1):
        for j in range(0, row, 1):
            for k in range(0, col, 1):
                L[i][j][k] = float(L[i][j][k])
    return (L)


#PROGRAM UTAMA (CONTOH)
#L = createListMatrix (3,3,3)
#L[0] = [[3,5,8],[0,1,6],[10,20,9]]
#L[1] = [[4,3,2],[3,1,6],[8,0,1]]
#L[2] = [[2,4,2],[0,1,3],[0,4,2]]

#M = createMatrix(3,3)
#M[0] = [2,1,3]
#M[1] = [4,-2,5]
#M[2] = [-3,-1,7]

#print(determinant(M))
#M = LambdaIMinA(M,2)
#displayMatrix(M)
