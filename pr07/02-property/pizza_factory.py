"""
Pizza Factory - ukazka z knihy
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Factory_method_examples#Python

Tohle je ovšem spíše Java přepsaná do Python syntaxe...
"""


class Pizza(object):

    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price


class HamAndMushroomPizza(Pizza):

    def __init__(self):
        self._price = 8.5


class DeluxePizza(Pizza):

    def __init__(self):
        self._price = 10.5


class HawaiianPizza(Pizza):

    def __init__(self):
        self._price = 11.5

#
# PizzaFactory
#


class PizzaFactory(object):

    @staticmethod
    def create_pizza(pizza_type):
        """
        staticmethod je dekorator
        rozhodovani pomoci nekolika elif neni nejlepsi pristup
        """
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()


def main():
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
        print('Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price()))

if __name__ == '__main__':
    main()
