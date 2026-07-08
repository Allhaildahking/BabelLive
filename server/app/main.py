import os
import shutil

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import FileResponse

from app.services.translator import TranslatorService
from app.services.speech import SpeechService
from app.services.voice import VoiceService

app = FastAPI(title="BabelLive")
app.mount(
    "/static",
    StaticFiles(directory="../client"),
    name="static"
)

translator = TranslatorService()
speech = SpeechService()
voice = VoiceService()


class TranslationRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse("../client/index.html")


@app.post("/translate")
def translate(request: TranslationRequest):

    translated_text = translator.translate(request.text)

    return {
        "original": request.text,
        "translated": translated_text
    }


@app.post("/transcribe")
def transcribe(audio: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", "audio.webm")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    print("Filename:", audio.filename)
    print("Saved to:", file_path)
    print("File size:", os.path.getsize(file_path), "bytes")

    transcription = speech.transcribe(file_path)

    translation = translator.translate(transcription)

    audio_file = voice.speak(translation)

    return {
        "transcription": transcription,
        "translation": translation,
        "audio_file": audio_file
    }


@app.get("/audio")
def get_audio():

    audio_path = "outputs/translated.mp3"

    if not os.path.exists(audio_path):
        return {"error": "No translated audio found."}

    return FileResponse(
        audio_path,
        media_type="audio/mpeg",
        filename="translated.mp3"
    )