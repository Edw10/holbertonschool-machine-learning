#!/usr/bin/env python3
""" Function add_matrices """


def add_matrices2D(mat1, mat2):
    """ return the add of two matrices """
    return [[i + j for i, j in zip(y, x)] for y, x in zip(mat1, mat2)]
    
