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
- 🌐 Future: Schedule meetings automatically on Google Calendar

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

---

## 📸 Demo
**Supports English, Urdu, and Hindi**
_Sample input in voice using the Gradio UI:_  
<img width="943" height="485" alt="image" src="https://github.com/user-attachments/assets/4cf40a94-f73c-4418-a2cf-740203401c1c" />

This input is transcribed using **whisper**
> “Meeting schedule کردو علی حیدر کے ساتھ کل آٹھ بجے”

_Sample output:_
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

---

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

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up environment variables

Create a file named `.env` in the root folder and add your [Groq API key](https://console.groq.com/keys):

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 5. Run the Gradio app

```bash
python main.py
```

This will open the app in your browser.

---

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

### ✅ Coming Soon

- 🗓️ Integration with Google Calendar API
