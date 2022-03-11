from tkinter import *
import time
import threading
import random

THEME_COLOR = "#375362"
FONT_NAME = "Aharoni"


class TypeSpeedGui:
    def __init__(self):
        self.root = Tk()
        self.root.title("Typing Speed Application")
        self.root.config(padx=30, pady=30, bg=THEME_COLOR)
        # set up the dimension of the app

        self.canvas = Canvas(width=750, height=500, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=4, rowspan=2)
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.rowconfigure(0, weight=1)
        self.app_instruction = Label(self.root, text="choose your difficulty", fg="white", bg=THEME_COLOR,
                                     font=(FONT_NAME, 18))
        self.app_instruction.grid(column=0, row=0)

        # easy button
        self.easy_button = Button(self.root, text="Easy", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 16),
                                  command=self.easy_choosen)
        self.easy_button.grid(column=1, row=0, )
        self.easy_button.columnconfigure(0, weight=1)

        # medium button
        self.medium_button = Button(self.root, text="medium", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 16),
                                    command=self.medium_choosen)
        self.medium_button.grid(column=2, row=0)
        self.medium_button.columnconfigure(0, weight=1)
        # Hard button
        self.hard_button = Button(self.root, text="Hard", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 16),
                                  command=self.hard_choosen)
        self.hard_button.grid(column=3, row=0)

        # retrieve data from the easy txt file
        self.easy_level = open("text_to_type/easy.txt", "r").readlines()
        self.medium_level = open("text_to_type/medium.txt", "r").readlines()
        self.hard_level = open("text_to_type/hard.txt", "r").readlines()

        self.input_entry = None
        self.text_to_write = None
        self.counter = 0
        self.running = False
        self.speed_label = None
        self.rest_button = None
        self.level = None

        self.root.mainloop()

    def easy_choosen(self):

        self.level = "easy"
        self.easy_button.grid_forget()
        self.medium_button.grid_forget()
        self.hard_button.grid_forget()
        self.app_instruction.grid_forget()
        self.input_entry = Entry(self.root, width=40, font=("Helvetica", 24))
        self.input_entry.columnconfigure(0, weight=1)
        self.input_entry.grid(row=0, column=0, columnspan=1)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.text_to_write = Label(self.root, text=random.choice(self.easy_level), fg="white", bg=THEME_COLOR
                                   , font=(FONT_NAME, 25))
        self.text_to_write.grid(column=0, row=0, sticky=N)
        self.speed_label = Label(self.root, text="Speed:\n0,00 WPM Character",
                                 fg="white", bg=THEME_COLOR
                                 , font=(FONT_NAME, 25))
        self.speed_label.grid(column=0, row=1)

        self.back_button = Button(self.root, text="Back", command=self.back_button, font=("Helvetica", 18))
        self.back_button.grid(row=2, column=0)

        self.change_word = Button(self.root, text="Change Sentence", command=self.change_word, font=("Helvetica", 18))
        self.change_word.grid(row=0, column=0, sticky=SE)
        self.change_word.grid_rowconfigure(1, weight=1)
        self.change_word.grid_columnconfigure(1, weight=1)

    def medium_choosen(self):

        self.level = "medium"
        self.easy_button.grid_forget()
        self.medium_button.grid_forget()
        self.hard_button.grid_forget()
        self.app_instruction.grid_forget()
        self.input_entry = Entry(self.root, width=40, font=("Helvetica", 24))
        self.input_entry.columnconfigure(0, weight=1)
        self.input_entry.grid(row=0, column=0, columnspan=1)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.text_to_write = Label(self.root, text=random.choice(self.medium_level), fg="white", bg=THEME_COLOR
                                   , font=(FONT_NAME, 25))
        self.text_to_write.grid(column=0, row=0, sticky=N)
        self.speed_label = Label(self.root, text="Speed:\n0,00 WPM Character",
                                 fg="white", bg=THEME_COLOR
                                 , font=(FONT_NAME, 25))
        self.speed_label.grid(column=0, row=1)

        self.back_button = Button(self.root, text="Back", command=self.back_button, font=("Helvetica", 18))
        self.back_button.grid(row=2, column=0)

        self.change_word = Button(self.root, text="Change Sentence", command=self.change_word, font=("Helvetica", 18))
        self.change_word.grid(row=0, column=0, sticky=SE)
        self.change_word.grid_rowconfigure(1, weight=1)
        self.change_word.grid_columnconfigure(1, weight=1)

    def hard_choosen(self):

        self.level = "hard"
        self.easy_button.grid_forget()
        self.medium_button.grid_forget()
        self.hard_button.grid_forget()
        self.app_instruction.grid_forget()
        self.input_entry = Entry(self.root, width=40, font=("Helvetica", 24))
        self.input_entry.columnconfigure(0, weight=1)
        self.input_entry.grid(row=0, column=0, columnspan=1)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.text_to_write = Label(self.root, text=random.choice(self.hard_level), fg="white", bg=THEME_COLOR
                                   , font=(FONT_NAME, 25))
        self.text_to_write.grid(column=0, row=0, sticky=N)
        self.speed_label = Label(self.root, text="Speed:\n0,00 WPM Character",
                                 fg="white", bg=THEME_COLOR
                                 , font=(FONT_NAME, 25))
        self.speed_label.grid(column=0, row=1)

        self.back_button = Button(self.root, text="Back", command=self.back_button, font=("Helvetica", 18))
        self.back_button.grid(row=2, column=0)

        self.change_word = Button(self.root, text="Change Sentence", command=self.change_word, font=("Helvetica", 18))
        self.change_word.grid(row=0, column=0, sticky=SE)
        self.change_word.grid_rowconfigure(1, weight=1)
        self.change_word.grid_columnconfigure(1, weight=1)

    def start(self, event):
        if not self.running:
            # keycode is number that represent key in the keyboard for example 9 = left TAB
            if not event.keycode in [16, 17, 18, 9]:
                self.running = True
                # create two new threads
                # we use threads to run the app very fast
                t = threading.Thread(target=self.time_thread)
                # this is how to start the threads
                t.start()
        if not self.text_to_write.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        # The rstrip() method returns a copy of the string in which all chars have been stripped from the end of the string
        # best way to watch the accurate
        if self.input_entry.get().rstrip() == self.text_to_write.cget("text").rstrip():
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            # this is how to get the character per seconds
            cps = len(self.input_entry.get()) / self.counter
            print(f"this is {cps}")
            # character per minutes
            cpm = cps * 60
            # to calculate word per minutes you need to divid the total words by the total seconds then multiple it by 60
            # wrold per seconds
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            # 2f means two decimal places
            self.speed_label.config(text=f"SPeed:{wps:.2f} WPS\n{wpm:.2f}WPM")

    def back_button(self):
        self.root.destroy()
        g = TypeSpeedGui()

    def change_word(self):

        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed:0.00 WPS \n0,00 WPM Character", )
        if self.level == "easy":
            self.text_to_write.config(text=random.choice(self.easy_level), font=("Helvetica", 18))


        elif self.level == "medium":
            self.text_to_write.config(text=random.choice(self.medium_level), font=("Helvetica", 18))


        else:
            self.text_to_write.config(text=random.choice(self.hard_level), font=("Helvetica", 18))
            self.change_word = Button(self.root, text="Change Sentence", command=self.change_word,
                                      font=("Helvetica", 18))

        self.input_entry.delete(0, END)


g = TypeSpeedGui()
