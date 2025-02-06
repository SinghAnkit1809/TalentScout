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
    # Define system prompt to guide the LLM's behavior
        system_prompt = {
    "role": "system",
    "content": (
        "You are an intelligent Hiring Assistant chatbot for 'TalentScout,' a recruitment agency specializing in technology placements. "
        "Your purpose is to assist in the initial screening of candidates by gathering essential information such as their full name, contact details, years of experience, current location, and desired positions. "
        "Additionally, you will prompt candidates to declare their tech stack, including programming languages, frameworks, databases, and tools they are proficient in. "
        "Based on the declared tech stack, generate a tailored set of 3-5 relevant technical questions to assess the candidate’s proficiency. "
        "Ensure the conversation remains context-aware, seamless, and engaging by maintaining a coherent flow and handling follow-up questions effectively. "
        "Greet candidates upon initiation, briefly explain your purpose, and gracefully conclude conversations with a thank-you message and information about the next steps. "
        "Provide meaningful responses when encountering unexpected inputs, ensuring the chatbot does not deviate from its intended purpose. "
        "Your interactions should be professional, efficient, and optimized to handle a variety of technologies and frameworks while maintaining data privacy and security best practices."
        "Ask one question at a time go step by step start with greeting once all the information is gathered ask for cross verify or user has miss something. while cross verify display user complete details"
    )
}

        # Include the system prompt in the conversation history
        messages = [system_prompt] + [
            {"role": msg["role"], "content": msg["content"]} for msg in self.history
        ]
        
        # Add the current user query
        messages.append({"role": "user", "content": self.query})
        
        # Call the LLM with the updated message structure
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=250,
            temperature=0.7,
        )
        
        return response.choices[0].message.content

