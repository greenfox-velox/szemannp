from tkinter import *

root = Tk()

size = 600

canvas = Canvas(root, width = size, height = size, bg = 'green')
canvas.pack()

def recursive_drawing(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size)
    if size <= 3:
        pass
    else:
        recursive_drawing(x + size / 3, y, size / 3)
        recursive_drawing(x, y + size / 3, size / 3)
        recursive_drawing(x + size / 3 * 2, y + size / 3, size / 3)
        recursive_drawing(x + size / 3, y + size / 3 * 2, size / 3)

recursive_drawing(1, 1, 600)

root.mainloop()
