# -*- coding: utf-8 -*-
"""
ukazka urllib a parseru
"""

from bs4 import BeautifulSoup

 
import utils

def parse_html(html_doc):
    """
    run parsing on document
    """
        
    parser = BeautifulSoup(html_doc, "lxml")
    links = parser.findAll('a')
    pairs = [(link.text, link.get('href')) for link in links]
    [print(x) for x in pairs]


def main():
    """
    main routine
    """
    url = "http://als.tul.cz/"
    html_doc = utils.get_data_from_url(url)
    parse_html(html_doc)


if __name__ == "__main__":
    main()