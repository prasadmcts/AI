# Create virtual env
python -m venv confluence-env
# Activate
.\confluence-env\Scripts\activate  # Windows
source confluence-env/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Step 1: ingest Confluence
python ingest_confluence.py

# Step 2: run FastAPI server
uvicorn app:app --reload