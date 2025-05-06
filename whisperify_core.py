import os
import sys
import shutil
import subprocess
import time
import whisper

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("❌ ffmpeg not found in PATH.")
        print("Please install ffmpeg and add it to your system PATH.")
        sys.exit(1)
    else:
        try:
            subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            print("❌ ffmpeg is not working properly.")
            sys.exit(1)

def transcribe_audio(file_path, model_size="base", language=None):
    if not os.path.isfile(file_path):
        sys.exit(f"❌ File not found: {file_path}")

    check_ffmpeg()

    print(f"✅ Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)

    print(f"🎙️ Transcribing: {file_path}...")
    start_time = time.time() # Start the timer

    options = {"fp16": False}
    if language:
        options["language"] = language

    result = model.transcribe(file_path, **options)
    end_time = time.time() # End the timer
    elapsed_time = end_time - start_time
    print(f"⏱️ Transcription completed in {elapsed_time:.2f} seconds.")

    print(f"🗣️ Detected language: {result.get('language', 'unknown')}")
    output_file = os.path.splitext(file_path)[0] + "_transcription.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result["text"])

    print(f"✅ Transcription saved to: {output_file}")
    return result["text"]
