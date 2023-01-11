"""
Memoization decorator s využitím vniřní třídy
v některých případech je patrně rychlejší
http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
"""


def memoize(f):
    """
    Memoization Cache Class
    """
    class memodict(dict):

        def __init__(self, f):
            self.f = f

        def __call__(self, *args):
            return self[args]

        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret

    return memodict(f)


@memoize
def fibonacci(n):
    "Return the nth fibonacci number."
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    """
    v tomto případě nás ovšem udeří RecursionError daleko dříve
    a ani setrecursionlimit nepomůže
    """
    import sys
    sys.setrecursionlimit(10000)
    print(fibonacci(500))
