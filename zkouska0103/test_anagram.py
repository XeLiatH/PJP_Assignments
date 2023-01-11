"""
The anagram test file
"""

import anagram


def test_filter_words():
    word = 'ab'
    word_list = ['abd', 'bca', 'comb', 'dem']

    assert anagram.word_filter(word, word_list) == {'abd': ['a', 'b', 'd'], 'bca': ['a', 'b', 'c']}


def test_find_full_anagram():
    word = 'abc'
    valid_words = {'abd': ['a', 'b', 'd'], 'bca': ['a', 'b', 'c']}

    count = 0
    anagrams = anagram.find_full_anagram(word, valid_words)
    for an in anagrams:
        count += 1
        assert an == 'bca'

    assert count == 1


def test_find_multiple_anagrams():
    word = 'abc'
    valid_words = {'abd': ['a', 'b', 'd'], 'bca': ['a', 'b', 'c'], 'a': ['a'], 'bc': ['b', 'c']}

    count = 0
    anagrams = anagram.find_multiple_anagrams(word, valid_words)
    for an in anagrams:
        count += 1
        assert an == 'a bc' or an == 'bc a'

    assert count == 1


def test_get_anagrams():
    word = 'lumber'
    expected = 6

    assert len(anagram.get_anagrams(word)) == expected
