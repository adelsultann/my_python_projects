from tkinter import *
from PIL import Image, ImageTk
import random
import os


def display_logo(url, x, y):
    img = Image.open(url)
    img = img.resize((int(img.size[0] / 6), int(img.size[1] / 6)))
    img = ImageTk.PhotoImage(img)
    img_label = Label(image=img)
    img_label.image = img
    img_label.place(x=x, y=y)


def save_all(images):
    counter = 1
    for i in images:
        # mode is PIL object's attributes that allow us to show the mode of the picture
        if i.mode != "RGB":
            # convert is method in PIL to convert the picture
            i = i.convert("RGB")
            # save below is PL methods that allowed us to save picture
            # each time we save a picture we make a new name to the picture name
        i.save("img" + ".png", format="png")


