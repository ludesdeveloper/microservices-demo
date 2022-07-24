import sys
import os
import json
import pika
import psycopg2

POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']

conn = psycopg2.connect(database=POSTGRES_DB, user = POSTGRES_USER, password = POSTGRES_PASSWORD, host = POSTGRES_HOST, port = POSTGRES_PORT)
print("Opened database successfully")
cur = conn.cursor()
try:
    cur.execute('''CREATE TABLE COMPANY
        (ID SERIAL PRIMARY KEY,
        NAME           TEXT    NOT NULL,
        ADDRESS        CHAR(50));''')
    print("Table created successfully")
except:
    print("Table already created")
conn.commit()
conn.close()

RABBIT_USER = str(os.environ['RABBIT_USER'])
RABBIT_PASSWORD = str(os.environ['RABBIT_PASSWORD'])
RABBIT_URL = os.environ['RABBIT_URL']
RABBIT_PORT = os.environ['RABBIT_PORT']

def main():
    credentials = pika.PlainCredentials(
        RABBIT_USER, RABBIT_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL,
                                                                RABBIT_PORT,
                                                                '/',
                                                                credentials))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        data_to_db = json.loads(body)
        conn = psycopg2.connect(database="mydb", user = "postgres", password = "postgresSuperUserPsw", host = "mypostgres", port = "5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO COMPANY (NAME, ADDRESS) VALUES (%s, %s)", (data_to_db['Name'], data_to_db['Address']));
        conn.commit()
        print("Records created successfully")
        conn.close()

    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
