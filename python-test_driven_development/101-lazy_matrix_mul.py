#!/usr/bin/python3
"""
Multiply 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the product of two matrices
    """
    return np.matmul(m_a, m_b)