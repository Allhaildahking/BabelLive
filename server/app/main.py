from fastapi import FastAPI
from pydantic import BaseModel

from app.services.translator import TranslatorService

app = FastAPI(
    title="BabelLive API",
    version="0.1.0"
)

translator = TranslatorService()


class TranslationRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {
        "name": "BabelLive",
        "status": "running",
        "version": "0.1.0"
    }


@app.post("/translate")
def translate(request: TranslationRequest):

    translated_text = translator.translate(request.text)

    return {
        "original": request.text,
        "translated": translated_text
    }