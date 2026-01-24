from pydantic import BaseModel


class TextRequest(BaseModel):
    prompt: str


class TextResponse(BaseModel):
    result: str

class ExplainRequest(BaseModel):
    topic: str


class ExplainResponse(BaseModel):
    output: str
