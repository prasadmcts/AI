# Fetches Confluence pages via API
# Cleans HTML → extracts text
# Splits text into chunks
# Creates embeddings
# Stores FAISS vectors locally

import os
import requests
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document

load_dotenv()

BASE_URL = os.getenv("CONFLUENCE_BASE")
USER = os.getenv("CONFLUENCE_USER")
API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")

CHUNK_SIZE = 500  # tokens approx

# Step 1: Fetch pages
def fetch_pages(limit=50):
    url = f"{BASE_URL}/rest/api/content?type=page&limit={limit}&expand=body.storage"
    resp = requests.get(url, auth=(USER, API_TOKEN))
    resp.raise_for_status()
    return resp.json()["results"]

# Step 2: Preprocess pages
def preprocess_page(page):
    title = page["title"]
    html_content = page["body"]["storage"]["value"]
    # Simple HTML tag removal (for demo)
    import re
    text = re.sub(r"<[^>]+>", "", html_content)
    return text, title

# Step 3: Chunk text
def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Step 4: Create Documents
def create_documents():
    pages = fetch_pages()
    docs = []
    for page in pages:
        text, title = preprocess_page(page)
        chunks = chunk_text(text)
        for chunk in chunks:
            docs.append(Document(page_content=chunk, metadata={"title": title}))
    return docs

# Step 5: Create embeddings & store
def build_vectorstore():
    docs = create_documents()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("vectors")
    print(f"Saved {len(docs)} chunks to FAISS vectors.")

if __name__ == "__main__":
    build_vectorstore()