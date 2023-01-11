"""
Vypis titulku z RSS kanalu pomoci minidom parseru
"""

# -*- coding: UTF-8 -*-

from xml.dom import minidom                                          

if __name__ == '__main__':

    xmldoc = minidom.parse('data/cesky.xml')
    
    items = xmldoc.getElementsByTagName('item')

    titles = [item.getElementsByTagName('title')[0].firstChild.data for item in items]

    [print(title) for title in titles]