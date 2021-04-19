#!/usr/bin/env python3
def matrix_shape(matrix):
    # sadasd
    a = []
    while type(matrix) is not int:
        a.append(len(matrix))
        matrix = matrix[0]
    return a
