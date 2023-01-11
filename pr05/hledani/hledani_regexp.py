# -*- coding: utf-8 -*-
'''
ukazka hledani pomoci Regularnich vyrazu
'''

import re
import futils

def show_match(line):
    '''
    match hleda od zacatku
    '''
    match = re.match(r'[^c]+class=[\'\"]([^\'\"]+)', line)
    return match


def show_search(line):
    '''
    search prohledava retezec
    '''
    match = re.search(r'class=[\'\"]([^\'\"]+)', line)
    return match


def show_all(line):
    '''
    findall  prohledava retezec a vraci rovnou pole
    '''
    vsechny = re.findall(r'class=[\'\"]([^\'\"]+)', line)
    return vsechny


def show_tag(line):
    '''
    match pro HTML tag
    '''
    tag = re.match('(<[^>]+>)', line)
    return tag


def show_compile():
    '''
    kompilovane vyrazy jsou vyborne pro opakovane hledani
    '''

    compiled = re.compile(r'class=[\'\"]([^\'\"]+)')
    return compiled


def parse_lines(data):
    '''
    prohleda html string
    '''
    pat = show_compile()
    return [pat.findall(line) for line in data if pat.findall(line)]



if __name__ == '__main__':
    data = futils.get_line_list('aktualne.html')
    print(parse_lines(data))
    