import os
import numpy as np
import sympy as sy
from Matrix import *

def eigenvalue(matriks):
    lamda = sy.symbols('y')
    Mat = matriks
    i = np.identity(len(Mat), dtype=float)  #fungsi identitas di sympy, bisa juga pake fungsi kita sendiri kalo udah bikin fungsi identitas
    Min = Mat - np.dot(lamda, i) #perkalian dot di numpy, bisa juga pake fungsi kalimatriks
    det = determinant(Min) #fungsi determinan di cobi.py
    hasil = sy.solve(det) #fungsi solve di sympy
    return (hasil)

def eigenvaluelist(L):
    hasil = []
    for i in range(0, len(L), 1):
        hasil.append(eigenvalue(L[i]))
    return (hasil)

def eigenvector(matriks):
# (A - yI) v = 0
# A = matriks kovarian
# y = eigenvalue
# I = identitas
# v = eigenvector
    lamda = sy.symbols('y')
    Mat = matriks
    i = sy.eye(len(Mat), dtype=float)  #fungsi identitas di sympy, bisa juga pake fungsi kita sendiri kalo udah bikin fungsi identitas
    y = np.dot(lamda, i) #perkalian dot di numpy, bisa juga pake fungsi kalimatriks
    Z = y.subs(lamda, eigenvalue(Mat)) # substitusi nilai eigenvalue ke y
    Min = Mat - Z 
    hasil = Min.nullspace() #fungsi nullspace di sympy
    return (hasil)
