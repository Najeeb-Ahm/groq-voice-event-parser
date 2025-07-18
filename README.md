# 🗣️ GroqMeet — Voice to JSON Scheduler

**GroqMeet** is a voice-based assistant that transcribes your spoken request and converts it into structured meeting data in real-time. Powered by **whisper-large-v3-turbo** for transcription and **llama-3.3-70b-versatile** for natural language understanding, this app is built using **Gradio** for an intuitive voice interface.

> 🚧 This project is in early development — Google Calendar integration is coming next.

---

## 🎯 Features

- 🎤 **Voice Input** via microphone or file upload (MP3/WAV)
- ✍️ **Automatic transcription** using `whisper-large-v3-turbo`
- 🤖 **LLM-powered intent extraction** (name, time, day, date)
- 🧠 Returns clean, structured **JSON output**
- 🧪 Built with modular, production-friendly Python structure
- 🔁 **Runs both Gradio & FastAPI** concurrently via threading
- 🌐 **n8n webhook integration** for workflow automation
- 🌍 **Multilingual support** (English, Urdu, Hindi)
- 🔮 Future: Schedule meetings automatically on Google Calendar

---

## 📦 Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| **Python**   | Main programming language              |
| **Gradio**   | Frontend for voice input and display   |
| **FastAPI**  | Backend API server                     |
| **Groq API** | Whisper + LLaMA                        |
| **dotenv**   | Secure environment variable management |
| **Uvicorn**  | ASGI server for FastAPI                |
| **Threading**| Run Gradio + FastAPI together          |
| **n8n**      | Workflow automation integration        |

---

## 📋 Requirements

- Python 3.8+
- Internet connection (for Groq API)
- Microphone access (for voice input)
- Modern web browser
- Valid Groq API key with credits

---

## 📁 Project Structure

```
groq-voice-event-parser/
├── gradio.py              # Gradio UI interface
├── fastapi.py            # FastAPI server
├── fastapi_with_n8n.py   # FastAPI with webhook
├── main.py               # Combined runner
├── transcribe.py         # Whisper transcription
├── get_json.py           # LLM JSON extraction
├── config.py             # Environment config
├── requirements.txt      # Dependencies
└── .env                  # Environment variables
```

---

## 📸 Demo

**Supports English, Urdu, and Hindi**

*Sample input in voice using the Gradio UI:*  
<img width="943" height="485" alt="image" src="https://github.com/user-attachments/assets/4cf40a94-f73c-4418-a2cf-740203401c1c" />

This input is transcribed using **whisper**
> "Meeting schedule کردو علی حیدر کے ساتھ کل آٹھ بجے"

*Sample output:*
<img width="926" height="362" alt="image" src="https://github.com/user-attachments/assets/5d36f522-17e1-4a26-82a9-7721c6c270a2" />

```json
{
  "name": "Ali Haider",
  "time": "08:00",
  "day": "Wednesday",
  "date": "2025-07-17"
}
```

---

## ▶️ How to Use

Follow these steps to set up and run the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/Najeeb-Ahm/groq-voice-event-parser.git
cd groq-voice-event-parser
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a file named `.env` in the root folder and add your [Groq API key](https://console.groq.com/keys):

```env
GROQ_API_KEY=your_groq_api_key_here
WEBHOOK_URL=your_webhook_url_here
```

**Then run the config file once to load your environment variables:**
```bash
python config.py
```

### 5. Run the Project

#### Gradio UI Only
```bash
python gradio.py
```

#### FastAPI Only
```bash
python fastapi.py
```

#### FastAPI with n8n Only
```bash
python fastapi_with_n8n.py
```

#### Gradio + FastAPI + n8n (Recommended)
```bash
python main.py
```

This will open the app in your browser.

### 6. Interact with the app

- 🎙️ Record your voice or upload an `audio` file
- 🧠 The app uses **Whisper (via Groq)** to transcribe your voice
- 💬 Then it sends the transcript to a **Groq-hosted LLM** for understanding
- 📦 You get a clean **JSON object** like this:

```json
{
  "name": "Ali",
  "time": "08:00",
  "day": "Tuesday",
  "date": "2025-07-15"
}
```

---

## 🔌 API Endpoints

### FastAPI Server (http://127.0.0.1:8000)
- `POST /process-audio/` - Upload audio file for transcription and JSON extraction
- `GET /` - Health check endpoint

### Example API Usage
```bash
curl -X POST "http://127.0.0.1:8000/process-audio/" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "audio_file=@your_audio_file.wav"
```

---

## 🔧 Troubleshooting

- **Port conflicts**: If port 8000 is busy, the app will auto-select another port
- **API errors**: Verify your GROQ_API_KEY is valid and has credits
- **Audio issues**: Ensure your microphone permissions are enabled
- **Webhook errors**: Check that your WEBHOOK_URL is correct and accessible
- **Import errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`

---

## 🔮 Coming Soon

- 🗓️ Integration with Google Calendar API
- 📱 Mobile app version
- 🌐 Multi-language calendar event creation
- 🔔 Email notifications and reminders
- 📊 Meeting analytics and insights

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


---

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing fast AI inference
- [Gradio](https://gradio.app/) for the intuitive UI framework
- [FastAPI](https://fastapi.tiangolo.com/) for the robust API framework
- [n8n](https://n8n.io/) for workflow automation capabilities


---

**⭐ If you found this project helpful, please consider giving it a star on GitHub!**