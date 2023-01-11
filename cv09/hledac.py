"""
Implementujte program dle zadání úlohy 9. na elearning.tul.cz

Vytvořte program, který prohledá zadaný textový
soubor a nejde v něm řádky, na kterých se vyskytuje hledaný vzor. Případně více
vzorů. Tyto řádky pak vypíše na obrazovku a přidat k ním jejich čísla v původním
souboru.

Tak trochu se toto chování podobá unixovému příkazu grep, přesněji
řečeno grep -n.  Ten můžete případně použít pro kontrolu. Nicméně váš program
toho bude umět v mnoha ohledech méně a v jednom více (vyhledávání více vzorů
najednou). Nejde tedy o to vytvářet 100% kopii příkazu grep.

Program musí jít  ovládat z příkazové řádky. Základním parametrem zadávaným
vždy, je jméno souboru. Pokud jméno souboru není zadané program nemůže pracovat
a měl by v takovém případě zobrazit nápovědu.

Druhý parametr  parametr -s --search bude volitelný. Může být následován
libovolným počtem n slov. Samozřejmě, pokud je tam parametr -s musí tam být to
slovo alespoň jedno (tedy n >= 1).  Pokud není zadané hledané slovo, musí
program opět vypsat chybu nebo nápovědu.
 """

import sys
import argparse
import re


def find_lines(filename, search=None):
    """
    Returns line number and the line where the search matches
    in a dictionary, where key is the line number
    :param filename:
    :param search:
    :return:
    """
    if search is None:
        pattern = ".*"
    else:
        # building positive lookahead
        pattern = r"^"
        for word in search:
            pattern += "(?=.*\\b" + word + "\\b)"
        pattern += ".+"

    result = {}
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if re.search(pattern, line):
                result[i + 1] = line.rstrip()

    return result


def parse_args(args):
    """
    Parses command line arguments
    :return:
    """
    parser = argparse.ArgumentParser(description="It looks like grep, but it is not.")
    parser.add_argument('filename', type=str,
                        help="The input text file.")
    parser.add_argument('-s', '--search', type=str, required=False,
                        help="Words you are searching for. Must be 1 or more.")

    args = parser.parse_args(args)

    if args.filename is None:
        parser.error("The input text file must be specified.")

    if args.search is not None:
        args.search = args.search.split(" ")

    return args.filename, args.search


if __name__ == '__main__':
    PARSED = parse_args(sys.argv[1:])
    for number, content in find_lines(PARSED[0], PARSED[1]).items():
        print(f"%s:%s" % (number, content))
