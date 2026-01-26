Text files (Confluence)
 ↓
ingest.py (one-time)
 ↓
Embeddings + FAISS
 ↓
Saved vectors/

FastAPI (groq_app.py)
 ↓
Similarity search
 ↓
Groq LLM
 ↓
Answer

==============

python -m venv groq-env
groq-env\Scripts\activate

pip install fastapi uvicorn python-dotenv langchain langchain-community langchain-huggingface langchain-groq sentence-transformers faiss-cpu
pip freeze > requirements.txt

python ingest.py
python ingest_incremental.py

uvicorn groq_app:app --reload

http://127.0.0.1:8000/docs

what is leave policy?
what is wfh policy?
what are security guidelines?
tell about hemanya