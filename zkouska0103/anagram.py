"""
Module for finding anagrams
"""

import itertools


def word_filter(word, word_list: list):
    """
    Filters only the words from the word list, that start with any letter of the
    given word
    :param word: string
    :param word_list: list
    :return: dictionary
    """

    filtered = {}
    for letter in list(word):
        for eng_word in word_list:
            if eng_word.startswith(letter):
                filtered[eng_word] = sorted(list(eng_word))
    return filtered


def find_full_anagram(word, words: dict):
    """
    Tries to find all one worded anagrams
    :param word: string
    :param words: dictionary
    :return: generator
    """

    word_sorted = sorted(list(word))
    for key, value in words.items():
        if value == word_sorted and key != word:
            yield key


def find_multiple_anagrams(word, words: dict):
    """
    Tries to find all two worded anagrams
    :param word: string
    :param words: dictionary
    :return: generator
    """

    # todo: takes too long

    generated = []
    for combination in set(itertools.permutations(sorted(list(word)), len(word))):
        combination = ''.join(combination)
        for i in range(0, len(combination)):
            sub1 = combination[:i]
            sub2 = combination[i:]
            if sub1 in words.keys() and sub2 in words.keys() \
                    and '{} {}'.format(sub2, sub1) not in generated:
                yield '{} {}'.format(sub1, sub2)
                generated.append('{} {}'.format(sub1, sub2))


def get_anagrams(word):
    """
    Returns all possible anagrams for the given word
    :param word: string
    :return: list of all the anagrams, empty if none found
    """

    eng_words = []
    with open('brit-a-z.txt', 'r', encoding="utf-8") as file:
        for line in file:
            eng_words.append(line.rstrip())

    valid_words = word_filter(word, eng_words)

    anagrams = []
    for anagram in find_full_anagram(word, valid_words):
        anagrams.append(anagram)

    for anagram in find_multiple_anagrams(word, valid_words):
        anagrams.append(anagram)

    return anagrams


if __name__ == '__main__':
    # rychlý
    print(get_anagrams("lumber"))
    # pomalý
    ABRIDGE = get_anagrams("abridgement")
    print(len(ABRIDGE))
    print(ABRIDGE)
