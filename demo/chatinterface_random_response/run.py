import gradio as gr
import secrets

def random_response(message, history):
    return secrets.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response)

if __name__ == "__main__":
    demo.launch()
