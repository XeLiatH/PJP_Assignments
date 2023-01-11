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
    return my_mock
    

@pytest.mark.parametrize("mock_get_result, expected_result", [
    ({"status": 200, "data":{"key": "value"}}, True),
    ({"status": 403}, False)
    ])
def test_app_refresh_behaves_correctly(mock_api, mock_get_result, expected_result):
    """
    i pro mock objekty můžeme bez problémů použít parametrizaci
    """
    my_app = App("http://www.example.com/", mock_api)
    mock_api.get.return_value = mock_get_result
    assert my_app.refresh_data() == expected_result


   

