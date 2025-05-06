FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir fastapi uvicorn openai-whisper

# Set up working directory
WORKDIR /app
COPY . /app

# Default command to run the application
CMD ["uvicorn", "whisperify_api:app", "--host", "0.0.0.0", "--port", "80"]
