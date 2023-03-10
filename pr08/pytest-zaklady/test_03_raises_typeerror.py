# test_capitalize.py

import pytest

def capital_case(x):
    try:
        return x.capitalize()
    except AttributeError:
        raise TypeError("only string can be capitalized")    

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)    