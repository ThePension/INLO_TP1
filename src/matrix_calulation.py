"""
Module that gathers methods to manipulate matrices.
"""
import numpy as np


def add(X, Y):
    """Adds 2 matrices"""
    return np.add(X, Y)


def mat_mul(X, Y):
    """Multiplies 2 matrices"""
    return np.matmul(X, Y)


def identity(order):
    """Returns the identity matrix"""
    return np.identity(order)
