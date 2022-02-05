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
pygame.mixer.init()# initialise the pygame

def time():
    timer = int(app_entry.get())

    timer = timer * 60
    countdown(timer)


def countdown(count):
    mins, secs = divmod(count, 60)
    canvas.itemconfig(timer_text, text='{:02d}:{:02d}'.format(mins, secs))
    if count > 0:
        print(count)
        window.after(1000, countdown, count - 1)
    else:
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play(loops=2)
















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
app_entry.grid(column=2, row=1)
start_button = Button(text="start", font=(FONT_NAME, 15, "bold"), command=time)
start_button.grid(column=1, row=4)
rest_button = Button(text="Rest", font=(FONT_NAME, 15, "bold"), )
rest_button.grid(column=3, row=4)
canvas.grid(column=2, row=2)
# countdown(5)


window.mainloop()

#
# should_count = True
#
#
# while should_count:
#
#     # input time in seconds
#
#     try:
#         t = int(input("enter a number "))
#         seconds = 60 * t
#         print(seconds)
#         #
#         # function call
#         countdown(int(seconds))
#     except ValueError:
#         print("only Numbers are allowed ")
#     finally:
#         result = input("do you want to go again 'yes or 'No'").lower()
#
#     if result == "no":
#         should_count == False
#         print("good bye")
#
#
#
#
