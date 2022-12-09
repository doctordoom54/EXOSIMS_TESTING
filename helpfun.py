# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 13:32:51 2022

@author: sachin kelkar
"""

import numpy as np

# kill the diagonal of matrix with arbritary value
def fill_diag(A):
    """input:
        A : square matrix of size NxN
    output:
        B : Square matrix of size NxN with arbitrary high value for diagnoal
    """
    np.fill_diagonal(A, np.inf)
    return A


# kill the row with order [A_i,n]


def row_op(A, A_i):
    """
    Parameters
    ----------
    A : Matrix of size NxN
    A_i : Index of first target.

    Returns
    -------
    Matrix with row [A_i,n] with arbitrary high value.
    """
    A[A_i, :] = np.inf

    return A


def com_del(comp, i):
    """


    Parameters
    ----------
    comp : Nx1 completness matrix
    i : index of star .

    Returns
    -------
    Comp matrix with arbitrary high value at i.

    """
    comp[i] = 0
    return comp


def targets_del(M, a, b):
    """
    Parameters
    ----------
    M : NxN matrix.
    a : row index, integer
    b : column index,integer

    Returns
    -------
    M: NxN matrix with arbitrary high value for element (a,b).

    """
    M[a, b] = 1e9
    return M


def revisit(A, B, C):
    """


    Parameters
    ----------
    A : Size of null matrix [Nx1]
    B : Current matrix with number of observations [Nx1]
    C : current index of target observed [int]
        .

    Returns
    -------
    Updated matrix keeping count of number of observations done.[Nx1]

    """
    D = np.zeros(shape=(1, A))
    D[0, C] = 1
    D = D + B

    return D


def revisit_fun(A, a, b, c):
    """


    Parameters
    ----------
    A : NxN matrix with number of visits tab.
    a : Index of first target (int)
    b: Index of second target (int)
    c : Number of targets (int)
    Returns
    -------
    B: NxN matrix with updated visit tab at target a,b.

    """
    B = np.zeros((c, c))
    B[a, b] = 1
    B = B + A
    return B


def fill_d(A):
    """


    Parameters
    ----------
    A : NxN matrix  .

    Returns
    -------
    A : NxN matrix with 1e9 filled to diagonal.

    """
    A = np.fill_diagonal(A, 1e9)

    return A
