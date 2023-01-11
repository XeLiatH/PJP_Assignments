'''
Created on 3.11.2010

@author: albert
'''
import gzip
import pickle

def ukazka_gzip():
    """
    Gzip soubor v repozitáři není - je moc velký. 
    Musíte si tedy nejprve nějaký vytvořit či stáhnout.
    """
    with gzip.open("data.sql.gz", "r") as gdata:
        data = gdata.readlines()

    display = 35    
    print("počet řádků v gzip souboru: ", len(data))    
    print("řádek číslo {}: ".format(display), data[display])
    
    
def ukazka_pickle_dump():
    favorite_color = { "lion": "yellow", "kitty": "red", "process": ukazka_gzip}
    pickle.dump( favorite_color, open( "color.pickle", "wb" ) )


def ukazka_pickle_load():
    colors = pickle.load(open("color.pickle", "rb"))
    print(colors)
    print(type(colors))
    colors["process"]()

if __name__ == '__main__':
    
    #print("Ukázka čtení GZIP souboru")
    #ukazka_gzip()
    print("Ukázka Pickle")
    #ukazka_pickle_dump()
    ukazka_pickle_load()