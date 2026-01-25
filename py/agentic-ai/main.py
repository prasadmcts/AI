from fastapi import FastAPI
from agent import ask_agent

app = FastAPI()


@app.get("/ask")
def ask(q: str):
    return ask_agent(q)
