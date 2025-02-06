from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

class LLM:
    def __init__(self, query: str):
        self.client = Groq(api_key = os.getenv('GROQ_URL'))
        self.model = "llama-3.3-70b-versatile"
        self.query = query  
        
    def call_llm(self):
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "user", "content": self.query}],
            max_tokens = 250,
            temperature = 0.7
        )
        return response.choices[0].message.content