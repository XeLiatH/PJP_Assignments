"""
Testy pro modul censor.py
"""

import pytest
import censor


def test_censor():
    text = 'This is some text to be censored'
    char = '#'
    banned_words = ['is', 'censored']
    result = 'This ## some text to be ########'
    assert censor.censor(char, text, banned_words) == result


def test_transform():
    word = 'red'
    char = '#'
    transformed = '###'
    assert censor.transform_word(char, word) == transformed


def test_strip_tags():
    html = '<p>Tohle je test</p>'
    text = 'Tohle je test'
    assert censor.strip_tags(html) == text


def test_split_words():
    text = 'Tohle je test'
    result = ['Tohle', 'je', 'test']
    assert censor.split_text(text) == result


def test_no_argument():
    with pytest.raises(SystemExit):
        censor.parse_args([])


def test_toomany_arguments():
    with pytest.raises(SystemExit):
        censor.parse_args(['Sdfsdf', 'sfsdfs', 'dgfdgdfg'])


def test_empty_option():
    with pytest.raises(SystemExit):
        censor.parse_args(['-i', ])


def test_unknown_option():
    with pytest.raises(SystemExit):
        censor.parse_args(['-s', 'test'])


def test_invalid_option():
    with pytest.raises(TypeError):
        censor.parse_args(['-i', 1, '-l', 'list'])


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        censor.handle_io(['-i', 'test.html', '-l', 'list'])


def test_invalid_files():
    with pytest.raises(FileNotFoundError):
        censor.handle_io(['-i', 'data_test.html', '-l', 'list.txt'])


def test_valid_files():
    assert censor.handle_io(['-i', 'data_test.html', '-l', 'list_test.txt']) == 0


def test_valid_files_output_file():
    assert censor.handle_io(['-i', 'data_test.html', '-l', 'list_test.txt', '-c', '-o', 'pytest.txt']) == 1
