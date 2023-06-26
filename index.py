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

