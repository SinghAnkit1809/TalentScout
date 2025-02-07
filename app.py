import gradio as gr
from components.llm import LLM

llm= LLM()
def process_llm(message, history):
    message =message.strip()
    if message.lower() == "exit":
        final_message = llm.finalize_interview()
        history.append(message, final_message)
        return "", history
    else:
        response = llm.conduct_interview(message)
        history.append(message, response)
        return "", history

if __name__ == "__main__":
    gr.ChatInterface(fn=process_llm, type="messages").launch()
