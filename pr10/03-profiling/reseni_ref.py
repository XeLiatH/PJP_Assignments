#!/usr/bin/env python
'''
Modul s odevzdanym ukolem
'''


def vector(point_a, point_b):
    '''
    sestroji vektor ze dvou bodu
    @param {tuple} point_a / bod (x, y)
    @param {tuple} point_b / bod (x, y)
    @return {tuple} vector / vektor (vx, vy)
    '''
    return (point_b[0] - point_a[0], point_b[1] - point_a[1])


def triangle_size(vec_a, vec_b):
    '''
    vypocita obsah trojuhelnika
    @param {tuple} vec_a (vx,vy)
    @param {tuple} vec_b (vx,vy)
    @return {float} size
    '''
    return abs(vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0]) / 2.0


def compute_vectors(point_a, point_b, point_c, point_d):
    '''
    vypocitat vsechny prislusne vektory
    @param {tuple} point_a, b, c, d - body (x, y)
    @return {dictionary} vectors
    '''
    vectors = {}
    vectors["AB"] = vector(point_a, point_b)
    vectors["BA"] = (-vectors["AB"][0], -vectors["AB"][1])

    vectors["BC"] = vector(point_b, point_c)
    vectors["CB"] = (-vectors["BC"][0], -vectors["BC"][1])

    vectors["CD"] = vector(point_c, point_d)
    vectors["DC"] = (-vectors["CD"][0], -vectors["CD"][1])

    vectors["DA"] = vector(point_d, point_a)
    vectors["AD"] = (-vectors["DA"][0], -vectors["DA"][1])

    return vectors


def compute_triangle_sizes(point_a, point_b, point_c, point_d):
    '''
    vypocitat velikost vsech trojuhelniku
    @param {tuple} point_a, b, c, d - body (x, y)
    @return {dictionary} triangle sizes
    '''
    # Compute vectors
    vectors = compute_vectors(point_a, point_b, point_c, point_d)
    # Compute triangle sizes
    triangle_sizes = {}
    triangle_sizes[(point_a, point_b, point_c)] = \
        triangle_size(vectors["BA"], vectors["BC"])
    triangle_sizes[(point_b, point_c, point_d)] = \
        triangle_size(vectors["CB"], vectors["CD"])
    triangle_sizes[(point_c, point_d, point_a)] = \
        triangle_size(vectors["DC"], vectors["DA"])
    triangle_sizes[(point_d, point_a, point_b)] = \
        triangle_size(vectors["AD"], vectors["AB"])

    return triangle_sizes


def get_triangle(point_a, point_b, point_c, point_d):
    '''
    @param: celkem 4 body ve formatu (x, y)
    @return: 3 body ktere tvori nejvetsi trojuhelnik
    '''
    max_size = 0
    biggest_triangle = False
    triangle_sizes = compute_triangle_sizes(point_a, point_b, point_c, point_d)
    # Find the triangle wit the biggest size
    for triangle in triangle_sizes:
        if triangle_sizes[triangle] > max_size:
            max_size = triangle_sizes[triangle]
            biggest_triangle = triangle

    return biggest_triangle

if __name__ == '__main__':
    print(get_triangle((1, 1), (3, 1), (2, 2), (2, 3)))
