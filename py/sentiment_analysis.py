from transformers import pipeline

# Step 1: Load a sentiment-analysis pipeline
sentiment_pipeline = pipeline(
    task="sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Step 2: Input text
text = "I am very excited to become an AI Engineer!"

# Step 3: Run inference
result = sentiment_pipeline(text)

# Step 4: Print result
print("Input Text:", text)
print("Prediction:", result)
