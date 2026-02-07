python -m venv groq-agent-env
groq-agent-env\Scripts\activate

pip install fastapi uvicorn langchain langchain-groq python-dotenv
pip freeze > requirements.txt


uvicorn app:app --reload

http://127.0.0.1:8000/docs

Can I work from home tomorrow?
===================

Rule-Guided Agentic AI using Groq
Overview

This project demonstrates a Rule-Guided Agentic AI system built using Groq LLMs, FastAPI, and Python, designed to make controlled, deterministic decisions instead of letting the LLM directly execute actions.

The agent follows a hybrid architecture:

🧠 LLM decides intent

🧩 Python code decides actions

This approach ensures safety, predictability, and enterprise readiness, making it ideal for HR, policy, compliance, and internal knowledge systems.

Architecture
User Query
   ↓
Intent Classifier (LLM - Groq)
   ↓
Rule-Based Agent (Python)
   ↓
Policy / RAG Tool
   ↓
Final Answer

Key Design Principle

LLM is used only for reasoning and intent detection — not execution

Features

✅ Rule-guided agent workflow

✅ Intent classification using Groq LLM

✅ Deterministic policy handling

✅ FastAPI REST API

✅ Clear separation of responsibilities

✅ No hallucinated actions

✅ Enterprise-safe AI pattern

Supported Intents
Intent	Description
WFH_POLICY	Work From Home policy queries
LEAVE_POLICY	Leave policy related queries
POLICY	Generic policy questions
UNKNOWN	Out-of-scope questions
Project Structure
groq-agent/
│
├── app.py                # FastAPI entry point
├── agent.py              # Rule-based decision logic
├── intent_classifier.py  # LLM-powered intent detection
├── rag_tool.py           # Policy lookup (RAG-style)
├── requirements.txt
└── README.md

How It Works
1️⃣ Intent Classification (LLM)

The Groq LLM analyzes the user query and returns structured JSON indicating the intent.

Example:

{
  "intent": "WFH_POLICY"
}

2️⃣ Rule-Based Decision Making (Python)

Python evaluates the intent and decides which tool or logic to apply.

if intent == "WFH_POLICY":
    return query_policy_rag(query)

3️⃣ Policy Retrieval (RAG-Style)

Policies are retrieved from a controlled knowledge source (currently static, extensible to vector DB).

Example API Call
Request
GET /ask?q=Can I work from home tomorrow?

Response
{
  "answer": "Employees may work from home up to 3 days per week with manager approval."
}

Tech Stack

Python 3.10+

FastAPI

Groq LLM API

LangChain (Groq integration)

Uvicorn

Installation
1. Create Virtual Environment
python -m venv groq-agent-env
source groq-agent-env/bin/activate  # Windows: groq-agent-env\Scripts\activate

2. Install Dependencies
pip install fastapi uvicorn langchain langchain-groq groq python-dotenv

3. Set Environment Variable
export GROQ_API_KEY=your_api_key_here

Run the Application
uvicorn app:app --reload


Access Swagger UI:

http://127.0.0.1:8000/docs

=====================

Python

FastAPI

LangChain

Groq LLM (LLaMA 3)

Agent-based architecture

Rule-based decision engine