import os
import json
import hashlib
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/confluence"
VECTOR_PATH = "vectors"
REGISTRY_FILE = "data/index_registry.json"


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# Load registry
if not os.path.exists(REGISTRY_FILE):
    registry = {}
else:
    with open(REGISTRY_FILE, "r") as f:
        try:
            registry = json.load(f)
        except json.JSONDecodeError:
            registry = {}

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Load or create vector DB
if os.path.exists(VECTOR_PATH):
    db = FAISS.load_local(
        VECTOR_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    db = None

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

for file in os.listdir(DATA_PATH):
    if not file.endswith(".txt"):
        continue

    file_path = os.path.join(DATA_PATH, file)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    current_hash = compute_hash(content)

    # Skip unchanged
    if file in registry and registry[file]["hash"] == current_hash:
        print(f"⏭️ Skipped unchanged: {file}")
        continue

    print(f"🔄 Indexing: {file}")

    loader = TextLoader(file_path, encoding="utf-8")
    docs = loader.load()

    chunks = splitter.split_documents(docs)

    for c in chunks:
        c.metadata["source"] = file

    # Remove old vectors if updating
    if db and file in registry:
        db.delete(
            [k for k, v in db.docstore._dict.items()
             if v.metadata.get("source") == file]
        )

    if db:
        db.add_documents(chunks)
    else:
        db = FAISS.from_documents(chunks, embeddings)

    registry[file] = {
        "hash": current_hash,
        "chunks": len(chunks)
    }

# Save everything
db.save_local(VECTOR_PATH)

with open(REGISTRY_FILE, "w") as f:
    json.dump(registry, f, indent=2)

print("✅ Incremental indexing complete")