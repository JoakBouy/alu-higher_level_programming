#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        row_squared = list(map(lambda x: x**2, row))
        new_matrix.append(row_squared)
    return new_matrix
