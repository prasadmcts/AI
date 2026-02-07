from anthropic import Anthropic

client = Anthropic()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=100,
    messages=[
        {
            "role": "system",
            "content": "You are a teacher. Explain in very simple words."
        },
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
)

print(response.content[0].text)
