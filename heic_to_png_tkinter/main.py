from tkinter import *
from PIL import Image
import pillow_heif
from tkinter.filedialog import askopenfile
import os
import tkinter.messagebox
import random

# ----------------------------------- CONSTANTS------------------------------------

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Aharoni"

window = Tk()

window.title("heic to png")

# set up the size of the canvas
canvas = Canvas(width=500, height=222, bg=YELLOW, highlightthickness=0)
canvas.grid(column=2, row=1)


def heic_to_png(file):
    counter = random.randint(1, 50)

    path = "./heic_to_png"
    heif_file = pillow_heif.read_heif(file)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
    )
    try:

        os.mkdir(path)
        image.save(str(counter) + ".png", format("png"))
        tkinter.messagebox.showerror(title="Done", message="Saved successfuly")
    except OSError:
        image.save(str(counter) + ".png", format("png"))
        tkinter.messagebox.showerror(title="Done", message="Saved successfuly")
    browse_text.set("browes")


def open_file():
    browse_text.set("loading")
    file = askopenfile(parent=window, mode="rb", title="Choose a Picture", filetypes=[
        ("image", ".heic"),
        ("image", ".HEIC"),
        ("image", ".heif"),
    ])
    if file:
        heic_to_png(file)


# instructions label text

instruction = Label(canvas, text="Choose Heic picture only", bg=YELLOW, font=(FONT_NAME, 15, "bold"))
instruction.place(x=120, y=100)

# bitton

browse_text = StringVar()
browse_button = Button(window, textvariable=browse_text, font=(FONT_NAME, 15, "bold"),
                       bg="#20bebe", fg="white", height=1, width=10, command=lambda: open_file())
browse_text.set("Browse")
browse_button.place(x=180, y=160)
window.mainloop()
