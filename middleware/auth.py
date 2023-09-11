import json
from functools import wraps
from flask import jsonify, request

def read_account_json():
    with open('account_list.json', 'r') as f :
        data_temp = json.load(f)
        return data_temp

def check_access(f):
    @wraps(f)
    def procces_access(*args, **kwargs):
            authorize_access = request.headers.get('apikey')
            data_temps = read_account_json()

            if all(authorize_access != account['apikey'] for account in data_temps):
                return jsonify({'message': 'Apikey invalid !'}), 401

            return f(*args, **kwargs)
    return procces_access
