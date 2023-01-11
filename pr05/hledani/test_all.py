import hledani_parser
import hledani_regexp
import hledani_retezec
import hledani_bs4
import futils
import pytest

@pytest.fixture
def text_data():
    return futils.get_text('aktualne.html')

@pytest.fixture
def expected_result():
    return ['hlavni', 'monkey', 'odstavec', 'zelena modra', 'ctvrty', 'extra']

@pytest.fixture
def list_data():
    return futils.get_line_list('aktualne.html')


def test_parser(text_data, expected_result):
    result = hledani_parser.parse_html(text_data)
    assert result == expected_result


def test_regex(list_data, expected_result):
    result = hledani_regexp.parse_lines(list_data)
    assert result == expected_result


def test_retezec(list_data, expected_result):
    result = hledani_retezec.search_for_str(list_data)
    assert result == expected_result


def test_bs4(text_data, expected_result):
    result = hledani_bs4.parse_html(text_data)
    assert result == expected_result    