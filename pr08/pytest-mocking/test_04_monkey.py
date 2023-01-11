"""
Mocking objektů pomocí modulu unittest a třídy Mock
https://docs.python.org/3/library/unittest.mock.html
"""

import pytest
from unittest.mock import Mock

from code_03 import WebApi, App

@pytest.fixture()
def mock_api():
    my_mock = Mock(spec=WebApi)
    my_mock.get.return_value = {"status": 200, "data":{"key": "value"}}

    return my_mock


def test_app_refresh_get_result(monkeypatch, mock_api):
    """
    monkeypatch je pytest built in fixture
    umožňuje modifikovat existující objekt v průběhu testu
    """
    API = Mock(return_value=mock_api)
    monkeypatch.setattr('code_03.WebApi', API)
    my_app = App("http://www.example.com/")
    
    assert my_app.refresh_data() == True


def test_app_refresh_do_not_get_result(monkeypatch, mock_api):
    API = Mock(return_value=mock_api)
    monkeypatch.setattr('code_03.WebApi', API)
    my_app = App("http://www.example.com/")
    mock_api.get.return_value = {"status": 403}
    assert my_app.refresh_data() == False
   
   

