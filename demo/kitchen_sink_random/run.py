import gradio as gr
from datetime import datetime
import string
import os
import pandas as pd

from constants import (
    file_dir,
    img_dir,
    highlighted_text,
    highlighted_text_output_2,
    highlighted_text_output_1,
    random_plot,
    random_model3d,
)
import secrets


demo = gr.Interface(
    lambda *args: args[0],
    inputs=[
        gr.Textbox(value=lambda: datetime.now(), label="Current Time"),
        gr.Number(value=lambda: secrets.SystemRandom().random(), label="Ranom Percentage"),
        gr.Slider(minimum=-1, maximum=1, randomize=True, label="Slider with randomize"),
        gr.Slider(
            minimum=0,
            maximum=1,
            value=lambda: secrets.SystemRandom().random(),
            label="Slider with value func",
        ),
        gr.Checkbox(value=lambda: secrets.SystemRandom().random() > 0.5, label="Random Checkbox"),
        gr.CheckboxGroup(
            choices=["a", "b", "c", "d"],
            value=lambda: secrets.choice(["a", "b", "c", "d"]),
            label="Random CheckboxGroup",
        ),
        gr.Radio(
            choices=list(string.ascii_lowercase),
            value=lambda: secrets.choice(string.ascii_lowercase),
        ),
        gr.Dropdown(
            choices=["a", "b", "c", "d", "e"],
            value=lambda: secrets.choice(["a", "b", "c"]),
        ),
        gr.Image(
            value=lambda: secrets.choice([os.path.join(img_dir, img) for img in os.listdir(img_dir)]
            )
        ),
        gr.Video(value=lambda: os.path.join(file_dir, "world.mp4")),
        gr.Audio(value=lambda: os.path.join(file_dir, "cantina.wav")),
        gr.File(
            value=lambda: secrets.choice([os.path.join(file_dir, img) for img in os.listdir(file_dir)]
            )
        ),
        gr.Dataframe(
            value=lambda: pd.DataFrame(
                {"random_number_rows": range(secrets.SystemRandom().randint(0, 10))}
            )
        ),
        gr.State(value=lambda: secrets.choice(string.ascii_lowercase)),
        gr.ColorPicker(value=lambda: secrets.choice(["#000000", "#ff0000", "#0000FF"])),
        gr.Label(value=lambda: secrets.choice(["Pedestrian", "Car", "Cyclist"])),
        gr.HighlightedText(
            value=lambda: secrets.choice([
                    {"text": highlighted_text, "entities": highlighted_text_output_1},
                    {"text": highlighted_text, "entities": highlighted_text_output_2},
                ]
            ),
        ),
        gr.JSON(value=lambda: secrets.choice([{"a": 1}, {"b": 2}])),
        gr.HTML(
            value=lambda: secrets.choice([
                    '<p style="color:red;">I am red</p>',
                    '<p style="color:blue;">I am blue</p>',
                ]
            )
        ),
        gr.Gallery(
            value=lambda: [os.path.join(img_dir, img) for img in os.listdir(img_dir)]
        ),
        gr.Chatbot(
            value=lambda: secrets.choice([[("hello", "hi!")], [("bye", "goodbye!")]])
        ),
        gr.Model3D(value=random_model3d),
        gr.Plot(value=random_plot),
        gr.Markdown(value=lambda: f"### {secrets.choice(['Hello', 'Hi', 'Goodbye!'])}"),
    ],
    outputs=[
        gr.State(value=lambda: secrets.choice(string.ascii_lowercase))
    ],
)

if __name__ == "__main__":
    demo.launch()
