# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:15:57 2024

@author: Boateng Kwabena Henry
"""

import numpy as np


# =============================================================================
# def guassianElimination(numberRow, numberColumn,a=[]):
#     if numberColumn != numberRow:
#         raise ValueError ("The Number of rows must be equal to the number of Columns")
#     alpha = np.zeros((numberRow,numberColumn))
#     beta = np.zeros((numberRow,numberColumn))
#     b = np.array(a)
#     print (b)
#     i = 0
#     while i <numberRow-1:
#         #Finding the pivot element
#         pivot = b[i:, i]
#         pivot_index = np.argmax(np.abs(pivot))
#         pivot_index += i
#         print(pivot)
#         print(pivot_index)
#         
#         #Swapping rows to reduce Round-off error and Division by Zero errors
#         if  pivot_index != i:
#             b[[i, pivot_index]] = b[[pivot_index, i]]
#             alpha[[i, pivot_index]] = alpha[[pivot_index, i]]
#         
#         #performing Elimination
#         for j in range(0, numberColumn):
#             if (j < numberColumn-i-1 ):
#                 division = b[j][i] / b[i][i]
#                 beta[i] =( b[i] - division ) * b[j]
#                 print(beta)
#                 # alpha[j][i:] = a[j][i:] - division * a[i][i:]
#         b = beta  
#         i += 1
#     print (beta)
# 
# guassianElimination(3,3, [[25,5,1],[64,8,1],[144,12,1]])
# 
# =============================================================================


def guassianElimination(a_matrix, b_matrix):
    a = np.array(a_matrix)
    b = np.array(b_matrix)
    
    if a.shape[0] != a.shape[1]:
        print("Error: The row is not equal to the column")
        return
    if b.shape[1] > 1 or b.shape[0] != a.shape[0]:
        print("Error: Constant Vector is incorrectly sized")
        return
    
    n = len(b_matrix)
    m = n-1
    i = 0
    x = np.zeros(n)
    new_line = "\n"

    augmented_matrix = np.concatenate((a_matrix,b_matrix), axis = 1 , dtype= float)
    
  
    while i < n:
        #Partial Pivoting
        for p in range(i+1 , n):
            if  abs(augmented_matrix[i,1] < abs(augmented_matrix[p,i])):
                augmented_matrix[[p, i]]  = augmented_matrix[[i,p]]
                
        if augmented_matrix[i,i] == 0.0:
            print("Error: Divide by Zero error")
            return
        
        for j in range(i+1, n):
            scalar = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] -(scalar* augmented_matrix[i])
            print (augmented_matrix)

vari = np.array([[2,3],
                 [4,5]]
                 )
cons = np.array([[9],
                 [12]])
guassianElimination(vari,cons )