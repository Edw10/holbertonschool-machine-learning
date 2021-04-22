#!/usr/bin/env python3
""" derivate poli """


def poly_derivative(poly):
    """ poly pocket """
    if len(poly) == 0:
        return None
    for i in poly:
        if type(i) != int and type(i) != float:
            return None
    d = []    
    if len(poly) == 1:
        return [0]
    for i in range(1, len(poly)):
        if poly[i] != 0:
            d.append(poly[i]*i)
        else:
            d.append(0)
    return d
