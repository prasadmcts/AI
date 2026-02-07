def query_policy_rag(intent: str) -> str:
    if intent == "LEAVE":
        return (
            "Employees are entitled to 24 paid leaves per year. "
            "Casual leave can be taken with manager approval. "
            "Unused leaves cannot be carried forward."
        )

    if intent == "WFH":
        return (
            "Employees may work from home up to 3 days per week. "
            "WFH must be approved by the manager."
        )

    if intent == "POLICY":
        return "Please specify whether you are asking about leave or work from home policy."

    return "Policy information not found."
