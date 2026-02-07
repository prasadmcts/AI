from anthropic import Anthropic

def call_claude(prompt: str, config: dict) -> str:
    client = Anthropic()

    response = client.messages.create(
        model=config["llm"]["model"]["anthropic"],
        temperature=config["llm"]["temperature"],
        max_tokens=config["llm"]["max_tokens"],
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text
