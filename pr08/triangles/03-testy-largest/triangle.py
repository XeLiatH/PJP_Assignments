# -*- coding: utf-8 -*-

"""
Úkol:
Vytvořite funkci, která ze 4 zadaných bodů vybere trojici,
tvořící trojúhelník s největším obsahem. 

Body na vstupu jsou zadávány jako tuple (x, y),
kde x a y mohou být libovolná reálná čísla,
tedy i záporná. Počet trojúhelníků je obvykle čtyři,
ale není to pravidlem. Může jich být i méně a je potřeba
aby funkce hlídala i extrémní situace,
jako například, že body trojúhelník vůbec nevytváří.

Příklad řešení:
Body A(1,1), B(3,1), C(2,2), D(2,3) tvoří vzájemně
čtyři různé trojúhelníky ABC, ABD, ACD, BCD. 

Největší obsah má trojúhelník ABD. 
"""

def triangle_size(po_a, po_b, po_c):
    """
    vypočte velikost trojúhelníka zadaného trojicí bodů po (x, y)
    
    vzorec viz. https://cs.wikipedia.org/wiki/Troj%C3%BAheln%C3%ADk#Obvod_a_obsah
    """
    cit = (po_c[0] - po_a[0]) * (po_b[1] - po_a[1]) - (po_c[1] - po_a[1]) * (po_b[0] - po_a[0])
    return 0.5 * abs(cit)




if __name__ == '__main__':
    pass