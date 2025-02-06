import gradio as gr
from components.llm import LLM

def process_llm(message, history):
    history = history or []

    llm = LLM(query=message, history=history)
    response = llm.call_llm()
    
    return {"role": "assistant", "content": response}

  

if __name__ == "__main__":
    gr.ChatInterface(fn=process_llm, type="messages").launch()
