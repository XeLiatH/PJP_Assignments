# -*- coding: utf-8 -*-
"""
řešení úkolu 2 - postup
1. vytvořit kombinace bodů = 4 trojúhelníky
2. spočítat obsah každého trojúhelníka
3. najít maximální obsah
4. pokud maximum == 0 trojúhelník neexistuje - vrátit false
"""

import itertools

def triangle_size(triangle):
    """
    :param points
    :return triangle size
    S=\frac{1}{2}|(po_c[0] - po_a[0])(po_b[1] - po_a[1]) - (po_c[1] - po_a[1])(po_b[0] - po_a[0])|
    """
    po_a, po_b, po_c = triangle
    citatel = (po_c[0] - po_a[0]) * (po_b[1] - po_a[1]) - (po_c[1] - po_a[1]) * (po_b[0] - po_a[0])
    return abs(citatel) / 2.0

def get_triangle(po_a, po_b, po_c, po_d):
    """
    :param points (ax, ay)
    :return three points composing the larges triangle
    """ 
    triangles = list(itertools.combinations((po_a, po_b, po_c, po_d), 3))
    triangle_sizes = [triangle_size(tri) for tri in triangles]
    max_size = max(triangle_sizes)
    if max_size:
        max_idx = triangle_sizes.index(max_size)
        return triangles[max_idx]

    return False    


