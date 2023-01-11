"""
Kombinace dvou principů:

- funkce může být předána jako parametr jiné funkci

- funkce může vrátit funkci jako výsledek
"""

def printer(fce):
    """
    funkce která vytiskne výsledek argumentu

    Tuto funkci nazýváme dekorátor
    """
    def wrapper(arg):
        """
        Nová funkce - která bude výsledkem volání funkce printer

        Vypočítá výsledek parametru (fce) a vytiskne jeho výsledek
        """
        y = fce(arg)
        print("Výsledek vaší funkce je: {}".format(y))

    return wrapper
    
def exp_power(x):
    """
    @returns x^x
    """
    return x**x

def demo1():
    """
    pomocí dekorátoru vytvoříme novou funkci - tu použíjeme
    """
    newname = printer(exp_power)
    newname(4)

def demo2():
    """
    Dekorované funkci ale není potřeba dávat jméno

    Tento zápis je ale hůře čitelný
    """
    printer(exp_power)(4)


if __name__ == "__main__":
    print(exp_power(4))
    demo1()
    demo2()
    
