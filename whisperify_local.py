import argparse
import whisper
import os
import sys

def transcribe_audio(file_path, model_size="base", language=None):
    # if not os.path.isfile(file_path):
    #     print(f"File not found: {file_path}")
    #     sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"[DEBUG] Working dir: {os.getcwd()}")
        print(f"[DEBUG] File path received: {file_path}")
        print(f"[DEBUG] File exists: {os.path.exists(file_path)}")
        sys.exit(f"File not found: {file_path}")

    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)

    print(f"Transcribing: {file_path}...")
    options = {"fp16": False}
    if language:
        options["language"] = language

    result = model.transcribe(file_path, **options)

    print(f"Detected language: {result.get('language', 'unknown')}")
    output_file = os.path.splitext(file_path)[0] + "_transcription.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"Transcription saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper.")
    parser.add_argument("audio", help="Path to the audio file (e.g., .mp3, .wav)")
    parser.add_argument("--model", default="base", help="Whisper model size: tiny, base, small, medium, large")
    parser.add_argument("--language", help="Language code (e.g., 'es', 'en'). If not specified, it will be auto-detected.")
    args = parser.parse_args()

    transcribe_audio(args.audio, args.model, args.language)
