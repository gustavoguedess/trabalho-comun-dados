import requests 
from threading import Thread
from datetime import datetime
import json 

SERVER = 'http://18.191.148.32:8860'
name = input('Digite seu usuario: ')


def listen():
    while True:
        msg = requests.get(f"{SERVER}/listen/{name}").text
        if msg!='null':
            msg = json.loads(msg)
            print(f"{msg['origin_name']}: {msg['message']}")
[]
def encrypt(str):
    return str

def send_message(msg, dest_name):
    message = {}

    msg = encrypt(msg)
    message['dest_name'] = dest_name
    message['origin_name'] = name
    message['message'] = msg
    message['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 

    requests.post(f"{SERVER}/send", json=message)

t = Thread(target=listen)
t.daemon = True
t.start()

dest_name = input("Destino: ")
while True:
    msg = input()
    send_message(msg, dest_name)
