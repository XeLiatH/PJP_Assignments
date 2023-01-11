'''
Ukazka prace s doctest

Pokud je vse ok, nevypise se nic
v opacnem pripade se vypise test, ktery selhal
'''


def is_divisible_by_2_or_5(number):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(15)
    True
    """
    return number % 2 == 0 or number % 5 == 0


def remove_vowels(slovo):
    """
    >>> remove_vowels('vasik pasik')
    'vsk psk'
    """
    samohl = "aeiouyAEIOUY"
    s_bez_samohl = ""
    for letter in slovo:
        if letter not in samohl:
            s_bez_samohl += letter
    return s_bez_samohl


if __name__ == '__main__':
    import doctest

    doctest.testmod()
