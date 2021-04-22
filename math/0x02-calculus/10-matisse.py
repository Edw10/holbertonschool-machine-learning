#!/usr/bin/env python3
""" derivate poli """


def poly_derivative(poly):
    """ poly pocket """
    if len(poly) == 0 or type(poly) != list:
        return None
    for i in poly:
        if type(i) != int and type(i) != float:
            return None
    d = []    
    if len(poly) == 1:
        return [0]
    for i in range(1, len(poly)):
        d.append(poly[i]*i)
    return d
