"""

implementujte testy pro program hledac.py

pokrytí kódu musí být minimálně 75%
"""

import hledac
import pytest


def test_no_argument():
    with pytest.raises(SystemExit):
        hledac.parse_args([])


def test_toomany_arguments():
    with pytest.raises(SystemExit):
        hledac.parse_args(['Sdfsdf', 'sfsdfs', 'dgfdgdfg'])


def test_empty_option():
    with pytest.raises(SystemExit):
        hledac.parse_args(['lipsum.txt', '-s', ])


def test_invalid_option():
    with pytest.raises(TypeError):
        hledac.parse_args(['lipsum.txt', '-s', 1])


def test_valid_option_single():
    parsed = hledac.parse_args(['lipsum.txt', '-s', 'test'])
    assert parsed == ('lipsum.txt', ['test'])


def test_valid_option_multiple():
    parsed = hledac.parse_args(['lipsum.txt', '-s', 'test testing testing some more'])
    assert parsed == ('lipsum.txt', ['test', 'testing', 'testing', 'some', 'more'])


def test_invalid_file():
    with pytest.raises(FileNotFoundError):
        hledac.find_lines('stre')


def test_valid_file_all():
    result = hledac.find_lines('lipsum.txt')
    assert len(result) == 155


def test_valid_file_some():
    result = hledac.find_lines('lipsum.txt', ['dolor', 'amet'])
    assert len(result) == 4
