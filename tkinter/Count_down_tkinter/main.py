# import the time module
import time
from tkinter import *
from tkinter import messagebox
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
pygame.mixer.init()  # initialise the pygame

rest_timer = None


def time():
    timer = int(app_entry.get())

    timer = timer * 60
    countdown(timer)


def countdown(count):
    global rest_timer
    mins, secs = divmod(count, 60)
    canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(mins, secs))
    if count > 0:
        print(count)
        rest_timer = window.after(1000, countdown, count - 1)
    else:
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(loops=2)


def rest_timer():
    window.after_cancel(rest_timer)
    canvas.itemconfig(timer_text, text="00:00")


window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato - Copy.png")
timer_text = canvas.create_text(100, 128, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
# app_entry = Entry(width=60)

app_entry = Spinbox(from_=1,
                    to=60, )
app_entry.focus()
app_entry.place(x=100, y=60)
start_button = Button(text="start", font=(FONT_NAME, 15, "bold"), command=time)
start_button.grid(column=1, row=4)
rest_button = Button(text="Rest", font=(FONT_NAME, 15, "bold"), command=rest_timer)
rest_button.grid(column=3, row=4)
canvas.grid(column=2, row=2)
apps_label = Label(text="Choose How many minutes to Shutdown", fg=GREEN, bg="white", font=("Ariel", 15, "italic"))
apps_label.place(x=0, y=20)



window.mainloop()
