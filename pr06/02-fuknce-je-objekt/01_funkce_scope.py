'''
@author: albert
'''

def vnejsi():
    """
    vnější funkce
    """
    x = 3
    def vnitrni():
        """
        vnitřní funkce má přístup k proměnným vnější funkce 
        """
        print("vnitrni tiskne poprve x : {}".format(x))
        print("vnitrni tiskne podruhe x : {}".format(x+1))
        
    vnitrni()    
    print("vnejsi tiskne x : {}".format(x))


def mutace():
    """
    mutable typ vás může překvapit...
    """
    x = [10, 20]
    print("hodnota x na začátku : {}".format(x))
    def vnitrni():
        """
        vnitřní funkce má přístup k proměnným vnější funkce - může je i modifikovat
        pokud jsou mutable (např. list)
        """
        x.append(1000)
        print("vnitrni tiskne  x : {}".format(x))
    
    vnitrni()    
    print("vnejsi tiskne x : {}".format(x))



if __name__ == '__main__':
    #vnejsi()
    mutace()