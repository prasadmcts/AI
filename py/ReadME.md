Think of AI models / LLMs exactly like npm or NuGet packages—but instead of one registry, they live across model hubs, cloud providers, and local runtimes.

LLMs & AI models
	URL: https://huggingface.co/models
OpenAI Models (Hosted APIs)
        Docs: https://platform.openai.com/docs/models
Azure OpenAI (Enterprise-friendly): Same models as OpenAI, hosted inside Azure. Good for .Net

Local LLM Runtimes (Run like Docker)


https://app.datacamp.com/learn/career-tracks/associate-ai-engineer-for-developers

-> app ==> 
   python -m venv ai-env
   ai-env\Scripts\activate
   pip install fastapi uvicorn transformers torch
   uvicorn app.main:app --reload
	FastAPI = Framework
	Uvicorn = Server

	You cannot run FastAPI without a server like Uvicorn.

 docker build -t ai-text-generator .

docker run -p 8000:8000 ai-text-generator

http://localhost:8000/docs

-> Python is NOT a web server. Uvicorn is the web server.

In real companies: Client → Nginx → Gunicorn → Uvicorn → FastAPI → AI Model

This is equivalent to: Client → IIS → Kestrel → ASP.NET Core → Business Logic

-> “using models” → “training a model”

==> apptrain

python -m venv ai-train-env
ai-train-env\Scripts\activate
pip install transformers datasets torch scikit-learn
python train_sentiment.py
python trained_model_test.py

==> apptraincsv

python -m venv ai-train-env
ai-train-env\Scripts\activate
pip install transformers datasets torch scikit-learn
? pip install accelerate>=0.26.0
> python generate_csv.py
> training > python train_from_csv.py
> python test_csv_model.py


============
rmdir /s /q ai-env
python -m venv ai-env
ai-env\Scripts\activate
pip install -r requirements.txt
