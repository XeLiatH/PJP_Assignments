"""
Může dekorátor přijímat argumenty? 

Může - je to funkce

Ale má to jeden háček...
"""


def tags(tag_name):
    """
    decorator tags - přidává xml tag: tag_name kolem textu
    """
    def tags_decorator(func):
        """
        tato funkce bude výsledkem dekorátoru - přebírá funkci k odekorování
        """
        def func_wrapper(name):
            """
            pokud původní funkce má argumenty jsou normálně přístupné
            nebo spíš budou - ve výsledné funkci
            """
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
    
        return func_wrapper
    
    return tags_decorator


@tags("p")
def greetings(name):
    """
    tohle je funkce greetings 
    """
    return "Hello " + name


def demo():
    """
    ukázka dekorace
    """
    print(greetings("DEMO"))


def demo_loss():
    """
    dekorováním ale zjevně ztrácíme informace
    """
    print("dekorovano: ", greetings("John"))
    print("jmeno dekorovane funkce:", greetings.__name__)
    print("jeji doc string:", greetings.__doc__)
    print("modul ze ktereho je importovana:", greetings.__module__)


if __name__ == "__main__":
    #demo()
    demo_loss()
