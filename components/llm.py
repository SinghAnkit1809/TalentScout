from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

class LLM:
    def __init__(self, query: str, history: list):
        self.client = Groq(api_key=os.getenv('GROQ_URL'))
        self.model = "llama-3.3-70b-versatile"
        self.query = query  
        self.history = history 

    def call_llm(self):
    # Ensure history follows Groq's message format
        messages = [{"role": msg["role"], "content": msg["content"]} for msg in self.history]
        
        messages.append({"role": "user", "content": self.query})
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages, 
            max_tokens=250,
            temperature=0.7
        )
        
        return response.choices[0].message.content

