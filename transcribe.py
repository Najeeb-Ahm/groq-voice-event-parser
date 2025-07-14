from config import groq_client
# Open the audio file
def transcribe(filename):
  #print(f"initializing transcription for {filename}") ### It was to check if the file is opened
  with open(filename, "rb") as file:
    #print("file opened") ### It was to check if the file is opened
    transcription = groq_client.audio.transcriptions.create(
      file=file,
      model="whisper-large-v3-turbo",
      prompt="Specify context or spelling",
      response_format="verbose_json",
      language="ur",
      temperature=0.0
    )
    #print("transcription created") ### It was to check if the transcription is created
    print("Transcription response:", transcription.text)  # Debugging line to check the transcription output
    return transcription.text