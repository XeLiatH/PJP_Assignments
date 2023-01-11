# -*- coding: utf-8 -*-
'''
PJP prednaska 5
'''
import futils



def search_for_str(data):
    '''
    velice jednoducha ukazka hledani retezece v souboru
    '''
    
    result = []
    for line in data:
        pozice1 = line.find('class=')
        if pozice1 > 0:
            pozice1 += 6
            parznak = line[pozice1]
            pozice2 = line.find(parznak, pozice1 + 1,)
            if pozice2 > 0:
                result.append(line[pozice1 + 1:pozice2])

    return result

if __name__ == '__main__':
    data = futils.get_line_list('aktualne.html')
    print(search_for_str(data))
