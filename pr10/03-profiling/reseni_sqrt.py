from math import sqrt


def get_triangle(a, b, c, d):
    """
    @param: celkem 4 body ve formatu (x, y)
    @return: 3 body ktere tvori nejvetsi trojuhelnik
    """

    Sabc = plocha_trojuhelnika(a, b, c)
    Sacd = plocha_trojuhelnika(a, c, d)
    Sabd = plocha_trojuhelnika(a, b, d)
    Sbcd = plocha_trojuhelnika(b, c, d)
    if Sabc >= Sacd and Sabc >= Sabd and Sabc >= Sbcd:
        return a, b, c
    elif Sacd >= Sabc and Sacd >= Sabd and Sacd >= Sbcd:
        return a, c, d
    elif Sabd >= Sabc and Sabd >= Sacd and Sabd >= Sbcd:
        return a, b, d
    else:
        return b, c, d


def delka_usecky(a, b):
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    return sqrt((ax - bx) * (ax - bx) + (ay - by) * (ay - by))


def perimetr_trojuhelnika(a, b, c):
    ab = delka_usecky(a, b)
    ac = delka_usecky(a, c)
    bc = delka_usecky(b, c)
    return ab + ac + bc


def plocha_trojuhelnika(a, b, c):
    ab = delka_usecky(a, b)
    ac = delka_usecky(a, c)
    bc = delka_usecky(b, c)
    p = perimetr_trojuhelnika(a, b, c)
    return sqrt(p * (p - ab) * (p - ac) * (p - bc))


def main():
    a = (1, 1)
    b = (3, 1)
    c = (2, 2)
    d = (2, 3)
    print(get_triangle(a, b, c, d))

if __name__ == '__main__':
    main()
