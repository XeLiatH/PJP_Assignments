"""
Tento příklad ukazuje, co se stane když neuzavřete soubor po zápise.
"""


def wri():
    f1 = open('pokus.txt', 'w')
    f1.write('hello world')
    #f1.close()

    f2 = open('pokus.txt', 'r')
    print(f2.read())

if __name__ == '__main__':
    wri()
    