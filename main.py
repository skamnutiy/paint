from tkinter.colorchooser import *
from tkinter import *

from data import config as c
from data.setup import load_image

brush_size = c.BRUSH_SIZE
color = c.DEFAULT_COLOR

def draw(event):
    x1 = event.x - brush_size
    y1 = event.y - brush_size
    x2 = event.x + brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1. x2, y2, fill=color, outline=color)
def active_paint(event):
    global brush_size
    global color
    w.bind("<B1-Motion>", draw)
    w.bind("<ButtonPress-1>", draw)

def decrease_brush_size():
    global brush_size
    if brush_size > 5:
        brush_size -= 1

def increase_brush_size():
    global brush_size
    if brush_size < 20:
        brush_size += 1

def color_change():
    pass
root = Tk()
root.title("Paint")

w = Canvas(root, width=c.WIDTH, height=c.HEIGHT, bg=c.BG_COLOR)
eraser_icon = load_image('eraser.png')
increase_icon = load_image('inbrush.png')
decrease_icon = load_image('debrush.png')
brush_icon = load_image('brush.png')
decrease_btn = Button(root, image=decrease_icon, command=decrease_brush_size)
increase_btn = Button(root, image=increase_icon, command=increase_brush_size)
brush_btn = Button(root, image=brush_icon, command=lambda : color_change())