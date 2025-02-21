import os
from PIL import Image, ImageTk

PATH = os.path.dirname(os.path.dirname(__file__))

def load_image(name):
    location = os.path.join(PATH, 'resources', 'ions', name)
    img = Image.open(location).resize((20,20), Image.BICUBIC)
    return ImageTk.PhotoImage(img)