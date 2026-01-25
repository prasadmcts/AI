from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAI
import os

# make sure OPENAI_API_KEY is set
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = OpenAI(temperature=0)

def ask_rag(question: str):
    docs = vectorstore.similarity_search(question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an internal company assistant.
Answer ONLY from the context below.

Context:
{context}

Question:
{question}
"""

    return llm(prompt)
