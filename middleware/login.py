import json
from flask import Blueprint, jsonify, request

def read_temp():
    with open('account_list.json', 'r') as f:
        data_temp = json.load(f)
        return data_temp

login_procces = Blueprint('login_procces', __name__)

@login_procces.route('/login', methods=['POST'])
def login_auth():
    try : 
        
        data_r = request.get_json()
        
        apikey = data_r.get('apikey')

        temps_data = read_temp()
        if any(temp_data['apikey'] == apikey for temp_data in temps_data):
           username = next(temp_data['username'] for temp_data in temps_data if temp_data['apikey'] == apikey)
           return jsonify({'message': 'Auth Apikey Ditemukan !', 'username': username, 'apikey': apikey})
           
        return jsonify({'message': 'Auth Apikey Not Found.'})
        
    except Exception as e: 
        return jsonify({'error': str(e)})
