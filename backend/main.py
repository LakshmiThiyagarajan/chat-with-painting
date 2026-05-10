from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from prompts import PAINTINGS
import os

load_dotenv()

app = FastAPI()

# allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    painting: str
    character: str
    message: str


def generate_reply(painting, character, message):

    prompt = PAINTINGS[painting]["characters"][character]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": message
            }
        ],
        max_tokens=120
    )

    return response.choices[0].message.content


@app.post("/chat")
def chat(req: ChatRequest):

    reply = generate_reply(
        req.painting,
        req.character,
        req.message
    )

    return {"reply": reply}