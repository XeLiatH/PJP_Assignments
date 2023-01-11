"""
Implementuje program dle zadání úlohy 10. na elearning.tul.cz
"""

import re
import sys
import requests
import json
from bs4 import BeautifulSoup, Comment


def get_emails(url, smap):
    """
    Returns all emails for given url and sitemap
    """

    mails_per_file = {}
    for file in smap.keys():
        emails = []
        text = get_text(url + file)

        # in plain text
        plain = find_mails(text)
        if plain:
            emails = emails + plain

        # hypertext
        links = find_links(text)
        for link in links:
            if link.startswith("mailto"):
                emails.append(link)

        # comments
        comments = find_comments(text)
        for comment in comments:
            mails = find_mails(comment)
            if mails:
                emails = emails + mails

        mails_per_file[file] = pure(emails)

    return mails_per_file


def sitemap(url, file=None, smap=None, remaining=None, discarded=None):
    """
    Returns a dictionary sitemap for a give url
    """

    # Set default values
    if smap is None:
        smap = {}

    if remaining is None:
        remaining = set()

    if discarded is None:
        discarded = set()

    if file is None:
        file = 'index.html'

    discarded.add(file)

    if not url.endswith('/'):
        url = url + '/'

    text = get_text(url + file)

    links = find_links(text)
    for link in links:
        if link.startswith("mailto"):
            continue
        if link.startswith("http") and not is_same_origin(url, link):
            continue
        if link in discarded:
            continue
        remaining.add(link)

    if links:
        smap[file] = list(set(remaining))

    while remaining:
        next_file = remaining.pop()
        sitemap(url, next_file, smap, remaining, discarded)

    return smap


def pure(emails):
    """
    Purify all emails from anti spam measures and return only unique results
    """

    rules = {
        'mailto:': '',
        '#': '@',
        '--REMOVE-IF-YOU-ARE-NOT-S-P-A-M-E-R': '',
        '---NO---SPAM---': '',
        '//': '',
    }

    trimmed = []
    for email in emails:
        trim = email
        for rule, replace in rules.items():
            trim = trim.replace(rule, replace)
        trimmed.append(trim.strip())
    return list(set(trimmed))


def find_mails(text):
    """
    Finds e-mail addresses in a plain text
    """
    return re.findall(r'[\w.-]+@[\w.-]+', text)


def find_links(text):
    """
    Finds all hypertext links from html feed
    """
    links = []
    for link in BeautifulSoup(text, 'html.parser').find_all('a'):
        links.append(link['href'])
    return links


def find_comments(text):
    """
    Finds all comments from html feed
    """
    return BeautifulSoup(text, 'html.parser') \
        .find_all(string=lambda text: isinstance(text, Comment))


def is_mail(string):
    """
    Determines whether an input string is a valid e-mail address
    """
    return re.match(r"^[A-Za-z0-9.+_-]+@[A-Za-z0-9._-]+\.[a-zA-Z]*$", string)


def is_same_origin(base_url, url):
    """
    Determines whether given url is from the same domain
    """
    return base_url in url


def is_full_address(url):
    """
    Determines whether given url is a full address
    Basically if it starts with http or not
    """
    return re.match(r'^http', url)


def get_text(url):
    """
    Return the text content from a given url
    """
    if not is_full_address(url):
        url = "http://" + url

    return requests.get(url).text


def main():
    """
    Entry point for this program
    """
    try:
        url = sys.argv[1]
    except IndexError:
        url = "http://www.nti.tul.cz/~vrany/pjp_data/"

    smap = sitemap(url)
    files_and_emails = get_emails(url, smap)

    with open('scrap_result.txt', 'w') as file:

        output = json.dumps(smap, indent=4)
        output2 = re.sub(r'": \[\s+', '": [', output)
        output3 = re.sub(r'",\s+', '", ', output2)
        output4 = re.sub(r'"\s+\]', '"]', output3)

        file.write(output4)
        file.write("\n")
        file.write("\n")
        for _, value in files_and_emails.items():
            for email in value:
                file.write(email + "\n")

    print("E-mails successfully scraped!")


if __name__ == '__main__':
    main()
