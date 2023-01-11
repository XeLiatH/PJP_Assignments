# -*- coding: UTF-8 -*-

from xml.dom import minidom                                          

if __name__ == '__main__':

    xmldoc = minidom.parse('data/cds.xml')
    
    nodes = xmldoc.childNodes
    
    node = nodes[0]
    
    print(node.tagName)
    print(node.firstChild)
    print(node.lastChild)
    print(node.parentNode)
   
    