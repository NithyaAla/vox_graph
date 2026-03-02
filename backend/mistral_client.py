import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.mistral.ai/v1"

def get_headers():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise RuntimeError("MISTRAL_API_KEY not set in environment")
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

def voxtral_transcribe(audio_url: str):
    headers = get_headers()
    payload = {
        "model": "voxtral-small",
        "audio": {"url": audio_url},
        "tasks": ["transcription", "semantic_understanding"]
    }
    r = requests.post(f"{BASE_URL}/audio", headers=headers, json=payload)
    r.raise_for_status()
    return r.json()

def mistral_chat(prompt: str, model="mistral-small"):
    headers = get_headers()
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You extract structured knowledge."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    r = requests.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]