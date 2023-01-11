"""
Simple BlackJack Card implementation
"""


class Card:
    """
    A class to represent a playable card
    """

    RANKS = {
        2: ('dvojka', 'á'),
        3: ('trojka', 'á'),
        4: ('čtyřka', 'á'),
        5: ('pětka', 'á'),
        6: ('šestka', 'á'),
        7: ('sedmička', 'á'),
        8: ('osmička', 'á'),
        9: ('devítka', 'á'),
        10: ('desítka', 'á'),
        11: ('spodek', 'ý'),
        12: ('královna', 'á'),
        13: ('král', 'ý'),
        14: ('eso', 'é')
    }

    SUITS = {
        's': 'srdcov',
        'k': 'károv',
        'p': 'pikov',
        't': 'trefov',
    }

    @property
    def rank(self):
        """
        Card rank getter
        :return:
        """
        return self.__rank

    @rank.setter
    def rank(self, value):
        if value not in range(2, 15):
            raise TypeError("Given rank is not in range 2 .. 14")
        self.__rank = value

    @property
    def suit(self):
        """
        Card suit getter
        :return:
        """
        return self.__suit

    @suit.setter
    def suit(self, value):
        if value not in ['s', 'k', 'p', 't']:
            raise TypeError("Given suit is does not match s, k, p or t")
        self.__suit = value

    def __init__(self, given_rank, given_suit):
        self.__rank = None
        self.__suit = None
        self.rank = given_rank
        self.suit = given_suit

    def __str__(self):
        return self.SUITS[self.suit] + self.RANKS[self.rank][1] + " " + self.RANKS[self.rank][0]

    def __eq__(self, other):
        return self.black_jack_rank() == other.black_jack_rank()

    def __ge__(self, other):
        return self.black_jack_rank() >= other.black_jack_rank()

    def __gt__(self, other):
        return self.black_jack_rank() > other.black_jack_rank()

    def __le__(self, other):
        return self.black_jack_rank() <= other.black_jack_rank()

    def __lt__(self, other):
        return self.black_jack_rank() < other.black_jack_rank()

    def black_jack_rank(self):
        """
        Returns Card rank according to BlackJack rules
        :return:
        """
        if self.rank < 10:
            return self.rank
        if self.rank == 14:
            return 11
        return 10


if __name__ == '__main__':
    pass
