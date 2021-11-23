from typing import Optional
from fastapi import FastAPI
import uvicorn 

app = FastAPI()

messages_list = []

@app.get("/")
def read_root():
    return {"Server": "On"}

@app.get("/send_message/")
def send_message():
    return {"Hello": "World"}

@app.get("/listen/{name}")
def listen(name: str):
    message = None
    for msg in messages_list:
        if msg['dest_name']==name:
            message = msg
            break 
    if not message:
        return None

    messages_list.remove(message)
    return message

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run("server_api:app", host="0.0.0.0", port=8860, log_level="info")
