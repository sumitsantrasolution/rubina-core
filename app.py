from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "Rubina Core is running"}

@app.post("/ask")
def ask_ai(data: Message):
    user_message = data.message
    
    # Basic response (temporary)
    reply = f"Rubina received: {user_message}"
    
    return {
        "reply": reply
    }
