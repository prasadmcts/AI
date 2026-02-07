from fastapi import FastAPI
from agent import agent_answer

app = FastAPI(title="Rule-Guided AI Agent (Groq)")


@app.get("/")
def health():
    return {"status": "Groq Agent running"}


@app.get("/ask")
def ask(q: str):
    return {
        "question": q,
        "answer": agent_answer(q)
    }
