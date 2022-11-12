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
        As = copy_matrix(A) # B) make a copy, and ...
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

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
 
        :return: A copy of the given matrix
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])
 
    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)
 
    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
 
    return MC

def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
 
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M

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
