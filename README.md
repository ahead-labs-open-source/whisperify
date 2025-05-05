# 🎧 Whisprify

**Whisprify** is an open-source API to transcribe audio files into text using OpenAI's Whisper model. Easily deployable as a container in Azure, it turns any voice recording into plain text via a simple HTTP request.

---

## 🚀 Features

- 🎙️ Automatic transcription of audio files (MP3, WAV, etc.)
- 🧠 Powered by [OpenAI Whisper](https://github.com/openai/whisper)
- 🌍 Multilingual support (defaults to Spanish)
- ☁️ Ready to deploy on Azure via Docker or Container Apps
- 📦 REST API built with FastAPI and OpenAPI documentation

---

## 🧱 Structure

```
📂 whisprify/
├── transcriber_api.py      # Main API with FastAPI
├── requirements.txt        # Python dependencies
├── Dockerfile              # Production-ready container setup
└── README.md               # This file
```

---

## 🛠️ Requirements

- Python 3.8+
- ffmpeg installed on the system
- Docker (optional for deployment)

To install dependencies:
```bash
pip install -r requirements.txt
```

---

## ▶️ Local Usage

```bash
uvicorn transcriber_api:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) to test the API using Swagger UI.

---

## 📡 API Usage

### POST `/transcribe/`

**Parameters:**
- `file` (multipart/form-data): Audio file

**Response:**
```json
{
  "transcription": "Transcribed text from the audio"
}
```

---

## 🐳 Docker Deployment

```bash
docker build -t whisprify .
docker run -p 8000:80 whisprify
```

---

## ☁️ Azure Deployment

Whisprify is ready for deployment in Azure Container Apps or Azure App Service with container support. See `docs/deploy_azure.md` (coming soon).

---

## 📄 License

GPL v3.0 License. This project is open-source and you can use, modify, and share it freely.

---

## 🤝 Contributions

Got ideas, improvements, or issues? Feel free to open pull requests or issues!

---

## 💡 Inspiration

Built on the power of OpenAI Whisper and the need for simple, private voice transcription services. Created with ❤️ for developers, journalists, researchers, and creators.
