from dotenv import load_dotenv
from langchain_groq import ChatGroq
import json


load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",   # ✅ currently supported
    temperature=0
)

INTENT_PROMPT = """
You are an intent classifier.

Classify the user question into ONE of:
WFH, LEAVE, POLICY, UNKNOWN

Return ONLY valid JSON in this format:
{{
  "intent": "WFH|LEAVE|POLICY|UNKNOWN"
}}

User question:
{query}
"""


def classify_intent(query: str) -> str:
    prompt = INTENT_PROMPT.format(query=query)
    response = llm.invoke(prompt)

    try:
        data = json.loads(response.content)
        return data.get("intent", "UNKNOWN")
    except Exception:
        return "UNKNOWN"
