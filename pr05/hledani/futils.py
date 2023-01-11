        
def get_line_list(filename):
    '''
    nacte data ze souboru jako list
    '''
    try:
        with open(filename, 'r') as htmlfile:
            data = htmlfile.readlines()
    except IOError:
        print('chyba cteni')
        data = False

    return data        

def get_text(filename):
    '''
    nacte data ze souboru jako retezec
    '''
    try:
        with open(filename, 'r') as htmlfile:
            data = htmlfile.read()
    except IOError:
        print('chyba cteni')
        data = False

    return data        

