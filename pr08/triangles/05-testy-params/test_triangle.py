# -*- coding: utf-8 -*-

"""
Pokud chceme zjistit, který trojúhelník je největší, potřebujeme
funkci, která tento výpočet provede.
"""
import pytest
import triangle


@pytest.mark.parametrize("tri_points, expected_size", [
    (((0, 0), (1, 0), (0, 1)), 0.5),
    (((0, 0), (2, 0), (0, 2)), 2)
])
def test_triangle_size(tri_points, expected_size):
    """
    parametrický test nám stačí jen jeden
    funkce pro velikost trojúhelníka zadaného pomocí bodů v rovině
    """
    point_a, point_b, point_c = tri_points

    assert triangle.triangle_size(point_a, point_b, point_c) == expected_size


@pytest.mark.parametrize("points, expected_triangle", [
    (((1, 1), (3, 1), (2, 3), (2, 2)), ((1, 1), (3, 1), (2, 3))),
    (((0, 0), (-10, 0), (-2, -2), (0, -5)), ((0, 0), (-10, 0),  (0, -5)))
])
def test_zadani(points, expected_triangle):
    """
    zakladni test / vzorové řešení ze zadání
    trojuhelnik tvori body (1, 1) (3, 1) (2, 2)
    """
    bod_a, bod_b, bod_c, bod_d = points

    vzor = sorted(expected_triangle)
    vysledek = sorted(triangle.largest_triangle(bod_a, bod_b, bod_c, bod_d))
    assert vzor == vysledek
