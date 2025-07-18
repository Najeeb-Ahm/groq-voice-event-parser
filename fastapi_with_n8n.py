import os
import tempfile
import requests
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from config import WEBHOOK_URL
app = FastAPI()

# Get webhook URL from environment variable

@app.get("/")
def read_root():
    print("Welcome to the FastAPI application!")
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
        
        # Send data to n8n webhook
        print(f"Here is the actual type when sending it to Webhook: {type(js)}")
        try:
            if not WEBHOOK_URL:
                raise ValueError("WEBHOOK_URL is not set in the environment variables.")
            
            # Send JSON data to n8n webhook
            webhook_response = requests.post(WEBHOOK_URL, json=js)
            
            if webhook_response.ok:
                print("Webhook Initiated Successfully")
                print(f"Webhook response: {webhook_response.status_code}")
            else:
                print(f"Webhook failed with status: {webhook_response.status_code}")
                print(f"Webhook response: {webhook_response.text}")
                
        except Exception as webhook_error:
            print(f"Webhook error: {webhook_error}")
            # Continue execution even if webhook fails
        
        # Print results for debugging
        print("Transcription:", tr)
        print("JSON Data:", js)
        
        return {"transcription": tr, "json": js}
        
    except Exception as e:
        return JSONResponse(content={"error": f"Failed: {str(e)}"}, status_code=500)
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port= 8000, log_level="info")