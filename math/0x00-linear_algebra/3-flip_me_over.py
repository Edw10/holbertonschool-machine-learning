#!/usr/bin/env python3
""" Functrion matrix_transpose """


def matrix_transpose(matrix):
    """ return the transpose of a matrix """
    a = []
    for i in range(len(matrix[0])):
        a.append([])
    for i in matrix:
        c = 0
        for y in i:
            a[c].append(y)
            c += 1
    return a
