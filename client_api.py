from fastapi import FastAPI
import uvicorn 

from pydantic import BaseModel

import requests
import json 
from datetime import datetime

from comunicacaodados import *


import matplotlib.pyplot as plt
import numpy as np

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

SERVER = 'http://18.191.148.32:8860'

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageItem(BaseModel):
    dest_name: str
    origin_name: str
    message: str
    date: str

class DecryptItem(BaseModel):
    encrypted: str
    binary: str
    encoded: str
    message: str

class OnlyMessage(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"Server": "On"}

@app.post("/send/{origin_username}/{dest_username}")
def send(origin_username:str, dest_username:str, msg: OnlyMessage):

    date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 
    
    message = {
        "dest_name":dest_username, 
        "origin_name":origin_username, 
        "message":msg.message, 
        "date":date
    }

    
    return requests.post(f'{SERVER}/send/', json=message).json()

@app.get("/listen/{name}")
def listen(name: str):
    msg = requests.get(f'{SERVER}/listen/{name}').json()
    return msg

@app.get("/decode/")
def decrypt(query: OnlyMessage):
    encoded = list(map(int, query.message.strip('][').split(', ')))
    binary = AMIParaBits(encoded)
    encrypted = bitsParaString(binary)
    message = descriptografia(encrypted)
    
    graph(encoded)
    
    return DecryptItem(encrypted=encrypted, encoded=str(encoded), binary=str(binary), message=message)

@app.get("/encode/")
def decrypt(query: OnlyMessage):
    message = query.message
    encrypted = criptografia(query.message)
    binary = stringParaBits(encrypted)
    encoded = bitsParaAMI(binary)

    return DecryptItem(message=message, encrypted=encrypted, binary=str(binary), encoded=str(encoded))


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


if __name__ == "__main__":
    uvicorn.run("client_api:app", host="0.0.0.0", port=8000, log_level="info")
