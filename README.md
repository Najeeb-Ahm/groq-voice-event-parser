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
- 🌐 Future: Schedule meetings automatically on Google Calendar

---

## 📦 Tech Stack

| Tool         | Purpose                                |
|--------------|----------------------------------------|
| **Python**   | Main programming language              |
| **Gradio**   | Frontend for voice input and display   |
| **Groq API** | Whisper + llama                        |
| **dotenv**   | Secure environment variable management |

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
