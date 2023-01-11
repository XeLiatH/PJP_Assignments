"""
A file containing functions that turn messed up html into
something more readable -> .json file

The functions are specially designed to match the Relay section
of result.html file
"""

import json
import re


def split_text(text):
    """
    Copied from the cv05.cestina.py file and removed the blank space
    """
    return re.compile(r'[^\t\n\r\f\v,.?!:/+()]+', re.MULTILINE).findall(text)


def strip_tags(html_data: str):
    """
    Stripts the html tags from a string
    """
    return re.sub(r'<[^<]+?>', '', str(html_data))


def read_json(filename: str):
    """
    Reads a .json file and returns it as a dictionary
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


def read_html_clean(filename: str):
    """
    Reads an .html file and returns it without the
    html tags
    """
    with open(filename, 'r', encoding="utf-8") as file:
        reached_relay = False
        for _, line in enumerate(file):
            clean = strip_tags(line).strip()
            if reached_relay:
                yield clean
            if clean.lower() == 'relay':
                reached_relay = True


def transform_html(filename: str):
    """
    Transforms .html file content into an array of
    desired values and yields it (generator)
    """
    row = read_html_clean(filename)
    while True:
        try:
            nxt = next(row)
            for res in re.compile(r'([0-9]+)\) ([A-Za-z ]+) ([0-9:]+) (\(.*?\))', re.MULTILINE) \
                    .findall(nxt):
                placement = int(res[0])
                time = res[2]
                people = split_text(res[3])
                for person in people:
                    name_parts = person.strip().split(" ")
                    yield [placement, time, name_parts[0], name_parts[1]]
        except StopIteration:
            break


def match_competitors(json_data, iterable_html: iter):
    """
    Matches the competitors from a given json with the
    transformed html content
    """
    result = []
    while True:
        try:
            competitor = next(iterable_html)
            firstname = competitor[2]
            lastname = competitor[3]
            for data in json_data:
                if data['firstname'] == firstname and data['lastname'] == lastname:
                    result.append({'id': data['id'], 'result': competitor[0],
                                   'time': competitor[1]})
                    break
            else:
                result.append({'id': False, 'result': competitor[0], 'time': competitor[1],
                               'no_match': str(firstname) + " " + str(lastname)})
        except StopIteration:
            break

    return result


def output_json(result_list):
    """
    Saves all the competitors into a .json file
    """
    with open('output.json', 'w') as output:
        output.write(json.dumps(result_list, indent=4, sort_keys=True))


def output_txt(result_list):
    """
    Saves the matched competitors into a .txt file sorted by their id
    """
    with open('compare.txt', 'w') as output:
        result_list_sorted = sorted(result_list, key=lambda k: int(k['id']) if k['id'] else 0)
        for result in result_list_sorted:
            if result['id']:
                output.write(str(result['id']) + " " + str(result['result']) + "\n")


def output_result():
    """
    Outputs the results into .json and .txt files
    """
    result = match_competitors(read_json('competitors.json'), transform_html('result.html'))
    output_json(result)
    output_txt(result)


if __name__ == '__main__':
    output_result()
