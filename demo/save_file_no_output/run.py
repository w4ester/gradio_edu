import string
import gradio as gr 
import secrets

def save_image_random_name(image):
    random_string = ''.join(secrets.SystemRandom().choices(string.ascii_letters, k=20)) + '.png'
    image.save(random_string)
    print(f"Saved image to {random_string}!")

demo = gr.Interface(
    fn=save_image_random_name, 
    inputs=gr.Image(type="pil"), 
    outputs=None,
)
if __name__ == "__main__":
    demo.launch()
