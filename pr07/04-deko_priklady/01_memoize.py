import functools
import time
import sys
import decorators

def memoize(obj):
    """
    memoize je asi nejznámnější dekorátor 
    jde o jednoduchou implementaci memcache
    """

    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    """
    Fibbonaciho posloupnost se vraci...
    Zapis pomoc rekurze ma ale svoje limity.
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def demo():
    """
    332 je maximum, 333 raises RecursionError
    pomoci sys muzeme zvednout 
    bez memoize 35 vs 40
    """
    sys.setrecursionlimit(10000)
    t1 = time.time()
    print(fibonacci(3000))
    t2 = time.time()
    print("funkce bezela {:5f} s".format(t2 - t1))

if __name__ == '__main__':
    demo()
