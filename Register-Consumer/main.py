from flask import Flask, request
import requests
import json
import os

KONG_ADMIN_URL = os.environ['KONG_ADMIN_URL']

def create_consumer(username):
    url = f"{KONG_ADMIN_URL}/consumers"
    payload={'username': username}
    response = requests.request("POST", url, data=payload)
    return response.text

def create_jwt(username, password):
    url = f"{KONG_ADMIN_URL}/consumers/{username}/jwt"
    payload={'secret': password}
    response = requests.request("POST", url, data=payload)
    return response.text


app = Flask(__name__)

@app.route("/register-consumer", methods = ['POST'])
def register_consumer():
    data = request.get_json()
    username = data['username']
    password = data['password']
    check_consumer = create_consumer(username)
    check_consumer = json.loads(check_consumer)
    try:
        print(check_consumer['id'])
        print(create_jwt(username, password))
    except:
        pass
    return data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)