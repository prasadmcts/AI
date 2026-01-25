from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAI
import os

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load vector DB
vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

# LLM
llm = OpenAI(temperature=0)

def ask_rag(question: str):
    docs = vectorstore.similarity_search(question, k=3)

    if not docs:
        return "I don't have information about this."

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an internal company assistant.
Answer ONLY from the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response
