"""
ukazka objektu s definovanou relaci usporadani
"""

class Foo:

    def __init__(self, x):
        self._x = x

    def __eq__(self, other):

        if type(other) == type(self):
            return self._x  == other._x
        else:
            return False

    def __gt__(self, other):

        if type(other) == type(self):
            return self._x  > other._x
        else:
            raise TypeError("Foo cannot be compared to %s" % str(type(other)))

    def __lt__(self, other):

        if type(other) == type(self):
            return self._x  < other._x
        else:
            raise TypeError("Foo cannot be compared to %s" % str(type(other)))            

if __name__ == "__main__":

    f1 = Foo(1)

    f2 = Foo(2)

    print('f1 is smaller than f2:', f1 < f2)  # True
    
    print('f1 is equal to f2:', f1 == f2)    # False
    
    print('f1 is None:', f1 == None)         # False

    x = list("string")
    print(x)
    try:
        print(x > f1)
    except TypeError as e:
        print(repr(e))    
