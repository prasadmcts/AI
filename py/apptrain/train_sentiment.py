from datasets import load_dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)

# 1️⃣ Load dataset
dataset = load_dataset("imdb")

# Use small subset to train fast
dataset = dataset["train"].shuffle(seed=42).select(range(2000))
test_dataset = load_dataset("imdb")["test"].select(range(500))

# 2️⃣ Load tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)


def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding=True)


dataset = dataset.map(tokenize, batched=True)
test_dataset = test_dataset.map(tokenize, batched=True)

# 3️⃣ Load model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2
)

# 4️⃣ Training config
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    num_train_epochs=2,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_steps=50,
    save_strategy="epoch",
    learning_rate=2e-5,
    weight_decay=0.01,
)

# 5️⃣ Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=test_dataset,
)

# 6️⃣ Train
trainer.train()

# 7️⃣ Save model
model.save_pretrained("./trained_model")
tokenizer.save_pretrained("./trained_model")
