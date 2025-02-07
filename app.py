import gradio as gr
from components.llm import LLM

llm= LLM()
def process_llm(message, history):
    message =message.strip()
    if message.lower() == "exit":
        final_message = llm.finalize_interview()
        history.append((message, final_message))
        return "", history
    else:
        response = llm.conduct_interview(message)
        history.append((message, response))
        return "", history
with gr.Blocks() as demo:
    gr.Markdown("## TalentScout Hiring Assistant")
    gr.Markdown("# Type Exit to end the conversation")
    chatbot = gr.Chatbot()
    user_input = gr.Textbox(label="Your Message")
    user_input.submit(process_llm, [user_input, chatbot], [user_input, chatbot])

if __name__ == "__main__":
    demo.launch()
