import os
import json
from multiprocessing import connection
from flask import Flask, request
import pika

RABBIT_USER = str(os.environ['RABBIT_USER'])
RABBIT_PASSWORD = str(os.environ['RABBIT_PASSWORD'])
RABBIT_URL = os.environ['RABBIT_URL']
RABBIT_PORT = os.environ['RABBIT_PORT']

def sent_queue(data):
    credentials = pika.PlainCredentials(
        RABBIT_USER, RABBIT_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL,
                                                                RABBIT_PORT,
                                                                '/',
                                                                credentials))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=json.dumps(data))
    print(data)
    connection.close()

app = Flask(__name__)

@app.route("/get-request", methods = ['POST'])
def get_request():
    data = request.get_json()
    sent_queue(data)
    return data

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)