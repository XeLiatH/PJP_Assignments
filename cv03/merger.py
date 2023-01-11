"""
Na vstupu jsou dány 3 sekvence. Každá z nich obsahuje několik uspořádaných
dvojic uložených jako tuple (id, count).
Sekvence může tedy vypadat například takto: ((1, 3), (3, 4), (10, 2)).
První prvek sekvence je tedy tuple s hodnotami  id = 1 je count = 3 a tak dále.
Vaším úkolem je spojit tyto tři sekvence do jednoho slovníku. Ten bude výstupem z programu.

Položky slovníku budou v následujícím tvaru {id: [A, B, C]},
kde A, B a C jsou hodnoty pro příslušné ID v první, druhé a třetí sekvenci.

Ovšem pozor - neplatí, že každé id je obsaženo ve všech sekvencích.
Může být ve všech, ve dvou, nebo pouze v jedné.

Tady máte konkrétní příklad. Zadané sekvence mají následující podobu:

line_a = ((1, 3), (3, 4), (10, 2))
line_b = ((1, 2), (2, 4), (5, 2))
line_c = ((1, 5), (3, 2), (7, 3))

Transformací musí vzniknout následující slovník:

{1: [3, 2, 5], 
 2: [0, 4, 0],
 3: [4, 0, 2],
 5: [0, 2, 0],
 7: [0, 0, 3],
10: [2, 0, 0]}
"""

import itertools


def merge_tuples(line_a, line_b, line_c):
    """
    funkce merge tuples - spojujici sekvence
    """
    _dict = {}
    for (tup1, tup2, tup3) in itertools.zip_longest(line_a, line_b, line_c):
        if tup1 is not None:
            if tup1[0] not in _dict:
                _dict[tup1[0]] = [0, 0, 0]
            _dict[tup1[0]][0] += tup1[1]

        if tup2 is not None:
            if tup2[0] not in _dict:
                _dict[tup2[0]] = [0, 0, 0]
            _dict[tup2[0]][1] += tup2[1]

        if tup3 is not None:
            if tup3[0] not in _dict:
                _dict[tup3[0]] = [0, 0, 0]
            _dict[tup3[0]][2] += tup3[1]

    _sorted = {}
    for key in sorted(_dict.keys()):
        _sorted[key] = _dict[key]

    return _sorted


def simple_visual_test():
    """
    Print výsledku je sice primitivní metoda, ale jako základní test
    slouží programátorům odjakživa...
    """
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2))
    line_c = ((1, 5), (3, 2), (7, 3))
    print(merge_tuples(line_a, line_b, line_c))


if __name__ == "__main__":
    simple_visual_test()
