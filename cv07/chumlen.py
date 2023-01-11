# -*- coding: utf-8 -*-

"""
Cvičení 7. - práce s daty

Vaším dnešním úkolem je spojit dohromady data, uložená ve dvou různých
souborech. První soubor obsahuje výsledky závodu - jména a časy závodníků. Druhý
pak obsahuje databázi závodníků uloženou jako JSON - mimo jiné jejich id. Cílem
je vytvořit  program, který tyto data propojí, tedy ke každému závodníkovi ve
štafetě najde jeho id. Případně také nenajde, data nejsou ideální. I tuto
situaci ale musí program korektně ošetřit.  Výsledky programu bude potřeba
zapsat do dvou souborů.

Kompletní zadání je jako vždy na https://elearning.tul.cz/

"""
import re
import json


def name2id(dict_list):
    """
    matches names from dict_list with database of competitors and returns desired format
    """
    with open("competitors.json", encoding="utf8") as json_file:
        json_data = json.load(json_file)
    for record in dict_list:
        name = record['name'].split(" ")
        for data in json_data:
            if name[0] == data['firstname'] and name[1] == data['lastname']:
                record['id'] = data['id']
        if not record['id'] and 'no_match' not in record.keys():
            record['no_match'] = record['name']
        record.pop('name')
    return dict_list


def parse_results():
    """
    Parses html into list of dictionaries
    """
    with open("result.html") as results:
        results_list = results.readlines()

    regex = re.compile(r'[0-9]\)')
    relev = [regex.split(res) for res in results_list if "(" in res and "Length" not in res]
    list_rc = []

    for line in relev:
        place = 1
        for record in line:
            timestamp = re.findall(r'[0-9]:[0-9][0-9]:[0-9][0-9]', record)
            names = re.findall(r'\(.*\)', record)
            if names:
                names = names[0].split(",")
                dct = [dict({
                    'id': False,
                    'name': name.strip(" ").replace("(", "").replace(")", ""),
                    'time': timestamp[0],
                    'result': place
                }) for name in names]
                place += 1
                list_rc = list_rc + dct
    return list_rc


def output_json(result_list):
    """
    Uloží list slovníků do souboru output.json tak jak je požadováno
    v zadání.
    """
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def output_txt(result_list):
    """
    Saves results as plain text file
    """
    with open('compare.txt', 'w') as output:
        result_list_sorted = sorted(result_list, key=lambda k: k['id'])
        for res in result_list_sorted:
            if res['id']:
                output.write(str(res['id']) + " " + str(res['result']) + "\n")


if __name__ == '__main__':
    output_json(name2id(parse_results()))
    output_txt(name2id(parse_results()))
