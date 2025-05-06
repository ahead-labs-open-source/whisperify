FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir fastapi uvicorn openai-whisper

WORKDIR /app
COPY . /app

# Default command to run the application
CMD ["uvicorn", "whisperify_api:app", "--host", "0.0.0.0", "--port", "80"]
