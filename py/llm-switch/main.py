import yaml
from llm_factory import generate_response

with open("config.yaml") as f:
    config = yaml.safe_load(f)

prompt = "Explain Python in very simple words"

result = generate_response(prompt, config)

print("\nLLM RESPONSE:\n")
print(result)
