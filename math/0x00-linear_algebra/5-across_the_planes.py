#!/usr/bin/env python3
""" Function add_matrices """


def add_matrices2D(mat1, mat2):
    """ return the add of two matrices """
    a = [[], []]
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for i in range(2):
            a[0].append(mat1[0][i]+mat2[0][i])
            a[1].append(mat1[1][i]+mat2[1][i])
        return a
    else:
        return "None"
