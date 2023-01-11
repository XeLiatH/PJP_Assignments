"""
Implementuje program dle zadání úlohy 11. na elearning.tul.cz
"""

import sys
import argparse
import re


def censor(char, text, banned_words):
    """
    Replaces banned words in text by specified character
    """
    for word in banned_words:
        pattern = r"\b" + word + "\\b"
        text = re.sub(pattern, transform_word(char, word), text)
    return text


def transform_word(char, word):
    """
    Transform the word to n characters, where n is the length of the word
    For example red -> ###
    """
    return char * len(word)


def strip_tags(html_data):
    """
    Stripts the html tags from a string
    """
    stripped = re.sub(r'<[^<]+?>', '', str(html_data))
    # trimming useless empty lines
    stripped = filter(lambda x: not re.match(r'^\s*$', x), stripped.splitlines())
    return '\n'.join(stripped)


def split_text(text):
    """
    Splits text by individual words
    """
    return re.compile(r'[^ \t\n\r\f\v,.?!:/+]+', re.MULTILINE).findall(text)


def parse_args(args):
    """
    Parses command line arguments
    """
    parser = argparse.ArgumentParser(description="Simple censorship program to keep "
                                                 "freedom of speech in check")

    parser.add_argument('-i', '--input', type=str, required=True,
                        help="file with content to be censored")
    parser.add_argument('-l', '--list', type=str, required=True,
                        help="file containing banned words")
    parser.add_argument('-o', '--output', default=False, required=False,
                        help="output file, printed if not specified")
    parser.add_argument('-c', '--clean', default=False, required=False, action='store_true',
                        help="text only output")

    args = parser.parse_args(args)

    return args


def handle_io(args):
    """
    Handles the input arguments of the program
    """
    parsed = parse_args(args)
    with open(parsed.input, 'r', encoding="utf-8") as file:
        text = file.read()

    with open(parsed.list, 'r', encoding="utf-8") as file:
        words = file.read().splitlines()

    if parsed.clean:
        text = strip_tags(text)

    text = censor('#', text, words)

    if parsed.output:
        with open(parsed.output, 'w', encoding="utf-8") as file:
            file.write(text)
        return 1

    print(text)

    return 0


if __name__ == '__main__':
    handle_io(sys.argv[1:])
