"""
Pizza Factory - tovarni metoda pomoci slovniku
"""


class Pizza(object):

    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price


class HamAndMushroomPizza(Pizza):

    def __init__(self):
        super(HamAndMushroomPizza, self).__init__()
        self._price = 8.5


class DeluxePizza(Pizza):

    def __init__(self):
        super(DeluxePizza, self).__init__()
        self._price = 10.5


class HawaiianPizza(Pizza):

    def __init__(self):
        super(HawaiianPizza, self).__init__()
        self._price = 11.5


def create_pizza_dict(pizza='default'):
    """
    tovarni metoda
    kazda funkce v modulu je vlastne staticka metoda objektu
    vyhledani v hash tabulce ma slozitost O(1)
    """
    pizza_dict = {
        'HamAndMushroom': HamAndMushroomPizza,
        'Deluxe': DeluxePizza,
        'Hawaiian': HawaiianPizza,
        'default': Pizza
    }
    return pizza_dict[pizza]()


def create_pizza_getattr(pizza_type):
    """
    getattr je nejuniverzálnější
    """
    import sys
    this_mod = sys.modules[__name__]
    pizza_type = pizza_type + "Pizza"
    pizza = getattr(this_mod, pizza_type, Pizza)
    return pizza()
    


if __name__ == '__main__':
    for pizza_type in ('HamAndMushroom', 'Deluxe', 'Hawaiian'):
        print('Dictionary price of {0} is {1}'.format(pizza_type, create_pizza_dict(pizza_type).get_price()))

    for pizza_type in ('HamAndMushroom', 'Deluxe', 'Hawaiian'):
        print('Getattr price of {0} is {1}'.format(pizza_type, create_pizza_getattr(pizza_type).get_price()))
    