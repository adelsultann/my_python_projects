from tkinter import *


root = Tk()



class temp_frame:

    def __init__(self, master):
        self.master = master
        self.secondary_win = None
        self.btn_next = Button(self.master, text="Forward", command=self.Forward)
        self.btn_next.pack()


    def Forward(self):
        # Open secondary Window
        if not self.secondary_win:
            self.secondary_win = Toplevel()
            back_btn = Button(self.secondary_win, text="Back", command=self.Backward)
            back_btn.pack()
            self.master.withdraw()
        else:
            self.secondary_win.deiconify()
            self.master.withdraw()



    def Backward(self):
        self.secondary_win.withdraw()
        self.master.deiconify()


temp = temp_frame(root)

root.mainloop()