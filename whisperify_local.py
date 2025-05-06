import argparse
from whisperify_core import transcribe_audio

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe an audio file using Whisper.")
    parser.add_argument("audio", help="Path to the audio file (e.g., .mp3, .wav)")
    parser.add_argument("--model", default="base", help="Whisper model size: tiny, base, small, medium, large")
    parser.add_argument("--language", help="Language code (e.g., 'es', 'en'). If not specified, it will be auto-detected.")
    args = parser.parse_args()

    transcribe_audio(args.audio, args.model, args.language)
