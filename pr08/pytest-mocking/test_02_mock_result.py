"""
Mocking objektů pomocí modulu unittest a třídy Mock
https://docs.python.org/3/library/unittest.mock.html
"""

import pytest
from unittest.mock import Mock

from code_02 import WebApi, App


@pytest.fixture()
def mock_api():
    my_mock = Mock(spec=WebApi)
    my_mock.get.return_value = {"status": 200, "data": {"key": "value"}}

    return my_mock


def test_app_calls_api(mock_api):
    """
    smyslem unit testu pro App není zjistit, jestli WebApi funguje jak má
    chceme jen vědět, že ho aplikace zavolá jak má
    """
    my_app = App("http://www.example.com/", mock_api)
    my_app.refresh_data()
    mock_api.get.assert_called()


def test_app_calls_api_with_correct_address(mock_api):
    """
    smyslem unit testu pro App není zjistit, jestli WebApi funguje jak má
    chceme jen vědět, že ho aplikace zavolá jak má
    """
    test_url = "http://www.example.com/"
    my_app = App(test_url, mock_api)
    my_app.refresh_data()
    mock_api.get.assert_called_with(test_url)    


def test_app_refresh_get_result(mock_api):
    """
    smyslem unit testu pro App není zjistit, jestli WebApi funguje jak má
    chceme jen vědět, že aplikace zpracuje výsledek tak jak má 
    proto si v mock objektu přípravíme výsledek přesně tak jak potřebujeme
    """
    my_app = App("http://www.example.com/", mock_api)
    
    assert my_app.refresh_data() == True


def test_app_refresh_do_not_get_result(mock_api):
    """
    smyslem unit testu pro App není zjistit, jestli WebApi funguje jak má
    chceme jen vědět, že aplikace zpracuje výsledek tak jak má 
    proto si v mock objektu přípravíme výsledek přesně tak jak potřebujeme
    """
    
    my_app = App("http://www.example.com/", mock_api)
    mock_api.get.return_value = {"status": 403}
    assert my_app.refresh_data() == False
   
   

