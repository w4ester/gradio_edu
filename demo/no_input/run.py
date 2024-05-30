import gradio as gr
import secrets

sentence_list = [
    "Good morning!",
    "Prayers are with you, have a safe day!",
    "I love you!"
]


def random_sentence():
    return sentence_list[secrets.SystemRandom().randint(0, 2)]


demo = gr.Interface(fn=random_sentence, inputs=None, outputs="text")

if __name__ == "__main__":
    demo.launch()
