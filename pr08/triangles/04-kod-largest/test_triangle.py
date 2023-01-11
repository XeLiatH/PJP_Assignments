# -*- coding: utf-8 -*-

"""
Pokud chceme zjistit, který trojúhelník je největší, potřebujeme
funkci, která tento výpočet provede.
"""

import triangle

def test_triangle_size():
    """
    první test funkce pro velikost trojúhelníka zadaného pomocí bodů v rovině
    """
    point_a = (0, 0)
    point_b = (1, 0)
    point_c = (0, 1)

    expected_size = 0.5

    assert triangle.triangle_size(point_a, point_b, point_c) == expected_size


def test_triangle_size2():
    """
    druhý test funkce pro velikost trojúhelníka zadaného pomocí bodů v rovině
    jiné hodnoty
    """
    point_a = (0, 0)
    point_b = (2, 0)
    point_c = (0, 2)

    expected_size = 2.0

    assert triangle.triangle_size(point_a, point_b, point_c) == expected_size 


def test_zadani():
    """
    zakladni test / vzorové řešení ze zadání
    trojuhelnik tvori body (1, 1) (3, 1) (2, 2)
    """
    bod_a = (1, 1)
    bod_b = (3, 1)
    bod_c = (2, 3)
    bod_d = (2, 2)
    vzor = sorted((bod_a, bod_b, bod_c))
    vysledek = sorted(triangle.largest_triangle(bod_a, bod_b, bod_c, bod_d))
    assert vzor == vysledek

def test_zapornych():
    """
    trojuhelnik tvori body ABD + maji zaporne souradnice
    """
    bod_a = (0, 0)
    bod_b = (-10, 0)
    bod_c = (-2, -2)
    bod_d = (0, -5)
    vzor = sorted((bod_a, bod_b, bod_d))
    vysledek = sorted(triangle.largest_triangle(bod_a, bod_b, bod_c, bod_d))
    assert vzor == vysledek
