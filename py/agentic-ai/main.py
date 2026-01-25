# from fastapi import FastAPI
# from agent import ask_agent

# app = FastAPI()


# @app.get("/ask")
# def ask(q: str):
#     return ask_agent(q)


from fastapi import FastAPI
from rag import ask_rag

app = FastAPI(title="Internal AI Assistant")

@app.get("/ask")
def ask(q: str):
    return {"answer": ask_rag(q)}