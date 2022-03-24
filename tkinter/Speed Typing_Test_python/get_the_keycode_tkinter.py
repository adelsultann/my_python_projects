import tkinter as tk

# --- functions ---

def on_press(event):
    # display pressed key
    #print(event)
    print('PRESS   | keycode: {}, keysym: {}, char: {}'.format(event.keycode, event.keysym, event.char))

def on_release(event):
    # display released key
    #print(event)
    print('RELEASE | keycode: {}, keysym: {}, char: {}'.format(event.keycode, event.keysym, event.char))

    # exit program on ESC
    #if event.keysym == 'Escape':
    #     root.destroy()

# --- main ---

root = tk.Tk()

# assign functions to events
root.bind('<KeyPress>', on_press)
root.bind('<KeyRelease>', on_release)

root.mainloop()
