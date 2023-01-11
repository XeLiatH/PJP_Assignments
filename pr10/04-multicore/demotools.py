import math

def rozklad(cislo):
    """
    rozklad na prvočísla pomocí E. síta
    @param integer number
    @return list of primes
    """
    horni_mez = int(math.sqrt(cislo))
    prvocisla = eratosthenovo_sito(horni_mez)
    rozklad = []
    for prvocislo in prvocisla:
        while cislo % prvocislo == 0:
            rozklad.append(prvocislo)
            cislo /= prvocislo
    if cislo != 1:
        rozklad.append(cislo)
    return rozklad


def eratosthenovo_sito(limit):
    """
    Eratosthenovo síto nalezne prvočísla menší než 
    @param limit int number
    @return list of primes
    """
    limit += 1
    sito = [True] * limit

    for i in range(2, limit):
        if sito[i]:
            for j in range(i * 2, limit, i):
                sito[j] = False

    prvocisla = []
    for i in range(2, limit):
        if sito[i]:
            prvocisla.append(i)
    return prvocisla


def test_rozklad():
    """
    test rozkladu na prvocisla
    """
    assert rozklad(12) == [2, 2, 3]
    assert rozklad(15) == [3, 5]
    assert rozklad(9699690) == [2, 3, 5, 7, 11, 13, 17, 19]

