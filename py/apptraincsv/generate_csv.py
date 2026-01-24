import csv
import random

positive_templates = [
    "I love {}",
    "This {} is amazing",
    "Very good {}",
    "Excellent {}",
    "I am happy with {}",
    "{} works perfectly",
    "Really satisfied with {}",
    "Highly recommend this {}",
    "{} exceeded my expectations",
    "Fantastic {}"
]

negative_templates = [
    "I hate {}",
    "Very bad {}",
    "Terrible {}",
    "Not good {}",
    "Worst {} ever",
    "I am disappointed with {}",
    "{} is awful",
    "Completely unhappy with {}",
    "Poor quality {}",
    "{} failed badly"
]

objects = [
    "product", "service", "experience", "delivery",
    "app", "software", "website", "support",
    "feature", "system"
]

rows = []

for _ in range(500):  # positive
    text = random.choice(positive_templates).format(random.choice(objects))
    rows.append([text, 1])

for _ in range(500):  # negative
    text = random.choice(negative_templates).format(random.choice(objects))
    rows.append([text, 0])

random.shuffle(rows)

with open("data/sentiment_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "label"])
    writer.writerows(rows)

print("✅ sentiment_data.csv created with 1000 rows")
