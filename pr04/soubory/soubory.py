"""
Prace se souborem, textove i binarne
"""

def show_binary():
    """
    textovy soubor muzeme otevrit i jako binarni
    rozdil je v chovani na platforme Windows z duvodu jine sekvence pro konce radku
    v Unixu neni vlastne nutne, ale pro lepsi prenositelnost ho muzete nechat
    """
    with open("soudata.txt","rb") as bin_file:
        print(bin_file.read())
    

def show_text():
    """
    textovy soubor a ukazka pohybu v suboru pomoci seek
    """

    with open("soudata.txt", "r", encoding="utf-8") as text_file:
        print(text_file.name)
        print(dir(text_file))
        print(text_file.tell())
        print(text_file.read(16))
        print(text_file.tell())
        text_file.seek(28)
        print(text_file.tell())
        print(text_file.read(10))
        print(text_file.writable())

    
def show_iter():
    """
    textovy soubor a ukazka iterace přes řádky
    """

    with open("soudata.txt", "r", encoding="utf-8") as text_file:
        for nr, line in enumerate(text_file):
            print(nr, line.strip())
            

if __name__ == "__main__":
    #print("BINARY")
    #show_binary()
    #print("SEEK IN TEXT")
    #show_text()
    print("ITERACE")
    show_iter()