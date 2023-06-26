from flask import Flask, jsonify, request
import json

from model.account import Account
from model.events import Deposit, Withdraw, Transfer
from control.accounts_controller import AccountsController

app = Flask(__name__)

ac_controller = AccountsController()

@app.route('/reset', methods=['POST'])
def reset():
    ac_controller.reset()
    return "OK", 200

@app.route('/balance', methods=['GET'])
def get_balance():
    try:
        balance = ac_controller.get_balance(request.args.get('account_id'))
        return str(balance), 200
    except KeyError:
        return "0", 404

@app.route('/event', methods=['POST'])
def handle_event():
    event = request.get_json()
    if event['type'] == 'deposit':
        account = ac_controller.deposit(Account(id=event['destination'], balance=event['amount']))
        return json.dumps({"destination": account.dict()}), 201

    if event['type'] == 'withdraw':
        try:
            account = ac_controller.withdraw(Account(id=event['origin'], balance=event['amount']))
            return json.dumps({"origin": account.dict()}), 201
        except KeyError:
            return "0", 404

    if event['type'] == 'transfer':
        try:
            orig_ac = Account(id=event['origin'], balance=event['amount'])
            dest_ac = Account(id=event['destination'])
            orig_ac, dest_ac = ac_controller.transfer(orig_ac, dest_ac)
            return json.dumps({"origin": orig_ac.dict(), "destination": dest_ac.dict()}), 201
        except KeyError:
            return "0", 404

    return "Unrecognized event", 501
