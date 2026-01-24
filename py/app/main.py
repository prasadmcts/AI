from fastapi import FastAPI
from app.ai_service import TextGenerationService
from app.models import TextRequest, TextResponse, ExplainRequest, ExplainResponse

app = FastAPI()
service = TextGenerationService()

@app.post("/generate", response_model=TextResponse)
def generate_text(request: TextRequest):
    output = service.generate(request.prompt)
    return TextResponse(result=output)


@app.post("/explain", response_model=ExplainResponse)
def explain_topic(request: ExplainRequest):
    text = service.generate_explanation(request.topic)
    return ExplainResponse(output=text)
