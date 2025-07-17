from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tempfile, os , requests
import os
import uvicorn
import threading
import gradio as gr


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/process-audio/")
async def process_audio(audio_file: UploadFile = File(...)):
    from transcribe import transcribe
    from get_json import get_json

    try:
        # Save uploaded file to a temp file
        suffix = os.path.splitext(audio_file.filename)[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            content = await audio_file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Transcribe from saved file path
        tr = transcribe(tmp_path)
        js = get_json(tr)

        # Clean up the temp file
        os.remove(tmp_path)

        return {"transcription": tr, "json": js}

    except Exception as e:
        return JSONResponse(content={"error": f"Failed: {str(e)}"}, status_code=500)

def process(audio_path):
    try:
        with open(audio_path, "rb") as f:
            files = {"audio_file": (os.path.basename(audio_path), f, "audio/wav")}
            response = requests.post("http://127.0.0.1:8000/process-audio/", files=files)

        if response.ok:
            data = response.json()
            return data["transcription"], data["json"]
        else:
            return "Error", response.text
    except Exception as e:
        return "Error", str(e)
    
def start_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    


if __name__ == "__main__":
    # Start FastAPI in a separate thread
    threading.Thread(target=start_fastapi,daemon=True).start()
    print(f"FastAPI server started on http://127.0.0.1:8000")

    #Start Gradio interface
    gr.Interface(
        fn=process,
        inputs=gr.Audio(sources=["microphone", "upload"], type="filepath"),
        outputs=["text", "text"],
        title="Microphone Audio Processing",
        description="Record audio from your microphone and process it."
    ).launch()