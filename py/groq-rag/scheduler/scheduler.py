import time
import subprocess
import threading


def reindex_job():
    while True:
        print("Running incremental re-index...")
        subprocess.call(["python", "ingest_incremental.py"])
        time.sleep(3600)  # every 1 hour


def start_scheduler():
    thread = threading.Thread(target=reindex_job, daemon=True)
    thread.start()

    pip install fastapi uvicorn langchain langchain-groq python-dotenv
