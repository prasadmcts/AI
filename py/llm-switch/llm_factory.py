from claude_client import call_claude
from gpt_client import call_gpt

def generate_response(prompt: str, config: dict) -> str:
    provider = config["llm"]["provider"]

    if provider == "anthropic":
        return call_claude(prompt, config)
    elif provider == "openai":
        return call_gpt(prompt, config)
    else:
        raise ValueError("Unsupported LLM provider")
