import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get the API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL_n8n")
#print(WEBHOOK_URL)

# Check if the key is loaded correctly
if not GROQ_API_KEY:
    raise EnvironmentError("GROQ_API_KEY not found in .env file")

# Initialize Groq client
groq_client = Groq(api_key=GROQ_API_KEY)