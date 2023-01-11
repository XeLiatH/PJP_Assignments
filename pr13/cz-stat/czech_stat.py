# coding: utf-8
"""
statistikA potratU po obcich
Nacita excellovske tabulky z CSU 

@Autor Jan Cibulka https://www.irozhlas.cz/jan-cibulka-5345565?page=1

@Motivace 

Bohužel už se mi nedaří najít původní článek/tweet. Šlo o to, že ČSU (nebo to byl jiný úřad?)
odmítal tuto statistiky vydat s tím, že to není možné, protože data jsou uložena po obcích v excellu a vytvoření
požadovaného přehledu by zabralo měsíc času a práce úředníků...
"""

import urllib
import pandas as pd
from bs4 import BeautifulSoup
import re
import os

# extrakce odkazů z webu CZSO
req = urllib.request.urlopen('https://www.czso.cz/csu/czso/databaze-demografickych-udaju-za-obce-cr').read().decode('utf-8')
soup = BeautifulSoup(req, 'html.parser')

for url in soup.find_all('a', href=re.compile('obce_d/srp')):
    urllib.request.urlretrieve('https://www.czso.cz' + url.get('href'), './scratch/potraty/' + url.get('href').split('/')[-1])

# extrakce dat z excel pekla
out = pd.DataFrame()
for file in os.listdir('./scratch/potraty/'):
    temp = pd.read_excel('./scratch/potraty/' + file)
    out = out.append(temp, ignore_index=True)

# odstranění teček a pomlček v hodnotách
def remove_interpunction(pulp):
    if ((str(pulp) == '.') | (str(pulp) == '-')):
        return None
    else:
        return pulp
    
out[['Sňatky', 'Rozvody', 'Potraty']] = out[['Sňatky', 'Rozvody', 'Potraty']].applymap(lambda x: remove_interpunction(x))

# filtrace a export ve formátu pro lidi
out[out.Rok == 2014].to_csv('./scratch/potraty_tbl.csv', encoding='utf-8')