# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:26:40 2022

@author: sachin kelkar
"""
import numpy as np
def addition(a,b):
    x = a+b
    return x 
def mat(A,B,C):
    """ inputl 
    A : NxN matrix
    B:  3xN matrix
    C : NxN matrix
    
    output:
        this function algebrically manipulates the matrices
        to produce some shit
        
    """
    A_norm = np.linalg.norm(A)
    C = C@A
    A = A/A_norm
    b = B.T
    D = C@b
    return np.linalg.norm(D)


def matrix_calc(A,A_i):
    A[A_i,:] = np.inf
    
    return None

def TMT(a,b,c):
    if a == 1:
        print("a = 1")
    if a == 0:
        print("a = 0")
    print(np.pi*b)
    print(np.e*c)
   
        
    return b+c
    
    