"""
A file containing function split_text to split text base on individual words
"""

import re


def split_text(text):
    """
    @TODO: viz. zadani na elearning.fm.tul.cz
    """

    return re.compile(r'[^ \t\n\r\f\v,.?!:/+]+', re.MULTILINE).findall(text)


def simple_visual_test():
    """
    A function to provide a quick feedback, only for testing purposes

    @:return void
    """
    text = """Programovací jazyk Python přispívá k
         rychlému vývoji. Python se sice snaží být intuitivní,
        ale obsahuje věci, které nejsou všední, a příliš se o nich neví.

        A nyní něco úplně jiného: jedna. Kde leží Frýdek-Místek?
        Jedna + jedna se rovná? Totéž co čtyři / dvěma!
        """

    print(split_text(text))


if __name__ == "__main__":
    simple_visual_test()
