#!/usr/bin/env python3
""" derivate poli """


def poly_derivative(poly):
    """ poly pocket """
    if len(poly) == 0 or type(poly) != list:
        return None
    if all(isinstance(x, (int, float)) for x in poly):
        d = []    
        if len(poly) == 1:
            return [0]
        for i in range(1, len(poly)):
            d.append(poly[i]*i)
        return d
    return None
