#!/usr/bin/env python3
""" Function cat_arrays """


def cat_arrays(arr1, arr2):
    """ return the concat of two arrays """
    a = []
    for i in arr1:
        a.append(i)
    for i in arr2:
        a.append(i)
    return a
