import pytest

from bank import Account

@pytest.fixture
def account():
    return  Account(initial_balance=1000)

def test_deposit(account):

    account.deposit(1000)
    assert account.balance==2000


def test_withdraw(account):

    account.withdraw(amount=500)
    assert account.balance == 500


def test_withdraw_error():
    account=Account(initial_balance=200)

    with pytest.raises(ValueError):
      account.withdraw(500)


def test__create_identifier(account):

    assert len(account.identifier)!=0
