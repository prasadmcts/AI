from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="./trained_model",
    tokenizer="./trained_model"
)

id2label = getattr(classifier.model.config, "id2label", {})


def pretty_print(text):
    out = classifier(text)[0]
    label = out["label"]
    score = out.get("score", 0.0)
    idx = None
    if isinstance(label, str) and label.startswith("LABEL_"):
        try:
            idx = int(label.split("_")[-1])
        except Exception:
            idx = None
    human = id2label.get(idx, id2label.get(
        str(idx), label)) if id2label else label
    print(f'"{text}" -> {human} ({score:.3f})')


texts = [
    "I hate bhargavi",
    "I love bhargavi"
]

for t in texts:
    pretty_print(t)
