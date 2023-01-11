import pytest

"""
Fixtures - příslušenství pro jednolitvé testy
"""


class Person():

    def greet(self):
        return "Hello"


@pytest.fixture
def person():
    return Person()


def test_greeting(person):
    greeting = person.greet()

    assert greeting == "Hello"
