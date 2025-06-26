import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("HUGGINGFACE_API_URL")
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def query_huggingface(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except (KeyError, IndexError):
            return "⚠️ Unexpected response format."
    else:
        return f"❌ Error {response.status_code}: {response.text}"
