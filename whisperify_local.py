import argparse
import os

import whisper
from pathlib import Path
import sys

def transcribe_audio(file_path, model_size="base", language=None):
    # Convert to Path object for better path handling
    audio_path = Path(file_path)
    
    if not audio_path.is_file():
        print(f"[DEBUG] Working dir: {Path.cwd()}")
        print(f"[DEBUG] File path received: {file_path}")
        print(f"[DEBUG] File exists: {audio_path.exists()}")
        sys.exit(f"File not found: {file_path}")

    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)

    print(f"Transcribing: {file_path}...")
    options = {}
    if language:
        options["language"] = language

    output_file = audio_path.with_name(f"{audio_path.stem}_transcription.txt")
    result = model.transcribe(str(audio_path), **options)

    print(f"Detected language: {result.get('language', 'unknown')}")
    
    # Handle the transcription text properly
    transcription_text = result["text"]
    if isinstance(transcription_text, list):
        transcription_text = " ".join(transcription_text)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(transcription_text)

    print(f"Transcription saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper.")
    parser.add_argument("audio", help="Path to the audio file (e.g., .mp3, .wav)")
    parser.add_argument("--model", default="base", help="Whisper model size: tiny, base, small, medium, large")
    parser.add_argument("--language", help="Language code (e.g., 'es', 'en'). If not specified, it will be auto-detected.")
    args = parser.parse_args()

    transcribe_audio(args.audio, args.model, args.language)
