# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:15:57 2024

@author: ASARE
"""

import numpy as np

# =============================================================================
# a  = np.array([[25,5,1],[64,8,1],[144,12,1]])
# 
# # b = (a[2][0]/a[0][0]) *a[0]
# 
# e = np.zeros((3,3))
# c = np.zeros((3,3))
# d = np.zeros((3,3))
# print("First Step in Gaussian Elimination")
# for i in range(0,3):
#     if (i < 2):
#         b = (a[i+1][0]/a[0][0]) *a[0]
#         e[i+1] = b
#     c[i] = a[i] - e[i]
# print(c)
# print("Second Step in Gaussian Elimination ")
# for i in range (1,3):
#     if (i < 2):
#         f = (c[i+1][1]/c[1][1]) *c[1]
#         d[i+1] = f
#     c[i] = c[i] - d[i]
# print(c)
# # print (a.shape[0])
# =============================================================================

def guassianElimination(numberRow, numberColumn,a=[]):
    assert numberRow == numberColumn
    alpha = np.zeros((numberRow,numberColumn))
    beta = np.zeros((numberRow,numberColumn))
    b = np.array(a)
    print (b)
    j = 0
    while j <numberRow-1:
        for i in range(0, numberColumn):
            if (i < numberColumn-j-1 ):
                elimination = (b[i+j+1][j]/b[j][j] * b[j])
                alpha[i+1] = elimination
            beta[i] = b[i] - alpha[i]
       # b = beta  
        j += 1
    print (beta)
# =============================================================================
#     for i in range (1, numberColumn):
#         if (i < numberColumn-1):
#             elimination = (beta[i+1][1]/beta[1][1] * beta[1])
#             alpha[i+1] = elimination
#         beta[i] = beta[i] - alpha[i]
#             
#     
# =============================================================================
guassianElimination(3,3, [[25,5,1],[64,8,1],[144,12,1]])