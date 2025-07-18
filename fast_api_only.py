from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tempfile, os

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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
