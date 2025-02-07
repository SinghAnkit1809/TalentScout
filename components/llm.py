from groq import Groq
from components.Get_prompt import SystemPrompt
from dotenv import load_dotenv
import os
import json
import uuid
import re
from datetime import datetime

load_dotenv()

class LLM:
    def __init__(self):
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
        self.model = "llama-3.3-70b-versatile"
        self.interviewPrompt = SystemPrompt.get_interview_prompt()
        self.createDataPrompt = SystemPrompt.get_extraction_prompt()
        self.conversation_history = []  # Full transcript of the conversation
        self.data_dir = "candidate_data"
        os.makedirs(self.data_dir, exist_ok=True)


    def conduct_interview(self, user_message):
        # Append candidate message to the conversation history.
        self.conversation_history.append({"role": "user", "content": user_message})
        # Build the prompt including instructions and conversation history.
        prompt = self.interviewPrompt + "\n\nConversation Transcript:\n" + json.dumps(self.conversation_history, indent=2)
        messages = [{"role": "system", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        assistant_message = response.choices[0].message.content.strip()
        self.conversation_history.append({"role": "assistant", "content": assistant_message})

        # If the assistant indicates interview completion, finalize automatically.
        if ("interview complete" in assistant_message.lower() or 
            "data will now be stored" in assistant_message.lower()):
            final_message = self.finalize_interview()
            self.conversation_history.append({"role": "assistant", "content": final_message})
            return final_message

        return assistant_message
    
    def finalize_interview(self):
        # Build extraction prompt including the full conversation transcript.
        prompt = self.createDataPrompt + "\n\n" + json.dumps(self.conversation_history, indent=2)
        messages = [{"role": "system", "content": prompt}]
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=300,
            temperature=0.5
        )
        json_output = response.choices[0].message.content.strip()

        # Attempt to extract a JSON object from the LLM output.
        try:
            json_str = re.search(r'(\{.*\})', json_output, re.DOTALL).group(1)
            candidate_data = json.loads(json_str)
        except Exception:
            candidate_data = {"error": "Failed to parse JSON", "raw_output": json_output}

        # Add candidate id and timestamp.
        candidate_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()
        candidate_data["candidate_id"] = candidate_id
        candidate_data["timestamp"] = timestamp

        # Save the data to a file.
        filename = os.path.join(self.data_dir, f"{candidate_id}.json")
        with open(filename, "w") as f:
            json.dump(candidate_data, f, indent=2)

        final_message = f"Interview finalized. Your Candidate ID is {candidate_id}."
        return final_message


