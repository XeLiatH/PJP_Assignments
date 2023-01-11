'''
@author: Jiri Vrany
'''


def volany_ucastnik(param_fce):
    print("1. chystam se zavolat předanou funkci")
    param_fce()
    print('2. hotovo')


def nejaka_jina_funkce():
    print('3. @TODO dulezita funkce')

if __name__ == '__main__':
    volany_ucastnik(nejaka_jina_funkce)
