from fastapi import FastAPI, UploadFile, File
from whisperify_core import transcribe_audio
import tempfile

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio_api(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        contents = await file.read()
        temp_audio.write(contents)
        temp_audio_path = temp_audio.name

    transcription = transcribe_audio(temp_audio_path, model_size="base", language="es")
    return {"transcription": transcription}
