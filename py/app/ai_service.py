from transformers import pipeline
from app.prompt_templates import PROMPT_TEMPLATES

class TextGenerationService:

    def __init__(self):
        self.generator = pipeline(
            task="text-generation",
            model="gpt2"
        )

    def generate(self, prompt: str):
        result = self.generator(
            prompt,
            max_length=50,
            num_return_sequences=1
        )
        return result[0]["generated_text"]


    def generate_explanation(self, topic: str) -> str:
        prompt = PROMPT_TEMPLATES["explain_concept"].format(
            topic=topic
        )

        result = self.generator(
            prompt,
            max_length=250,
            num_return_sequences=1
        )

        return result[0]["generated_text"]
