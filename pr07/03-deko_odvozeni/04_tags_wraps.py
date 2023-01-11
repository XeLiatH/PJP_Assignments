"""
Korektní chování dekorátoru nám zajístí...

dekorátor @wraps
"""

from functools import wraps


def tags(tag_name):
    """
    decorator tags - přidává xml tag: tag_name kolem textu
    """
    def tags_decorator(func):
        """
        tato funkce bude výsledkem dekorátoru - přebírá funkci k odekorování
        """
        @wraps(func)
        def func_wrapper(name):
            """
            pokud původní funkce má aragumenty jsou normálně přístupné
            nebo spíš budou - ve výsledné funkci
            """
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        
        return func_wrapper
    
    return tags_decorator


@tags("neco")
@tags("h1")
def greetings(name):
    """
    tohle je funkce greetings 
    """
    return "Hello " + name


def demo():
    """
    print("dekorovano: ", greetings("John"))
    print("jmeno dekorovane funkce:", greetings.__name__)
    print("jeji doc string:", greetings.__doc__)
    """
    print("dekorovano: ", greetings("John"))
    print("jmeno dekorovane funkce:", greetings.__name__)
    print("jeji doc string:", greetings.__doc__)
   


if __name__ == "__main__":
    demo()