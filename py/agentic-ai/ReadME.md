python -m venv agentic-ai-env
agentic-ai-env\Scripts\activate

pip install langchain langchain-community faiss-cpu sentence-transformers fastapi uvicorn python-dotenv

python ingest.py

uvicorn main:app --reload

http://127.0.0.1:8000/docs

What is the leave policy?
Can I work from home?
What are security rules?