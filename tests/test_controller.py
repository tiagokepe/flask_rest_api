import pytest

from model.account import Account
from control.accounts_controller import AccountsController

@pytest.mark.smoke
def test_new_account():
    assert pytest.my_controller.add_account(Account(id='100', balance=10)) is None
    assert pytest.my_controller.add_account(Account(id='300', balance=0)) is None

@pytest.mark.smoke
def test_deposit():
    assert pytest.my_controller.deposit(Account(id='100', balance=10))
    assert pytest.my_controller.get_balance('100') == 20

@pytest.mark.smoke
def test_withdraw_non_existing():
    with pytest.raises(KeyError):
        pytest.my_controller.withdraw(Account(id='200', balance=10))
        
@pytest.mark.smoke
def test_withdraw():
    assert pytest.my_controller.withdraw(Account(id='100', balance=5))
    assert pytest.my_controller.get_balance('100') == 15
    
@pytest.mark.smoke
def test_transfer():
    assert pytest.my_controller.transfer(Account(id='100', balance=15), Account(id='300'))
    assert pytest.my_controller.get_balance('100') == 0
    assert pytest.my_controller.get_balance('300') == 15
    
@pytest.mark.smoke
def test_transfer_non_existing():
    with pytest.raises(Exception):
        assert pytest.my_controller.transfer(Account(id='200', balance=15), Account(id='300'))