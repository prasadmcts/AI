from fastapi import FastAPI
from groq_rag import ask_rag
from scheduler.scheduler import start_scheduler

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    return {
        "question": q,
        "answer": ask_rag(q)
    }


# @app.on_event("startup")
# def startup_event():
#     start_scheduler()
