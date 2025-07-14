# 🗣️ GroqMeet — Voice to JSON Scheduler

**GroqMeet** is a voice-based assistant that transcribes your spoken request and converts it into structured meeting data in real-time. Powered by **Groq’s Whisper model** for transcription and **LLMs** for natural language understanding, this app is built using **Gradio** for an intuitive voice interface.

> 🚧 This project is in early development — Google Calendar integration is coming next.

---

## 🎯 Features

- 🎤 **Voice Input** via microphone or file upload (MP3/WAV)
- ✍️ **Automatic transcription** using Groq's `whisper-large-v3-turbo`
- 🤖 **LLM-powered intent extraction** (name, time, day, date)
- 🧠 Returns clean, structured **JSON output**
- 🧪 Built with modular, production-friendly Python structure
- 🌐 Future: Schedule meetings automatically on Google Calendar

---

## 📦 Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| **Python**   | Main programming language              |
| **Gradio**   | Frontend for voice input and display   |
| **Groq API** | Whisper + LLMs for transcription/NLU   |
| **dotenv**   | Secure environment variable management |

---

## 📸 Demo (coming soon)

_Sample input:_  
> “Schedule a meeting with Ali on Tuesday at 8 AM”

_Sample output:_

```json
{
  "name": "Ali",
  "time": "08:00",
  "day": "Tuesday",
  "date": "2025-07-15"
}
