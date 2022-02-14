import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import random
import string

YELLOW = "#f7f5dd"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermark App")
        # set the dimensions of the tkinter
        self.geometry("300x100")
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)
        # background of the image
        self.config(bg=YELLOW)
        # create the widgets once the app is initialized
        self.create_widgets()

    def create_widgets(self):
        self.file_btn()
        self.quit_btn()

    def file_btn(self):
        self.button = tk.Button(text="Search for Picture", command=self.fileDailog)
        self.button.grid(column=0, row=0, sticky=tk.W, pady=10)

    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir="C:/Users/Adel/Desktop", title="Select A File",
                                                   filetype=(("jpeg", "*.jpg"), ("png", "*.png")))
        self.label = tk.Label(text="Image Upload")
        self.label.grid(sticky=tk.N)
        # to show the full path of the uploaded picture
        self.label.configure(text=self.fileName)
        self.watermark_image()

    def quit_btn(self):
        self.quit_button = tk.Button(self, text='Quit',
                                     command=self.quit)
        self.quit_button.grid(column=0, row=1, sticky=tk.W)

    def watermark_image(self):
        # opens image
        image = self.fileName
        image = Image.open(image)

        # copies image to make changes
        watermark_image = image.copy()
        draw = ImageDraw.Draw(watermark_image)

        # selects font
        font = ImageFont.truetype("arial.ttf", 30)

        # add watermark
        draw.text((0, 0), 'watermark', "red", font=font)

        # save the image
        self.save_image(watermark_image)

    def save_image(self, image):
        # Create a directory for the watermark pictures
        try:
            path = "C:/Users/Adel/Desktop/DeskTop/Programming/my python project/" \
                   "Watermarking_Desktop_App/watermarked_pic"
            os.mkdir(path)
            picture_file = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
            image.save(f'./watermarked_pic/{picture_file}.jpg')

            # generate random name to the picture file name



        except OSError:
            picture_file = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
            image.save(f'./watermarked_pic/{picture_file}.jpg')
            return print("Saved Successful")

        return print("Saved Successful")


app = App()
app.mainloop()
