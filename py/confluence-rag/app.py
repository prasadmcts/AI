# Accepts GET /ask?q=your question
# Retrieves relevant Confluence chunks from FAISS
# Sends them as context to the LLM
# Returns answer + page titles as sources

from fastapi import FastAPI, Query
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI  # Optional if using OpenAI LLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

app = FastAPI()

# Load FAISS vectors
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("vectors", embeddings)

# Optional: OpenAI LLM (replace with local LLM if needed)
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Prompt template
PROMPT = """
Answer the question using ONLY the context below from Confluence.
Do NOT make up information. If unknown, say "I don’t know."

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(template=PROMPT, input_variables=["context", "question"])
chain = LLMChain(llm=llm, prompt=prompt)

@app.get("/ask")
def ask(q: str = Query(..., description="Your question")):
    # Retrieve top 3 relevant chunks
    docs = db.similarity_search(q, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    result = chain.run({"context": context, "question": q})
    return {
        "answer": result,
        "sources": [doc.metadata["title"] for doc in docs]
    }
