from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("Searching for flash models:")
for model in client.models.list():
    if "flash" in model.name.lower():
        print(f"{model.name}")
