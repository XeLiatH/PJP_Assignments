'''
@author: Jiri Vrany
'''

def promluv(slovo, styl = 'nahlas'):
    
    def nahlas():
        return slovo.upper()+'!'
    
    def potichu():
        return slovo.lower()+'...'
    
    if (styl == 'nahlas'):
        return nahlas
    else:
        return potichu


if __name__ == '__main__':
    vysledek = promluv('TEEST', styl='potichu')
    print(type(vysledek))
    print(vysledek())