#!/bin/env python
# -*- coding: utf-8 -*-
"""
PJP - cvičení číslo 2
"""

import math


def tuple_sub(point_A, point_B):
    return point_A[0] - point_B[0], point_A[1] - point_B[1]


def calc_angle(vector_A, vector_B):
    return math.degrees(
        math.acos((vector_A[0] * vector_B[0] + vector_A[1] * vector_B[1]) / (
                math.sqrt(vector_A[0] ** 2 + vector_A[1] ** 2) * math.sqrt(vector_B[0] ** 2 + vector_B[1] ** 2))))


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí, 
    zda tvoří konvexní čtyřúhelník.
    
    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří. 
    """

    AB = tuple_sub(a, b)
    AD = tuple_sub(a, d)
    CB = tuple_sub(c, b)
    CD = tuple_sub(c, d)

    try:
        alpha = calc_angle(AB, AD)
        beta  = calc_angle(AB, CB)
        gamma = calc_angle(CB, CD)
        delta = calc_angle(AD, CD)
    except ZeroDivisionError:
        return False

    angles = [alpha, beta, gamma, delta]

    if sum(angles) != 360:
        return False

    return True


if __name__ == '__main__':
    print(is_convex((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0)))
    print(is_convex((0.0, 0.0), (0.2, 0.7), (1.0, 1.0), (0.0, 1.0)))
