# -*- coding: UTF-8 -*-

"""
Parsovani velkych soubory pomoci Eltree iter parseru
"""
import xml.etree.ElementTree as etree
import bz2

def fix_tag(ns, nsmap, tag):
    return '{{{}}}{}'.format(nsmap[''], tag)


def parse_dump(xml_fn):
    with bz2.BZ2File(xml_fn, 'r') as fr:
        nsmap = {}
        for event, elem in etree.iterparse(fr, events=('end', 'start-ns')):
            if event == 'start-ns':
                ns, url = elem
                nsmap[ns] = url
            
            if event == 'end':
                if elem.tag == fix_tag('', nsmap, 'page'):
                    title = elem.find(fix_tag('', nsmap, 'title')).text
                    yield title
                    elem.clear()


if __name__ == '__main__':

    fname = 'data/cswiki-latest-pages-articles.xml.bz2'

    pattern = "kolo"
    
    counter = 0
    for title in parse_dump(fname):
        if pattern in title:
            print(title)
            counter += 1
        
        if counter >= 10:
            break
