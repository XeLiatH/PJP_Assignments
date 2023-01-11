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