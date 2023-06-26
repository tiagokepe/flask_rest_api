from model.account import Account

class AccountsController:

    def __init__(self):
        self._accounts = {}

    def reset(self):
        self._accounts.clear()

    def get_balance(self, id: str):
        if id in self._accounts:
            return self._accounts.get(id).balance
        raise KeyError("Non-existing account.")

    def deposit(self, ac: Account):
        if self._accounts.get(ac.id) is None:
            self._accounts[ac.id] = ac
        else:
            self._accounts[ac.id].balance += ac.balance
        return self._accounts[ac.id]
