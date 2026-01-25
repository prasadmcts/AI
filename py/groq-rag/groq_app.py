from fastapi import FastAPI
from groq_rag import ask_rag

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    return {
        "question": q,
        "answer": ask_rag(q)
    }
