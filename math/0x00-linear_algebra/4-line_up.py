#!/usr/bin/env python3
""" Function add_arrays """


def add_arrays(arr1, arr2):
    """ return the add of two arrays """
    a = []
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            a.append(arr1[i]+arr2[i])
        return a
    else:
        return "None"
