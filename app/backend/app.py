from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; restrict to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Language data
LANGUAGES = {
    "en": {
        "greeting": "Hello, {name}!",
        "response": "Your message was: {message}"
    },
    "es": {
        "greeting": "¡Hola, {name}!",
        "response": "Tu mensaje fue: {message}"
    }
}

class MessageRequest(BaseModel):
    name: str
    message: str
    language: str

@app.post("/process-message")
async def process_message(data: MessageRequest):
    lang = data.language if data.language in LANGUAGES else "en"
    response = {
        "greeting": LANGUAGES[lang]["greeting"].format(name=data.name),
        "response": LANGUAGES[lang]["response"].format(message=data.message)
    }
    return response
