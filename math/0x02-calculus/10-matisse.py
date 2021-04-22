#!/usr/bin/env python3
""" derivate poli """


def poly_derivative(poly):
    """ poly pocket """
    if len(poly) == 0:
        return None
    d = []
    if all(isinstance(x, int) for x in poly):    
        if len(poly) == 1:
            return [0]
        for i in range(1, len(poly)):
            d.append(poly[i]*i)
        return d
