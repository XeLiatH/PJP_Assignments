# -*- coding: UTF-8 -*-

"""
Vypis titulku z RSS kanalu pomoci ElementTree parseru
"""

import xml.etree.ElementTree as eltree                                       

if __name__ == '__main__':

    xmldoc = eltree.parse('data/cesky.xml')

    root = xmldoc.getroot()

    titles = [item.find('title').text for item in root.iter('item')]

    [print(title) for title in titles]