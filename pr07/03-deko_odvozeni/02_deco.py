"""
@decorator je zjednodušení syntaxe (syntax sugar) použití dekorátoru
"""

def printer(fce):
    def wrapper(arg):
        y = fce(arg)
        print("Výsledek vaší funkce je: {}".format(y))
        #return y

    return wrapper

# dekorovaná fuknce
@printer 
def exp_power(x):
    """
    @returns x^x
    """
    return x**x

if __name__ == "__main__":
    exp_power(4)
    print(exp_power(2))
