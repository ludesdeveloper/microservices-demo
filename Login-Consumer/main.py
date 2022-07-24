from flask import Flask, request
import requests
import json
import os
import jwt

KONG_ADMIN_URL = os.environ['KONG_ADMIN_URL']

def get_username(username):
    url = f"{KONG_ADMIN_URL}/consumers/{username}/jwt"
    response = requests.request("GET", url)
    return response.text

def create_jwt(username, secret, key):
    secret = secret 
    key = key 
    encoded = jwt.encode({
    "name": username,
    "exp": 1900000000,"iss": key 
    }, secret, algorithm="HS256")
    return encoded

app = Flask(__name__)

@app.route("/login-consumer", methods = ['POST'])
def login_consumer():
    data = request.get_json()
    username = data['username']
    password = data['password']
    check_password = json.loads(get_username(username))
    for i in check_password['data']:
        if password == i['secret']:
            secret = i['secret']
            key = i['key']
            jwt = create_jwt(username,secret,key)
            break
    return jwt 

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)