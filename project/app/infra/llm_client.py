# app/infra/llm_client.py
import os
import requests


class LLMClient:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = "gemini-flash-latest"

        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")

        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{self.model}:generateContent"
        )

    def generate_text(self, prompt: str) -> str:
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ]
        }

        response = requests.post(
            self.url,
            params={"key": self.api_key},
            json=payload,
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]
