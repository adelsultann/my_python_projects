import tkinter as tk
from PIL import ImageTk, Image
import PyPDF2
from tkinter.filedialog import askopenfile

# canvas = root.Canvas(root,width=600,height=300)

root = tk.Tk()

# set up the width and height of the app

canvas = tk.Canvas(root, width=600, height=300, highlightthickness=0)

# place the canvas
canvas.grid(columnspan=3)

# create the logo image and place it
logo_image = Image.open("logo.png")
logo_image = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(image=logo_image)
logo_label.image = logo_image
logo_label.grid(column=1, row=0)

# instruction

instruction = tk.Label(root, text="Select PDF file on your computer extract all its text", font="Raleway")
instruction.grid(columnspan=3, column=0, row=1, )


def open_file():
    # to change the button name to Loading
    brows_text.set("loading....")
    file = askopenfile(parent=root, mode="rb", title="Choose a File", filetype=[("Pdf file", "*pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        print(page_content)
        # make the extracted texts appears inside tboxext box
        text_box = tk.Text(root, height=8, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        # change the button text
        brows_text.set("Browse")


# browse button

brows_text = tk.StringVar()
# textvariable gives you the ability to change the words inside the button
brows_btn = tk.Button(root, textvariable=brows_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15,
                      command=open_file)
brows_text.set("Browse")
brows_btn.grid(column=1, row=2,padx=40,pady=50)

# to stretch the app from bottom so we can put the extracted text
canvas = tk.Canvas(root, width=600, height=250, highlightthickness=0)
canvas.grid(columnspan=3)

tk.mainloop()
