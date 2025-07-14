from transcribe import transcribe
from get_json import get_json
import json
import gradio as gr
def process(audio_data):
    try:
        tr = transcribe(audio_data)
        js = get_json(tr)
        return tr, json.dumps(js, indent=2)
        #added comment
    
    except Exception as e:
        print("Failed:", e)
        return "Error", f"Failed: {e}"

app = gr.Interface(fn=process,
    inputs=gr.Audio(sources=["microphone","upload"], type="filepath"),
    outputs=["text", "text"],
    title="Microphone Audio Processing",
    description="Record audio from your microphone and process it."
)
app.launch()
