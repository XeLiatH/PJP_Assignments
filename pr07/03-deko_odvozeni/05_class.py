'''
Dekorátorem nemusí být pouze funkce. Může to být i jiný callable objekt.

Tedy například třída, která implementuje speciální metodu __call___

'''
from functools import wraps

class Tags(object):
    def __init__(self, tagname):
        self.tag = tagname

    def __call__(self, func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(self.tag, func(name))
        return func_wrapper    
    

@Tags("em")
@Tags("p")
def greetings(name):
    """
    tohle je funkce greetings 
    """
    return "Hello " + name
    
def demo():
    """
    výsledek je stejný jako v příkladě 04 - 
    """
    print(greetings('world'))
    print("jmeno dekorovane funkce:", greetings.__name__)
    print("jeji doc string:", greetings.__doc__)

if __name__ == '__main__':
    demo()