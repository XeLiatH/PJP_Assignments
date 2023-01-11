"""
Ukázka kombinace parametrických testů i fixtures nad třídou BankAccount
""" 

import pytest
from bankaccount import BankAccount, InsufficientAmount


@pytest.fixture
def my_account():
    '''Returns a Wallet instance with a zero balance'''
    return BankAccount()

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(my_account, earned, spent, expected):
    my_account.add_cash(earned)
    my_account.spend_cash(spent)
    assert my_account.balance == expected