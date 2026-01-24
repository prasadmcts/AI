from transformers import pipeline

# Load text-generation pipeline
generator = pipeline(
    task="text-generation",
    model="gpt2"
)

# Prompt
prompt = "Artificial Intelligence will change the future of software development because"

# Generate text
result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1
)

print(result[0]["generated_text"])
