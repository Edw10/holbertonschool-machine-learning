#!/usr/bin/env python3
""" derivate poli """


def poly_derivative(poly):
    """ poly pocket """
    if len(poly) == 0:
        return None
    if all(not isinstance(x, (int, float)) for x in poly):
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
