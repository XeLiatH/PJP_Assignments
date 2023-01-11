"""
Ukázka použítí parametrických testů nad třídou BankAccount
"""
import pytest
from bankaccount import BankAccount, InsufficientAmount


@pytest.mark.parametrize("earned, spent, expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(earned, spent, expected):
    my_account = BankAccount()
    my_account.add_cash(earned)
    my_account.spend_cash(spent)
    assert my_account.balance == expected