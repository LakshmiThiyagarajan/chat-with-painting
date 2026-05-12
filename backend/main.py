from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

from prompts import PAINTINGS
from database import SessionLocal, Memory

import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class ChatRequest(BaseModel):
    session_id: str
    painting: str
    character: str
    message: str


def get_memory(key: str) -> str:
    db = SessionLocal()
    memory = db.query(Memory).filter(Memory.key == key).first()
    db.close()
    return memory.summary if memory else ""


def save_memory(key: str, painting: str, character: str, summary: str):
    db = SessionLocal()
    memory = db.query(Memory).filter(Memory.key == key).first()

    if memory:
        memory.summary = summary
    else:
        memory = Memory(
            key=key,
            painting=painting,
            character=character,
            summary=summary
        )
        db.add(memory)

    db.commit()
    db.close()


def summarize_memory(old_summary: str, user_msg: str, ai_msg: str) -> str:
    prompt = f"""
You are maintaining a memory summary of a conversation between a user and a roleplay character.

Previous memory:
{old_summary}

New interaction:
User: {user_msg}
Character: {ai_msg}

Update the memory in 3-4 lines capturing important emotional and contextual details.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=120
    )

    return response.choices[0].message.content


def build_prompt(painting, character, memory_summary):
    base_prompt = PAINTINGS[painting]["characters"][character]

    memory_block = f"""
[Memory of Conversation]
The character remembers the following about previous conversation with this user:
{memory_summary}
"""

    return base_prompt + memory_block


def generate_reply(session_id: str, painting: str, character: str, message: str) -> str:
    key = f"{session_id}_{painting}_{character}"


    memory_summary = get_memory(key)

    prompt = build_prompt(painting, character, memory_summary)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],
        max_tokens=150
    )

    reply = response.choices[0].message.content

    updated_memory = summarize_memory(
        memory_summary,
        message,
        reply
    )

    save_memory(key, painting, character, updated_memory)

    return reply


# -------- API --------

@app.post("/chat")
def chat(req: ChatRequest):
    reply = generate_reply(
        req.session_id, 
        req.painting,
        req.character,
        req.message
    )

    return {"reply": reply}