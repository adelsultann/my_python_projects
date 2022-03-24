import tkinter as tk
import time
import threading
import random


class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        # set up the dominion
        self.root.geometry("800x600")
        # to read the text file and separate each line
        self.texts = open("texts.txt", "r").readlines()
        # Frame widget is used to organize the
        # group of widgets. It acts like a container which can be used to hold the other widgets
        self.fram = tk.Frame(self.root)
        self.sample_label = tk.Label(self.fram, text=random.choice(self.texts), font=("Helvetica", 18))
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.input_entry = tk.Entry(self.fram, width=40, font=("Helvetica", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.fram, text="Speed:\n0.00 CPS\n0.00 CPM\n0.00 WPS \n0,00 WPM Character",
                                    font=("Helvetica", 18))
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.rest_button = tk.Button(self.fram, text="Rest", command=self.rest, font=("Helvetica", 18))
        self.rest_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.fram.pack(expand=True)

        self.counter = 0
        self.running = False

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
                # cget is a way to get text from Label in Tkinter
        if not self.sample_label.cget("text").startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget("text"):
            self.running = False
            self.input_entry.config(fg="green")

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            # character per seconds
            cps = len(self.input_entry.get()) / self.counter
            # character per minutes
            cpm = cps * 60

            # wrold per seconds
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            # 2f means two decimal places
            self.speed_label.config(text=f"SPeed: \n{cps:.2f}CPS \n{cpm:.2f}CPM\n {wps:.2f} WPS\n{wpm:.2f}WPM")

    def rest(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed:\n0.00 CPS\n0.00 CPM\n0.00 WPS \n0,00 WPM Character", )
        self.sample_label.config(text=random.choice(self.texts), font=("Helvetica", 18))
        self.input_entry.delete(0, tk.END)


TypeSpeedGUI()

tk.mainloop()
