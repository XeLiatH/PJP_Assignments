# -*- coding: utf-8 -*-
"""
ukazka urllib a parseru
"""

from html.parser import HTMLParser
import urllib.request

import utils


class FindHTML(HTMLParser):

    """
    Hledani textu a linku u odkazu
    """

    def __init__(self, *args, **kwargs):
        super(FindHTML, self).__init__(*args, **kwargs)
        self.text = []
        self.links = []
        self.semafor = False

    def handle_starttag(self, tag, attrs):
        """Zpracovaní oteviraciho tagu, napriklad <a>"""

        attrs = dict(attrs)
        if tag.lower() == 'a':
            self.find_href(attrs)
            self.semafor = True

    def handle_endtag(self, tag):
        """Zpracovaní uzaviraciho tagu, napriklad </a>"""

        if tag.lower() == 'a':
            self.semafor = False

    def handle_data(self, data):
        """Zpracovani dat uvnitr paroveho tagu"""

        if self.semafor:
            self.text.append(data)

    def find_href(self, attrs):
        """
        metoda pro hledani hodnoty atributu href
        """

        attrs = dict(attrs)
        if 'href' in attrs:
            self.links.append(attrs['href'])        



def parse_ḧtml(html_doc):
    """
    parse data from doc
    """
    
    parser = FindHTML()
    parser.feed(html_doc)
    parser.close()
    
    pairs = list(zip(parser.text, parser.links))
    [print(x) for x in pairs]



def main():
    """
    main routine
    """
    url = "http://als.tul.cz/"
    html_doc = utils.get_data_from_url(url)
    parse_ḧtml(html_doc)


if __name__ == "__main__":
    main()
