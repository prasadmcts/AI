from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="./trained_model",
    tokenizer="./trained_model"
)

print(classifier("This movie was amazing"))
print(classifier("This movie was terrible"))
