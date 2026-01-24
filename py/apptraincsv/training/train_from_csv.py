import pandas as pd
from datasets import Dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    Trainer,
    TrainingArguments
)

# 1️⃣ Load CSV
df = pd.read_csv("../data/sentiment_data.csv")

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df)

# Train-test split
dataset = dataset.train_test_split(test_size=0.2)

train_dataset = dataset["train"]
eval_dataset = dataset["test"]

# 2️⃣ Load tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained(
    "distilbert-base-uncased"
)


def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding=True
    )


train_dataset = train_dataset.map(tokenize, batched=True)
eval_dataset = eval_dataset.map(tokenize, batched=True)

# 3️⃣ Load model
# model = DistilBertForSequenceClassification.from_pretrained(
#     "distilbert-base-uncased",
#     num_labels=2
# )

label2id = {
    "NEGATIVE": 0,
    "POSITIVE": 1
}

id2label = {
    0: "NEGATIVE",
    1: "POSITIVE"
}

model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=2,
    label2id=label2id,
    id2label=id2label
)

# 4️⃣ Training arguments
# training_args = TrainingArguments(
#     output_dir="./results",
#     evaluation_strategy="epoch",
#     num_train_epochs=3,
#     per_device_train_batch_size=8,
#     per_device_eval_batch_size=8,
#     logging_steps=10,
#     save_strategy="epoch",
#     learning_rate=2e-5,
#     weight_decay=0.01
# )

training_args = TrainingArguments(
    output_dir="../results",
    # old-style params for older transformers:
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_steps=10,
    save_steps=500,          # instead of save_strategy
    do_eval=True,            # enable evaluation
    # evaluation_strategy="epoch" if hasattr(
    #     TrainingArguments, "evaluation_strategy") else None,
    learning_rate=2e-5,
    weight_decay=0.01
)

# 5️⃣ Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# 6️⃣ Train
trainer.train()

# 7️⃣ Save model
model.save_pretrained("../trained_model")
tokenizer.save_pretrained("../trained_model")

print("✅ Training completed and model saved")
