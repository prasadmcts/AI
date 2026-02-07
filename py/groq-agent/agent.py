from intent_classifier import classify_intent
from rag_tool import query_policy_rag


def agent_answer(query: str) -> str:
    intent = classify_intent(query)

    if intent in ["LEAVE", "WFH", "POLICY"]:
        return query_policy_rag(intent)

    return "Sorry, I could not understand your request."
