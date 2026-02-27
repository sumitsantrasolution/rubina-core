from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return {"status": "Rubina Core is running with AI"}

@app.post("/ask")
def ask_ai(data: Message):
    try:
        user_message = data.message

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are Rubina, a powerful personal AI assistant."},
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload
        )

        result = response.json()

        if "error" in result:
            return {"error": result["error"]}

        reply = result["choices"][0]["message"]["content"]

        return {"reply": reply}

    except Exception as e:
        return {"server_error": str(e)}
