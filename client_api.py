from fastapi import FastAPI
import uvicorn 

from pydantic import BaseModel

import requests
import json 
from datetime import datetime

from comunicacaodados import *

app = FastAPI()

SERVER = 'http://18.191.148.32:8860'

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
    
    return DecryptItem(encrypted=encrypted, encoded=str(encoded), binary=str(binary), message=message)

@app.get("/encode/")
def decrypt(query: OnlyMessage):
    message = query.message
    encrypted = criptografia(query.message)
    binary = stringParaBits(encrypted)
    encoded = bitsParaAMI(binary)

    return DecryptItem(message=message, encrypted=encrypted, binary=str(binary), encoded=str(encoded))

if __name__ == "__main__":
    uvicorn.run("client_api:app", host="0.0.0.0", port=8000, log_level="info")
