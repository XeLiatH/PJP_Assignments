# -*- coding: utf-8 -*-
'''
Ukazka pouziti standardniho HTML parseru
'''


from html.parser import HTMLParser
import futils

class TransHTML(HTMLParser):

    '''A simple HTML transform-class based upon HTMLparser.'''

    def __init__(self, *args, **kwargs):
        '''
        html parser je OldStyle objekt / takze nemuzeme pouzit metodu super
        '''
        super(TransHTML, self).__init__(*args, **kwargs)
        self.data = []

    def find_class(self, attrs):
        '''
        metoda pro hledani hodnoty atributu class
        '''

        attrs = dict(attrs)
        if 'class' in attrs:
            print(attrs['class'])
            self.data.append(attrs['class'])

    def handle_starttag(self, tag, attrs):
        """Zpracovaní oteviraciho tagu, napriklad <a>"""

        self.find_class(attrs)

    def handle_startendtag(self, tag, attrs):
        """Zpracovaní neparoveho tagu, napriklad <br />"""

        self.find_class(attrs)



def parse_html(data):
    parser = TransHTML()
    parser.feed(data)
    parser.close()

    return parser.data



if __name__ == "__main__":
    small_file = 'aktualne.html'
    large_file = 'diveintopython3.html'
    data = futils.get_text(large_file)
    print(parse_html(data))
    