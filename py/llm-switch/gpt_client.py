from openai import OpenAI

def call_gpt(prompt: str, config: dict) -> str:
    client = OpenAI()

    response = client.chat.completions.create(
        model=config["llm"]["model"]["openai"],
        temperature=config["llm"]["temperature"],
        max_tokens=config["llm"]["max_tokens"],
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
