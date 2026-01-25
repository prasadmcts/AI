from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def ask_rag(query: str):
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vectors",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = db.similarity_search(query, k=3)

    context = "\n\n".join([d.page_content for d in docs])
    
    print("Context:", context)

    prompt = f"""
You are an HR policy assistant.
Answer strictly using the context below.
If the answer is not found, say "Not found in policy".

Context:
{context}

Question:
{query}
"""

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0
    )

    response = llm.invoke(prompt)
    return response.content
