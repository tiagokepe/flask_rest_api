from model.account import Account

class AccountsController:

    def __init__(self):
        self._accounts = {}

    def reset(self):
        self._accounts.clear()

    def add_account(self, ac: Account):
        if ac.id in self._accounts:
            raise Exception("Account already exist.")
        self._accounts[ac.id] = ac

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

    def withdraw(self, ac: Account):
        if ac.id not in self._accounts:
            raise KeyError("Non-existing account.")
        self._accounts[ac.id].balance -= ac.balance
        return self._accounts[ac.id]
        
    def transfer(self, origin: Account, destination: Account):
        if origin.id not in self._accounts:
            raise KeyError("Non-existing account: %s." % origin.id)
        self._accounts[origin.id].balance -= origin.balance
        
        if destination.id not in self._accounts:
            self._accounts[destination.id] = destination
            # raise KeyError("Non-existing account: %d." % destination.id)
        self._accounts[destination.id].balance += origin.balance
    
        return self._accounts[origin.id], self._accounts[destination.id]
