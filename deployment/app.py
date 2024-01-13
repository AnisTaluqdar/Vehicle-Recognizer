from fastai.vision.all import *
import gradio as gr

# import pathlib  
# temp = pathlib.PosixPath
# pathlib.PosixPath = pathlib.WindowsPath

model = load_learner('models/Vehicle-recognizer-v1.pkl')


Vehicle_labels = model.dls.vocab
def recognize_image(image):
  pred, idx, probs = model.predict(image)
  return dict(zip(Vehicle_labels, map(float, probs)))

examples = [
    'test_images/bus.jpg',
    'test_images/train.jpg',
    'test_images/rowboat.jpg',
    'test_images/airplane.jpg'
    ]

iface = gr.Interface(title="Vehicle Recognizer", fn=recognize_image, inputs="image", outputs="label")
iface.launch(inline=False)