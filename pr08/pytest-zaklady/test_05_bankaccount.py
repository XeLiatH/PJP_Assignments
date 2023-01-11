"""
Ukázka použítí fixture nad třídou BankAccount
"""

import pytest
from bankaccount import BankAccount, InsufficientAmount


@pytest.fixture()
def start_ammount():
    """
    počátečním stav = 20000
    """
    return 20000


@pytest.fixture
def empty_account():
    """
    Vytvoří prázdný účet
    """
    return BankAccount()


@pytest.fixture
def account(start_ammount):
    """
    Vytvoří účet s počátečním stavem 20000

    Fixture může používat jinou fixture
    """
    return BankAccount(start_ammount)


def test_default_initial_amount(empty_account):
    assert empty_account.balance == 0


def test_setting_initial_amount(account, start_ammount):
    assert account.balance == start_ammount


def test_account_add_cash(account, start_ammount):
    account.add_cash(80)
    assert account.balance == start_ammount + 80


def test_account_spend_cash(account, start_ammount):
    account.spend_cash(10)
    assert account.balance == start_ammount - 10


def test_account_spend_cash_raises_exception_on_insufficient_amount(empty_account):
    with pytest.raises(InsufficientAmount):
        empty_account.spend_cash(100)
