import json
import random
from flask import Blueprint, jsonify, request

registers_account = Blueprint('registers_account', __name__)

def read_temp():
    with open('account_list.json', 'r') as f:
        data_temp = json.load(f)
        return data_temp

def write_temp(data):
    with open('account_list.json', 'w') as f:
        json.dump(data, f, indent=4)

def create_apikey(max_length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    length = random.randint(1, max_length)
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

    
@registers_account.route('/register', methods=['POST'])
def register_procces():
    try: 
        data_r = request.get_json()

        username = data_r.get('username')
        password = data_r.get('password')
        apikey = create_apikey(16)

        temps_data = read_temp()

        if any(temp_data['username'] == username for temp_data in temps_data):
                return jsonify({'message': 'Username Sudah Di Pakai'})

        data_s = { 'username': username, 'password': password, 'apikey': apikey }
        temps_data.append(data_s)
        write_temp(temps_data)

        return jsonify({'message': 'Data berhasil Ditambahkan'})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 501
