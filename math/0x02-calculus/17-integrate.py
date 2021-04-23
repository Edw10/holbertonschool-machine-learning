#!/usr/bin/env python3
""" integral poli """


def poly_integral(poly, C=0):
    """ poly pocket """
    if type(poly) != list or len(poly) == 0:
        return None
    d = [C]
    for i in range(0, len(poly)):
        if poly[i] % (i+1) == 0:
            d.append(poly[i]//(i+1))
        else:
            d.append(poly[i]/(i+1))
    return d
