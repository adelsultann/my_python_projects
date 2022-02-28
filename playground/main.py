from tkinter import *
root = Tk()

a = ["Adel", "Nasser"]

print(a)
for i in range(len(a)):
    a.pop()

print(a)


canvas = Canvas(root, width=600, height=300, highlightthickness=0)
canvas.grid(columnspan=3)
text_box = Text(root,bd=3,height=4,width=50
                )

text_box.insert(1.1,"this is adel")
text_box.tag_configure("center", justify="center")

text_box.tag_add("center", 1.0, "end")

text_box.grid(column=0,row=0,padx=15, pady=15)

root.mainloop()