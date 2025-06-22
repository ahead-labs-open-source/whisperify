# This code creates a FastAPI application that allows users to upload an audio file and transcribe it using the Whisper model.
from fastapi import FastAPI, UploadFile, File
import whisper
import tempfile

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        contents = await file.read()
        temp_audio.write(contents)
        temp_audio_path = temp_audio.name

    result = model.transcribe(temp_audio_path, language="es")
    return {"transcription": result["text"]}
