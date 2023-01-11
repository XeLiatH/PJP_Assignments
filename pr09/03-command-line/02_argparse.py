# -*- coding: UTF-8 -*-
'''
Argparse demo
@author: Jiri Vrany
'''

import argparse


def main_solver(input_file, output_file, trim):
    '''
    hlavni aplikacni logika - vyresi zadanou ulohu
    '''
    print(locals())


def parse_args():
    '''
    zpracuje argumenty prikazove radky
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="input file name")
    parser.add_argument("-o", "--output", help="output file name")
    parser.add_argument("-t", "--trim",
                        help="trim lines", action="store_true")
    args = parser.parse_args()

    if args.input is None:
        parser.error("nemuzu pracovat bez vstupniho souboru")

    main_solver(args.input, args.output, args.trim)

if __name__ == '__main__':
    parse_args()
