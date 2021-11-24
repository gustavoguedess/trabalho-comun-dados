import requests
from datetime import datetime

from comunicacaodados import *

import matplotlib.pyplot as plt
import numpy as np


SERVER = 'http://18.191.148.32:8860'

def send(origin_username:str, dest_username:str, message: str):

    date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
    
    message = {
        "dest_name":dest_username, 
        "origin_name":origin_username, 
        "message":message, 
        "date":date
    }

    
    return requests.post(f'{SERVER}/send/', json=message).json()

def listen(name: str):
    msg = requests.get(f'{SERVER}/listen/{name}').json()
    return msg

def decode(message):
    encoded = list(map(int, message.strip('][').split(', ')))
    binary = AMIParaBits(encoded)
    encrypted = bitsParaString(binary)
    message = descriptografia(encrypted)
    
    res = {
        'encrypted':encrypted, 
        'encoded':str(encoded), 
        'binary':str(binary), 
        'message':message
    }

    return res

def encode(message):
    encrypted = criptografia(message)
    binary = stringParaBits(encrypted)
    encoded = bitsParaAMI(binary)

    res = {
        'message': message, 
        'encrypted': encrypted, 
        'binary': str(binary), 
        'encoded': str(encoded)
    }
    return res

def graph(data):
    data.insert(len(data),0) # adds zero to fully draw the last bit on the graphic (not necessary, it just looks better)
    y = data
    x = np.arange(len(data))

    fig = plt.figure(figsize=(10,2),dpi=150)

    ax = fig.add_subplot()

    ax.plot(x, y, drawstyle="steps-post", linewidth=2.0)

    ax.set_yticks([-1,0,1])
    ax.set_yticklabels(['-V',0,'+V'])
    ax.set_title('Forma da onda - AMI')

    x_major_ticks = np.arange(-1, len(data)+1, 5)
    x_minor_ticks = np.arange(-1, len(data)+1, 1)

    ax.set_xticks(x_major_ticks)
    ax.set_xticks(x_minor_ticks, minor=True)

    ax.grid(which='major', axis='x', linestyle='--')
    ax.grid(which='minor', axis='x', linestyle='--')
    ax.grid(which='major', axis='y', linestyle='-', alpha=0.7)

    plt.savefig("grafico.png")
    data.pop() # removes the zero added at the start
