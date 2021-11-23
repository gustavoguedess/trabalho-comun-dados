from fastapi import FastAPI
import uvicorn 

from pydantic import BaseModel

app = FastAPI()

messages_list = []

class MessageItem(BaseModel):
    dest_name: str
    origin_name: str
    message: str
    date: str

@app.get("/")
def read_root():
    return {"Server": "On"}

@app.post("/send/")
def send(message: MessageItem):
    messages_list.append(message)
    return {"Status":"Ok"}

@app.get("/listen/{name}")
def listen(name: str):
    message = None
    for msg in messages_list:
        if msg.dest_name==name:
            message = msg
            break 
    if not message:
        return None

    messages_list.remove(message)
    return message

@app.get("/all")
def all():
    return {'messages':messages_list}


if __name__ == "__main__":
    uvicorn.run("server_api:app", host="0.0.0.0", port=8860, log_level="info")
