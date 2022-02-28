import random
import tkinter.messagebox
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from functions import display_logo, save_all, save
import os
import random
images = []
orange_color = "#e9c46a"

root = Tk()

root.geometry("400x350")
root.maxsize(350, 350)
root.minsize(350, 350)

instructions = Label(root, text="Select a PDF file", font=("Raleway", 10), bg="white")
instructions.grid(column=2, row=0, sticky=SE, padx=75, pady=5)

header = Frame(root, width=400, height=150, bg=orange_color)
header.grid(column=1, row=0)

# main content area - text and image extraction ((middle area)
main_content = Frame(root, width=400, height=150, bg="white")
main_content.grid(column=1, row=1)

display_logo("transfer.png", 140, 10)


def open_file():
    file = askopenfile(parent=root, mode="rb", filetypes=[
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
        ("image", ".HEIC"),
    ])
    if file:
        pass

    tkinter.messagebox.showerror(title="Done", message="Saved successfuly")


# instructions
instructions = Label(root, text="Select a image file only ", font=("Raleway", 10), bg=orange_color)
instructions.grid(column=1, row=1, rowspan=1)

browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, command=lambda: open_file(), font=("Raleway", 12), bg="#20bebe",
                    fg="white", height=1, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)
canvas = Canvas(width=200, height=224, bg=orange_color, highlightthickness=0)
timer_text = canvas.create_text(100, 128, text="00:00", fill="black", font=("Raleway", 35, "bold"))

root.mainloop()
