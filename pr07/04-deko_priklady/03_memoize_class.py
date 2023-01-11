"""
Další možnost implementace memcache pomocí třídy
"""

import collections
import functools


class Memoized(object):
    """
    memoize class
    """

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        """
        typy které nemohou být klíčem slovníku - nejsou hashable je lépe nepokoušet
        """
        if not isinstance(args, collections.Hashable):
            return self.func(*args)
        
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value

    def __repr__(self):
        """
        Return the function's docstring.
        """
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """
        Support instance methods.
        """
        return functools.partial(self.__call__, obj)


@Memoized
def fibonacci(n):
    """
    Return the nth fibonacci number.
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    """
    v tomto případě nás ovšem udeří RecursionError daleko dříve
    """
    print(fibonacci(165))
